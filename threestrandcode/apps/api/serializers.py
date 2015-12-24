from rest_framework import serializers

from applicants.models import Applicant
from homework.models import Assignment


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ('name', 'email', 'essay')


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = (
            'user',
            'created',
            'started',
            'pre_reqs_completed',
            'completed',
        )
