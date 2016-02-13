from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Artist(models.Model):
    name = models.CharField(max_length=500, unique=True)
    songkick_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class ArtistRating(models.Model):
    RATING_LOVE = 1
    RATING_LIKE = 2
    RATING_KNOW = 3
    RATING_NO = 4
    RATING_UNRATED = 5

    RATING_CHOICES = (
        (RATING_LOVE, _('Love')),
        (RATING_LIKE, _('Like')),
        (RATING_KNOW, _('Know')),
        (RATING_NO, _('Do not like')),
        (RATING_UNRATED, _('Not yet rated')),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    artist = models.ForeignKey(Artist)
    rating = models.IntegerField(choices=RATING_CHOICES)

    class Meta:
        ordering = ('artist__name', )
        unique_together = ('user', 'artist')

    def __str__(self):
        return u'{} - {}'.format(self.artist.name, self.user.get_full_name())


class Event(models.Model):
    name = models.CharField(max_length=500)
    artist = models.ForeignKey(Artist)
    location = models.CharField(_('Location'), max_length=500)
    date_time = models.DateTimeField(_('Date & Time'))
    bandsintown_id = models.CharField('BandsInTown ID', max_length=100, null=True, blank=True)
    songkick_id = models.IntegerField('Songkick ID', null=True, blank=True)

    def __str__(self):
        return u'{} {}'.format(self.name, self.date_time)


class EventRSVP(models.Model):
    RSVP_YES = 1
    RSVP_NO = 2
    RSVP_UNKNOWN = 3

    RSVP_CHOICES = (
        (RSVP_YES, _('Yes')),
        (RSVP_NO, _('No')),
        (RSVP_UNKNOWN, _('Unknown')),
    )
    rsvp = models.IntegerField(choices=RSVP_CHOICES)
    event = models.ForeignKey(Event)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return u'{} - {} - {}'.format(self.event, self.user, self.get_rsvp_display())

    class Meta:
        unique_together = ('event', 'user')
