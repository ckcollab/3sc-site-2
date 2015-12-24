from django.conf.urls import include, url
from django.contrib import admin

from pages.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^api/', include('api.urls', namespace="api")),

    # 3rd party
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]
