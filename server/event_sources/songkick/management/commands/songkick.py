import requests
from datetime import datetime
from django.core.management import BaseCommand
from django.conf import settings

from liveinconcert.models import Artist, Event, Venue


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.sync_artist_ids()
        self.import_events()
        self.sync_venue_ids()
        self.import_venue_events()

    def sync_artist_ids(self):
        for artist in Artist.objects.filter(songkick_id__isnull=True):
            response = requests.get('http://api.songkick.com/api/3.0/search/artists.json', params={
                'query': artist.name,
                'apikey': settings.SONGKICK_API_KEY,
            })
            results = response.json()['resultsPage']['results']

            if 'artist' in results:
                print('Found artist {}'.format(artist.name, results['artist'][0]['id']))
                artist.songkick_id = results['artist'][0]['id']
                artist.save()
            else:
                print('Artist not found {}'.format(artist.name))

    def import_events(self):
        for artist in Artist.objects.filter(songkick_id__isnull=False):
            response = requests.get('http://api.songkick.com/api/3.0/artists/{}/calendar.json'.format(
                    artist.songkick_id), params={'apikey': settings.SONGKICK_API_KEY})
            results = response.json()['resultsPage']['results']

            if 'event' in results:
                for event in results['event']:
                    if event['venue']['metroArea']['country']['displayName'] == 'Switzerland':
                        if event['start']['datetime']:
                            date_time = datetime.strptime(event['start']['datetime'], '%Y-%m-%dT%H:%M:%S%z')
                        else:
                            date_time = datetime.strptime(event['start']['date'], '%Y-%m-%d')

                        # skip duplicate events with the same name and date (but potentially not the same time)
                        if Event.objects.exclude(songkick_id=event['id'])\
                                .filter(name=event['displayName'], date_time__date=date_time.date()).exists():
                            continue

                        event_obj, _ = Event.objects.update_or_create(songkick_id=event['id'], defaults={
                            'name': event['displayName'],
                            'artist': artist,
                            'location': event['venue']['displayName'],
                            'date_time': date_time,
                            'songkick_id': event['id'],
                        })
                        print('Found event for {}: {}'.format(artist.name, event['displayName']))

    def sync_venue_ids(self):
        for venue in Venue.objects.filter(songkick_id__isnull=True):
            response = requests.get('http://api.songkick.com/api/3.0/search/venues.json', params={
                'query': venue.name,
                'apikey': settings.SONGKICK_API_KEY,
            })
            results = response.json()['resultsPage']['results']

            if 'venue' in results:
                print('Found venue {}'.format(venue.name, results['venue'][0]['id']))
                venue.songkick_id = results['venue'][0]['id']
                venue.save()
            else:
                print('Venue not found {}'.format(venue.name))

    def import_venue_events(self):
        for venue in Venue.objects.filter(songkick_id__isnull=False):
            response = requests.get('http://api.songkick.com/api/3.0/venues/{}/calendar.json'.format(
                    venue.songkick_id), params={'apikey': settings.SONGKICK_API_KEY})
            results = response.json()['resultsPage']['results']

            if 'event' in results:
                for event in results['event']:
                    if event['start']['datetime']:
                        date_time = datetime.strptime(event['start']['datetime'], '%Y-%m-%dT%H:%M:%S%z')
                    else:
                        date_time = datetime.strptime(event['start']['date'], '%Y-%m-%d')

                    # skip duplicate events with the same name and date (but potentially not the same time)
                    if Event.objects.exclude(songkick_id=event['id'])\
                            .filter(name=event['displayName'], date_time__date=date_time.date()).exists():
                        continue

                    artist, _ = Artist.objects.get_or_create(songkick_id=event['performance'][0]['artist']['id'],
                                                             defaults={
                        'name': event['performance'][0]['artist']['displayName']})

                    event_obj, _ = Event.objects.update_or_create(songkick_id=event['id'], defaults={
                        'name': event['displayName'],
                        'artist': artist,
                        'venue': venue,
                        'location': event['venue']['displayName'],
                        'date_time': date_time,
                        'songkick_id': event['id'],
                    })
                    print('Found event for {}: {}'.format(venue.name, event['displayName']))
