from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
    url(r'^api/auth/$', obtain_jwt_token),

    url(r'^', TemplateView.as_view(template_name='frontend/index.html'))
]
