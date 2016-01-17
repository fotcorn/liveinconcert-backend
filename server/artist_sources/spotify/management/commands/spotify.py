import spotipy
import spotipy.util as util

from django.contrib.auth.models import User
from django.core.management import BaseCommand, CommandError

from liveinconcert.models import Artist, ArtistRating


def traverse_dict(dictionary, *args):
    for key in args:
        if key in dictionary:
            dictionary = dictionary[key]
        else:
            return None
    return dictionary


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('spotify_username', type=str)

    def handle(self, *args, **options):
        username = options['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise CommandError(u'User with username "{}" does not exist'.format(username))

        spotify_user = options['spotify_username']
        token = util.prompt_for_user_token(spotify_user,
                                           scope='playlist-read-private user-library-read user-follow-read')
        self.sp = spotipy.Spotify(auth=token)

        artists = set()
        artists.update(self.get_playlist_artists(spotify_user))
        artists.update(self.get_library_artists())
        artists.update(self.get_followed_artists())

        for artist in artists:
            try:
                artist_obj = Artist.objects.get(name__iexact=artist)
            except Artist.DoesNotExist:
                artist_obj = Artist.objects.create(name=artist)
            ArtistRating.objects.get_or_create(artist=artist_obj, user=user,
                                               defaults={'rating': ArtistRating.RATING_UNRATED})

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
            playlists = self.sp.user_playlists(user, limit=page_size, offset=offset)

            if not len(playlists['items']):
                break
            for playlist in playlists['items']:
                print(playlist['name'])
                try:
                    tracks = traverse_dict(self.sp.user_playlist(user, playlist['id'], 'tracks'), 'tracks', 'items')
                except KeyboardInterrupt:
                    raise CommandError('Interrupted')
                except spotipy.SpotifyException:
                    pass

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
