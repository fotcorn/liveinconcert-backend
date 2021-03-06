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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)

    class Meta:
        ordering = ('artist__name', )
        unique_together = ('user', 'artist')

    def __str__(self):
        return u'{} - {}'.format(self.artist.name, self.user.get_full_name())


class Venue(models.Model):
    name = models.CharField(max_length=500)
    songkick_id = models.IntegerField('Songkick ID', null=True, blank=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=500)
    venue = models.ForeignKey(Venue, null=True, blank=True, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    location = models.CharField(_('Location'), max_length=500)
    date_time = models.DateTimeField(_('Date & Time'))
    bandsintown_id = models.CharField('BandsInTown ID', max_length=100, null=True, blank=True)
    songkick_id = models.IntegerField('Songkick ID', null=True, blank=True)

    def url(self):
        if self.bandsintown_id:
            return 'http://www.bandsintown.com/event/{}'.format(self.bandsintown_id)
        elif self.songkick_id:
            return 'http://www.songkick.com/concerts/{}'.format(self.songkick_id)

    def __str__(self):
        return u'{} {}'.format(self.name, self.date_time)

    class Meta:
        ordering = ('date_time',)


class EventRSVP(models.Model):
    RSVP_YES = 'yes'
    RSVP_NO = 'no'
    RSVP_UNKNOWN = 'not_yet_answered'

    RSVP_CHOICES = (
        (RSVP_YES, _('Yes')),
        (RSVP_NO, _('No')),
        (RSVP_UNKNOWN, _('No yet answered')),
    )
    rsvp = models.CharField(choices=RSVP_CHOICES, max_length=20)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return u'{} - {} - {}'.format(self.event, self.user, self.get_rsvp_display())

    class Meta:
        unique_together = ('event', 'user')
