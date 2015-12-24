from rest_framework import viewsets

from . import serializers
from applicants.models import Applicant


class ApplicationViewSet(viewsets.ModelViewSet):

    queryset = Applicant.objects.all()
    serializer_class = serializers.ApplicationSerializer

