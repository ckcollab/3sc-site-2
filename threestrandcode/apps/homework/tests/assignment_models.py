from django.contrib.auth.models import User
from django.test import TestCase

from homework.models import github as gh_assignments


class PreReqCheckTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")

    def test_pre_reqs_check_at_least_one_level(self):
        assignment = gh_assignments.MakeRepository.objects.create(user=self.user)
        assert gh_assignments.GithubSignUp in assignment.get_missing_pre_reqs()
        gh_assignments.GithubSignUp.objects.create(user=self.user, completed=True)
        assert not assignment.get_missing_pre_reqs()

    def test_pre_reqs_check_work_inherited(self):
        # To make a github page we need to make a repo but before that we need to sign up on github!
        assignment = gh_assignments.MakeGHPage.objects.create(user=self.user)
        assert gh_assignments.MakeRepository in assignment.get_missing_pre_reqs()
        # So we sign up, but still not all pre-reqs supplied
        gh_assignments.GithubSignUp.objects.create(user=self.user, completed=True)
        assert gh_assignments.MakeRepository in assignment.get_missing_pre_reqs()
        gh_assignments.MakeRepository.objects.create(user=self.user, completed=True)
        assert not assignment.get_missing_pre_reqs()

    def test_do_pre_req_check_overload_works(self):
        assignment = gh_assignments.GithubSignUp.objects.create(user=self.user)
        missing_pre_reqs = assignment.get_missing_pre_reqs()
        assert missing_pre_reqs == "I need your github username first"
