import requests

from django.core.management import BaseCommand
from django.conf import settings

from liveinconcert.models import Artist


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.sync_artist_ids()

    def sync_artist_ids(self):
        for artist in Artist.objects.filter(songkick_id__isnull=True):
            response = requests.get('http://api.songkick.com/api/3.0/search/artists.json', params={
                'query': artist.name,
                'apikey': settings.SONGKICK_API_KEY,
            })
            results = response.json()['resultsPage']['results']

            if 'artist' in results:
                print('Found artist: {}'.format(artist.name, results['artist'][0]['id']))
                artist.songkick_id = results['artist'][0]['id']
                artist.save()
            else:
                print('Artist not found: {}'.format(artist.name))


        # http://api.songkick.com/api/3.0/artists/{artist_id}/calendar.json?apikey={your_api_key}