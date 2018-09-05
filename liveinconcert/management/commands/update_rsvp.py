from collections import defaultdict

from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.utils import timezone

from liveinconcert.models import Event, ArtistRating, EventRSVP
from push.send import send_message


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = defaultdict(lambda: 0)
        for event in Event.objects.filter(date_time__gt=timezone.now()):
            for rating in event.artist.artistrating_set.exclude(rating=ArtistRating.RATING_NO):
                if not EventRSVP.objects.filter(event=event, user=rating.user).exists():
                    users[rating.user.pk] += 1
                    EventRSVP.objects.create(event=event, user=rating.user, rsvp=EventRSVP.RSVP_UNKNOWN)

        for user_pk, count in users.items():
            user = User.objects.get(pk=user_pk)
            for token in user.firebasepushtoken_set.all():
                send_message(token.token, '{} new concerts for you!'.format(count))
