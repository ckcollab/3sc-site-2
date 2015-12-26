from django.conf.urls import include, url
from django.contrib import admin

from pages.views import home, apply, init

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^apply/', apply, name='apply'),
    url(r'^init/', init, name='init'),

    url(r'^api/', include('api.urls', namespace="api")),
    url(r'^rest-auth/', include('rest_auth.urls')),

    # 3rd party
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
]
