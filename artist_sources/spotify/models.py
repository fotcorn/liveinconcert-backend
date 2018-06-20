from django.db import models
from django.conf import settings


class SpotifyProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(max_length=1000)
    access_token = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.user.username} Spotify: {self.username}'
