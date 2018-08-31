from django.utils import timezone
import graphene
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from graphene import relay
from graphene_django.filter.fields import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
from rest_framework import serializers

from api.base import RelaySerializerMutation
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
        filter_fields = ['rsvp', ]
        interfaces = (relay.Node,)


class EventRSVPSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRSVP
        fields = ('rsvp',)


class EventRSVPMutation(RelaySerializerMutation):
    class Meta:
        serializer_class = EventRSVPSerializer
        model_operations = ['update']


class UserNode(DjangoObjectType):
    class Meta:
        model = User


class Login(graphene.Mutation):
    user = graphene.Field(UserNode)

    class Arguments:
        username = graphene.String()
        password = graphene.String()

    Output = UserNode

    @staticmethod
    def mutate(root, info, **input):
        user = authenticate(
            username=input.get('username'),
            password=input.get('password'),
        )

        if not user:
            raise Exception('Invalid username or password!')

        login(info.context, user)

        return user


class Mutations(graphene.ObjectType):
    login = Login.Field()
    update_rsvp = EventRSVPMutation.Field()


class Query(graphene.ObjectType):
    event_rsvps = DjangoFilterConnectionField(EventRSVPNode)

    def resolve_event_rsvps(self, info, **kwargs):
        return EventRSVP.objects \
            .order_by('event__date_time') \
            .filter(event__date_time__gt=timezone.now()) \
            .filter(**kwargs) \
            .select_related('event', 'event__artist')


# do not filter by user
# def resolve_event_rsvps(self, info):
#     # context will reference to the Django request
#     if not info.context.user.is_authenticated:
#         return EventRSVP.objects.none()
#     else:
#         return EventRSVP.objects.filter(user=info.context.user)


schema = graphene.Schema(query=Query, mutation=Mutations)
