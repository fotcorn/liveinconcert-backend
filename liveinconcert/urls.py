from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from graphene_django.views import GraphQLView
import push.urls
from artist_sources.spotify import urls as spotify_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('push/', include(push.urls)),
    path('spotify/', include(spotify_url)),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
