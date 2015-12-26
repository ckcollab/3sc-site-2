from rest_framework import serializers

from applicants.models import Applicant
from homework.models import Assignment, Recipe


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


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            "creator",
            "created",
            "point_min",
            "point_max",
            "instructions",
            "module",
        )
