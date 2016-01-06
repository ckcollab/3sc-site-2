from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from rest_framework import serializers

from applicants.models import Applicant
from homework.models import Assignment, Recipe

from rest_auth.serializers import LoginSerializer


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


class EmailLoginSerializer(LoginSerializer):
    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')

        print(attrs)

        if email and password:
            print("UH HELLO??")
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
