from django.conf.urls import url, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'artist', views.ArtistViewSet)
router.register(r'artistrating', views.ArtistRatingViewSet, 'artistrating')
router.register(r'event', views.EventViewSet)
router.register(r'eventrsvp', views.EventRSVPViewSet, 'eventrsvp')

urlpatterns = [
    url(r'^', include(router.urls)),
]
