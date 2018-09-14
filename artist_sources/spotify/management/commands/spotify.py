import spotipy
from django.core.management import BaseCommand, CommandError

from artist_sources.spotify.models import SpotifyProfile
from artist_sources.spotify.views import get_oauth
from liveinconcert.models import Artist, ArtistRating


def traverse_dict(dictionary, *args):
    for key in args:
        if key in dictionary:
            dictionary = dictionary[key]
        else:
            return None
    return dictionary


class Command(BaseCommand):

    def handle(self, *args, **options):
        for spotify_profile in SpotifyProfile.objects.all():
            try:
                oauth = get_oauth()
                token = oauth.refresh_access_token(spotify_profile.refresh_token)
                spotify_profile.access_token = token['access_token']
                spotify_profile.refresh_token = token['refresh_token']
                spotify_profile.save()

                self.sp = spotipy.Spotify(auth=spotify_profile.access_token)

                artists = set()
                artists.update(self.get_playlist_artists(self.sp.me()['id']))
                artists.update(self.get_library_artists())
                artists.update(self.get_followed_artists())
                artists.discard('')

                for artist in artists:
                    try:
                        artist_obj = Artist.objects.get(name__iexact=artist)
                    except Artist.DoesNotExist:
                        artist_obj = Artist.objects.create(name=artist)
                    ArtistRating.objects.get_or_create(artist=artist_obj, user=spotify_profile.user,
                                                       defaults={'rating': ArtistRating.RATING_UNRATED})
            except:
                continue

    def get_followed_artists(self):
        artist_names = set()
        after = None
        while True:
            artists = self.sp.current_user_followed_artists(limit=10, after=after)
            artist_names.update(map(lambda a: a['name'], artists['artists']['items']))
            after = artists['artists']['cursors']['after']
            if after is None:
                break
        return artist_names

    def get_library_artists(self):
        artist_names = set()
        offset = 0
        page_size = 50

        while True:
            tracks = self.sp.current_user_saved_tracks(limit=page_size, offset=offset)
            if not len(tracks['items']):
                break
            for track in tracks['items']:
                artist_names.update(map(lambda a: a['name'], track['track']['artists']))
            offset += page_size
        return artist_names

    def get_playlist_artists(self, user):
        artist_names = set()
        offset = 0
        page_size = 50

        while True:
            playlists = self.sp.current_user_playlists(limit=page_size, offset=offset)

            if not len(playlists['items']):
                break
            for playlist in playlists['items']:
                print(playlist['name'])
                try:
                    tracks = traverse_dict(self.sp.user_playlist(user, playlist['id'], 'tracks'), 'tracks', 'items')
                except KeyboardInterrupt:
                    raise CommandError('Interrupted')
                except spotipy.SpotifyException as ex:
                    print(ex)
                    continue

                if not tracks:
                    continue

                for track in tracks:
                    artists = traverse_dict(track, 'track', 'artists')
                    if not artists:
                        continue
                    for artist in artists:
                        artist_names.add(artist['name'])

            offset += page_size
        return artist_names
