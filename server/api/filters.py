import django_filters

from liveinconcert.models import Event


class EventFilter(django_filters.FilterSet):
    min_date_time = django_filters.IsoDateTimeFilter(name='date_time', lookup_type='gte')
    max_date_time = django_filters.IsoDateTimeFilter(name='date_time', lookup_type='lte')

    class Meta:
        model = Event
        fields = ()
