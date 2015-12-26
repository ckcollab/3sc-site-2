from django.conf.urls import url, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'applicants', views.ApplicationViewSet, 'applicants')
router.register(r'assignments', views.AssignmentViewSet, 'assignments')
router.register(r'recipes', views.RecipeViewSet, 'recipes')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
