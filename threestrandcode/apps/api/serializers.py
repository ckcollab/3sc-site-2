from rest_framework import serializers

from applicants.models import Applicant


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Applicant
        fields = ('name', 'email', 'essay')
