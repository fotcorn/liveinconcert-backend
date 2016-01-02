
"""
Events GET
Artists GET
Login POST
ArtistRating GET/POST/PUT
RSVP GET/POST/PUT
"""

from rest_framework import viewsets, permissions

from api.filters import EventFilter
from api.serializers import ArtistSerializer, EventSerializer, ArtistRatingSerializer, EventRSVPSerializer
from liveinconcert.models import Artist, Event, ArtistRating, EventRSVP


class ArtistViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistRatingViewSet(viewsets.ModelViewSet):
    serializer_class = ArtistRatingSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return ArtistRating.objects.filter(user=self.request.user)


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_class = EventFilter


class EventRSVPViewSet(viewsets.ModelViewSet):
    serializer_class = EventRSVPSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return EventRSVP.objects.filter(user=self.request.user)
