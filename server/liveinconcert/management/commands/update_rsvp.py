from django.core.management import BaseCommand

from liveinconcert.models import Event, ArtistRating, EventRSVP


class Command(BaseCommand):
    def handle(self, *args, **options):
        for event in Event.objects.all():
            for rating in event.artist.artistrating_set.exclude(rating=ArtistRating.RATING_NO):
                EventRSVP.objects.get_or_create(event=event, user=rating.user,
                                                defaults={'rsvp': EventRSVP.RSVP_UNKNOWN})
