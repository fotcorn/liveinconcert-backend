from django.db import models
from django.conf import settings


class FirebasePushToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.TextField(unique=True)
