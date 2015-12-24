import responses

from django.contrib.auth.models import User
from django.test import TestCase

from ..models import GithubSignUp, MakeGHPage, MakeRepository
from applicants.models import Applicant


class GithubAssignmentTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.application = Applicant.objects.create(user=self.user, email="test@test.com")

    def test_check_github_signup_works(self):
        # try with empty github_name
        assignment = GithubSignUp.objects.create(user=self.user)
        assert not assignment.do_completed_check()

        with responses.RequestsMock() as rsps:
            self.application.github_name ="doesnt_exist"
            self.application.save()
            rsps.add(responses.GET, 'https://github.com/%s' % self.application.github_name, status=404)
            assert not assignment.do_completed_check()  # 404 response

            self.application.github_name = "ckcollab"
            self.application.save()
            rsps.add(responses.GET, 'https://github.com/%s' % self.application.github_name, status=200)
            assert assignment.do_completed_check()  # 200 response, it exists!

    def test_shiiiiiiiiiiiiiiiiiit(self):

        assert False, "What we need to do is github oauth... that way we can verify the ownership of the account!"
