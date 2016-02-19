
"""
Events GET
Artists GET
Login POST
ArtistRating GET/POST/PUT
RSVP GET/POST/PUT
"""
from datetime import date
from rest_framework import viewsets, permissions

from .filters import EventFilter
from .serializers import ArtistSerializer, EventSerializer, ArtistRatingSerializer, EventRSVPSerializer, VenueSerializer
from liveinconcert.models import Artist, Event, ArtistRating, EventRSVP, Venue


class ArtistViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class VenueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


class ArtistRatingViewSet(viewsets.ModelViewSet):
    serializer_class = ArtistRatingSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return ArtistRating.objects.filter(user=self.request.user)


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EventSerializer
    filter_class = EventFilter

    def get_queryset(self):
        return Event.objects.filter(date_time__date__gte=date.today())


class EventRSVPViewSet(viewsets.ModelViewSet):
    serializer_class = EventRSVPSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return EventRSVP.objects.filter(user=self.request.user)
