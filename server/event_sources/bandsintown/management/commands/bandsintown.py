from django.core.mail import send_mail
import requests
from urllib import quote_plus
from datetime import datetime

from django.core.management.base import BaseCommand
from django.conf import settings

from artist.models import Artist, ArtistRating
from event.models import Event



class Command(BaseCommand):
    def handle(self, *args, **options):
        for artist in Artist.objects.all():
            url = u'http://api.bandsintown.com/artists/{}/events.json?api_version=2.0&app_id=liveinconvert'\
                .format(quote_plus(artist.name.encode('utf-8')))

            ret = requests.get(url)
            if ret.status_code != 200:
                continue

            data = ret.json()
            if type(data) == dict:
                continue

            for event in data:
                if event['venue']['country'] != 'Switzerland':
                    continue

                event_obj, created = Event.objects.update_or_create(bandsintown_id=event['id'], defaults={
                    'name': event['title'],
                    'artist': artist,
                    'location': event['venue']['name'],
                    'date_time': datetime.strptime(event['datetime'], '%Y-%m-%dT%H:%M:%S'),
                    'bandsintown_id': event['id'],
                })

                if created:
                    for rating in artist.artistrating_set.filter(rating=ArtistRating.LIKE):
                        send_mail(u'New Concert for {}'.format(artist.name),
                                  u'{} {} {}'.format(event_obj.name, event_obj.artist, event_obj.date_time),
                                  settings.EMAIL_SENDER, [rating.user.email], fail_silently=False)
