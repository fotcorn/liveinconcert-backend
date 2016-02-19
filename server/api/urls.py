from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'artist', views.ArtistViewSet)
router.register(r'venue', views.VenueViewSet)
router.register(r'artistrating', views.ArtistRatingViewSet, 'artistrating')
router.register(r'event', views.EventViewSet, 'event')
router.register(r'eventrsvp', views.EventRSVPViewSet, 'eventrsvp')

urlpatterns = [
    url(r'^', include(router.urls)),
]
