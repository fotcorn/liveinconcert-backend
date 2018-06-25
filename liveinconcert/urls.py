from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from graphene_django.views import GraphQLView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    url(r'^api/auth/$', obtain_jwt_token),
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
]
