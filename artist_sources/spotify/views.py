from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import redirect
from spotipy.oauth2 import SpotifyOAuth

from artist_sources.spotify.models import SpotifyProfile


def _get_oauth():
    return SpotifyOAuth(client_id=settings.SPOTIPY_CLIENT_ID,
                        client_secret=settings.SPOTIPY_CLIENT_SECRET,
                        redirect_uri=settings.SPOTIPY_REDIRECT_URI,
                        scope=settings.SPOTIFY_SCOPES)


@login_required
def auth(request):
    oauth = _get_oauth()
    url = oauth.get_authorize_url()
    return redirect(url)


@login_required
def callback(request):
    code = request.GET.get('code')
    if not code:
        return HttpResponseBadRequest()

    oauth = _get_oauth()
    token = oauth.get_access_token(code)

    SpotifyProfile.objects.update_or_create(user=request.user, defaults={
        'access_token': token['access_token'],
        'refresh_token': token['refresh_token'],
    })

    return HttpResponse('OK')
