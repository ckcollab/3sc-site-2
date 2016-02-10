from django.contrib.auth.models import User
from django.test import TestCase

from model_mommy import mommy

from ..models import Assignment, Recipe, Course
from ..recipes import SignUp, MakeGHPage, MakeRepository
from applicants.models import Applicant


class GithubAssignmentTests(TestCase):

    def setUp(self):
        self.admin = User.objects.create_superuser(username="admin", password="test", email="admin@admin.com")
        self.application = Applicant.objects.create(email="test@test.com")
        self.user = self.application.user
        self.course = mommy.make(Course)
        self.sign_up_recipe = Recipe.objects.create(
            creator=self.admin,
            instructions='',
            module=SignUp.get_name(),
            course=self.course,
        )

    def test_check_github_signup_works(self):
        # try with empty github_name
        assignment = Assignment.objects.create(user=self.user, recipe=self.sign_up_recipe, completed=True)
        assert not assignment.recipe.get_class().do_completed_check(self.user)
        # set name
        self.application.github_name = "ckcollab"
        self.application.save()
        assert assignment.recipe.get_class().do_completed_check(self.user)
