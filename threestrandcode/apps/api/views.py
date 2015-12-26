from rest_framework import permissions
from rest_framework import viewsets

from . import serializers
from .permissions import IsSuperUserOrPOSTing
from applicants.models import Applicant
from homework.models import Assignment, Recipe


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = serializers.ApplicationSerializer
    permission_classes = (IsSuperUserOrPOSTing,)


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = serializers.AssignmentSerializer
    # TODO: Superuser can view/modify anything. Regular user can only view/modify their own
    #permission_classes = (permissions.,)

    # list method should just return for request.user not all!


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer
