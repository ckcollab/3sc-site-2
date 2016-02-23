from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from rest_framework import serializers

from applicants.models import Applicant
from homework.models import Assignment, Recipe, Path, Topic, Course

from rest_auth.serializers import LoginSerializer


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = (
            'first_name',
            'last_name',
            'email',
            'essay',
            'github_name',
        )


# ----------------------------------------------------------------------------
# Homework
# ----------------------------------------------------------------------------
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
            "course",
            "creator",
            "created",
            "points",
            "instructions",
            "module",
        )


class PathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path
        fields = (
            "topics",
            "title",
            "description",
        )


class TopicSerializer(serializers.ModelSerializer):
    # path = PathSerializer()

    class Meta:
        model = Topic
        fields = (
            "path",
            "title",
            "description",
        )


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            "topic",
            "title",
            "description",
        )

# ----------------------------------------------------------------------------
# EmailLogin
# ----------------------------------------------------------------------------
class EmailLoginSerializer(LoginSerializer):
    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
        elif username and password:
            user = authenticate(username=username, password=password)
        else:
            msg = 'Must include "username"/"email" and "password".'
            raise ValidationError(msg)

        # Did we get back an active user?
        if user:
            if not user.is_active:
                msg = 'User account is disabled.'
                raise ValidationError(msg)
        else:
            msg = 'Unable to log in with provided credentials.'
            raise ValidationError(msg)

        attrs['user'] = user
        return attrs
