from django.conf.urls import include, url
from django.contrib import admin

from pages.views import home

urlpatterns = [
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^api/', include('api.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
