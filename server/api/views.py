
"""
Events GET
Artists GET
Login POST
ArtistRating GET/POST/PUT
RSVP GET/POST/PUT
"""

from rest_framework import viewsets

from api.filters import EventFilter
from api.serializers import ArtistSerializer, EventSerializer
from liveinconcert.models import Artist, Event


class ArtistViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_class = EventFilter
