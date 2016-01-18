import requests
from urllib.parse import quote
from datetime import datetime

from django.core.management.base import BaseCommand

from liveinconcert.models import Artist, Event, ArtistRating, EventRSVP


class Command(BaseCommand):
    def handle(self, *args, **options):
        for artist in Artist.objects.all():
            print(artist)
            url = 'http://api.bandsintown.com/artists/{}/events.json?api_version=2.0&app_id=liveinconvert'\
                .format(quote(artist.name.encode('utf-8')))

            ret = requests.get(url)
            if ret.status_code != 200:
                continue

            data = ret.json()
            if type(data) == dict:
                continue

            for event in data:
                if event['venue']['country'] != 'Switzerland':
                    continue

                event_obj, _ = Event.objects.update_or_create(bandsintown_id=event['id'], defaults={
                    'name': event['title'],
                    'artist': artist,
                    'location': event['venue']['name'],
                    'date_time': datetime.strptime(event['datetime'], '%Y-%m-%dT%H:%M:%S'),
                    'bandsintown_id': event['id'],
                })

                for rating in artist.artistrating_set.exclude(rating=ArtistRating.RATING_NO):
                    EventRSVP.objects.get_or_create(event=event_obj, user=rating.user,
                                                    defaults={'rsvp': EventRSVP.RSVP_UNKNOWN})
