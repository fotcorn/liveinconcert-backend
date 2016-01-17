from django.contrib.auth.models import User
import spotipy
import spotipy.util as util

from django.core.management import BaseCommand, CommandError
from artist.models import Artist, ArtistRating


def traverse_dict(dictionary, *args):
    for key in args:
        if key in dictionary:
            dictionary = dictionary[key]
        else:
            return None
    return dictionary


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('username', type=unicode)
        parser.add_argument('spotify_username', type=unicode)

    def handle(self, *args, **options):
        # username = options['username']
        username = args[0]
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise CommandError(u'User with username "{}" does not exist'.format(username))

        # spotify_user = options['spotify_username']
        spotify_user = args[1]
        token = util.prompt_for_user_token(spotify_user)
        self.sp = spotipy.Spotify(auth=token)

        artists = self.get_playlist_artists(spotify_user)
        artists = list(artists)

        for artist in artists:
            try:
                artist_obj = Artist.objects.get(name__iexact=artist)
            except Artist.DoesNotExist:
                artist_obj = Artist.objects.create(name=artist)
            ArtistRating.objects.get_or_create(artist=artist_obj, user=user, defaults={'rating': ArtistRating.LIKE})

    def get_playlist_artists(self, user):
        artist_names = set()
        offset = 0
        page_size = 50

        while True:
            playlists = self.sp.user_playlists(user, limit=page_size, offset=offset)
            if not len(playlists['items']):
                break
            for playlist in playlists['items']:
                try:
                    tracks = traverse_dict(self.sp.user_playlist(user, playlist['id'], 'tracks'), 'tracks', 'items')
                except:
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
