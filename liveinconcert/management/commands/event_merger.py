from collections import defaultdict

from django.core.management import BaseCommand

from liveinconcert.models import Event


class Command(BaseCommand):
    def handle(self, *args, **options):
        event_dict = defaultdict(lambda: [])

        for event in Event.objects.all():
            name = '{}-{}'.format(event.artist.pk, event.date_time.date())
            event_dict[name].append(event)

        for events in filter(lambda event_list: len(event_list) > 1, event_dict.values()):
            main_event = events[0]
            for event in events[1:]:
                event.eventrsvp_set.update(event=main_event)
                event.delete()
