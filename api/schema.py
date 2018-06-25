import graphene
from graphene import relay
from graphene_django.filter.fields import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from liveinconcert.models import Artist, Venue, EventRSVP, ArtistRating, Event


class ArtistNode(DjangoObjectType):
    class Meta:
        model = Artist
        interfaces = (relay.Node,)


class ArtistRatingNode(DjangoObjectType):
    class Meta:
        model = ArtistRating
        interfaces = (relay.Node,)


class VenueNode(DjangoObjectType):
    class Meta:
        model = Venue
        interfaces = (relay.Node,)


class EventNode(DjangoObjectType):
    class Meta:
        model = Event
        filter_fields = ['date_time']
        interfaces = (relay.Node,)


class EventRSVPNode(DjangoObjectType):
    class Meta:
        model = EventRSVP
        filter_fields = ['rsvp',]
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    event_rsvps = DjangoFilterConnectionField(EventRSVPNode)


schema = graphene.Schema(query=Query)
