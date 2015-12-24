import responses

from django.contrib.auth.models import User
from django.test import TestCase

from ..models import GithubSignUp, MakeGHPage, MakeRepository
from applicants.models import Applicant


class GithubAssignmentTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.application = Applicant.objects.create(user=self.user, email="test@test.com", github_name="doesnt_exist")

    def test_check_github_signup_works(self):
        with responses.RequestsMock() as rsps:
            rsps.add(responses.GET, 'https://github.com/%s' % self.application.github_name, status=404)
            assignment = GithubSignUp.objects.create(user=self.user)
            assignment.do_completed_check()
            assert not GithubSignUp.objects.get(pk=assignment.pk).completed

            self.application.github_name = "ckcollab"
            self.application.save()
            rsps.add(responses.GET, 'https://github.com/%s' % self.application.github_name, status=200)
            assignment.do_completed_check()
            assert GithubSignUp.objects.get(pk=assignment.pk).completed
