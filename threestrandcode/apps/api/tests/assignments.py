import random

from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from faker import Factory
from loremipsum import generate_paragraph
from model_mommy import mommy

from applicants.models import Applicant
from homework.models import Course, Recipe
from homework.recipes import MakeGHPage


class TestAssignments(TestCase):

    def setUp(self):
        self.admin = User.objects.create_superuser(username="admin", password="test", email="admin@admin.com")
        self.user = User.objects.create_user(username="test", password="test", email="test@test.com")
        self.application = Applicant.objects.create(email="test@test.com", user=self.user)
        self.course = mommy.make(Course)
        self.make_gh_page_recipe = Recipe.objects.create(
            creator=self.admin,
            instructions='',
            module=MakeGHPage.get_name(),
            course=self.course,
        )

    def test_create_assignment_hooks_github_repo(self):
        # create user and all that shit
        # post to assignment endpoint
        # it should call "create_hook" on that repo
        self.client.login(username="test", password="test")
        self.client.post()
        pass
