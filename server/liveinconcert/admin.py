from django.contrib import admin
from .models import Artist, ArtistRating, Event, EventRSVP


class ArtistAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Artist, ArtistAdmin)
admin.site.register(ArtistRating)
admin.site.register(Event)
admin.site.register(EventRSVP)
