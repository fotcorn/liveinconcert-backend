from django.db import models
from django.conf import settings


class SpotifyProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='spotify_profile')
    access_token = models.CharField(max_length=1000)
    refresh_token = models.CharField(max_length=1000)

    def __str__(self):
        return self.user.username
