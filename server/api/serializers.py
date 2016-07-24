from rest_framework import serializers

from liveinconcert.models import Artist, Event, ArtistRating, EventRSVP, Venue


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name')


class ArtistRatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArtistRating
        fields = ('id', 'artist', 'rating')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    artist = ArtistSerializer()

    class Meta:
        model = Event
        fields = ('id', 'name', 'artist', 'location', 'date_time', 'url')


class EventRSVPSerializer(serializers.HyperlinkedModelSerializer):
    event = EventSerializer()

    class Meta:
        model = EventRSVP
        fields = ('id', 'event', 'rsvp')


class VenueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Venue
        fields = ('id', 'name')
