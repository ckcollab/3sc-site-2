from rest_framework import permissions
from rest_framework import viewsets

from . import serializers
from .permissions import IsSuperUserOrPOSTing
from applicants.models import Applicant


class ApplicationViewSet(viewsets.ModelViewSet):

    queryset = Applicant.objects.all()
    serializer_class = serializers.ApplicationSerializer
    permission_classes = (IsSuperUserOrPOSTing,)
