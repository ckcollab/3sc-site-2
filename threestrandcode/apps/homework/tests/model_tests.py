from django.contrib.auth.models import User
from django.test import TestCase

from model_mommy import mommy

#from homework.models import github as gh_assignments
from ..models import Assignment, Recipe, Course, Topic, Path
from ..recipes.github import SignUp, MakeRepository, MakeGHPage


class PreReqCheckTests(TestCase):

    def setUp(self):
        self.admin = User.objects.create_superuser(username="admin", password="test", email="admin@admin.com")
        self.user = User.objects.create_user(username="test", password="test")
        self.course = mommy.make(Course)
        self.sign_up_recipe = Recipe.objects.create(
            creator=self.admin,
            instructions='',
            module=SignUp.get_name(),
            course=self.course,
        )
        self.make_repo_recipe = Recipe.objects.create(
            creator=self.admin,
            instructions='',
            module=MakeRepository.get_name(),
            course=self.course,
        )
        self.make_ghpage_recipe = Recipe.objects.create(
            creator=self.admin,
            instructions='',
            module=MakeGHPage.get_name(),
            course=self.course,
        )

    def test_pre_reqs_check_at_least_one_level(self):
        assignment = Assignment.objects.create(user=self.user, recipe=self.make_repo_recipe)
        assert SignUp in assignment.recipe.get_class().get_missing_pre_reqs(self.user)
        Assignment.objects.create(user=self.user, recipe=self.sign_up_recipe, completed=True)
        assert not assignment.recipe.get_class().get_missing_pre_reqs(self.user)

    def test_pre_reqs_check_work_inherited(self):
        assignment = Assignment.objects.create(user=self.user, recipe=self.make_ghpage_recipe)
        assert SignUp, MakeRepository in assignment.recipe.get_class().get_missing_pre_reqs(self.user)
        Assignment.objects.create(user=self.user, recipe=self.sign_up_recipe, completed=True)
        assert MakeRepository in assignment.recipe.get_class().get_missing_pre_reqs(self.user)
        Assignment.objects.create(user=self.user, recipe=self.make_repo_recipe, completed=True)
        assert not assignment.recipe.get_class().get_missing_pre_reqs(self.user)


        # # To make a github page we need to make a repo but before that we need to sign up on github!
        # assignment = gh_assignments.MakeGHPage.objects.create(user=self.user)
        # assert gh_assignments.MakeRepository in assignment.get_missing_pre_reqs()
        # # So we sign up, but still not all pre-reqs supplied
        # gh_assignments.GithubSignUp.objects.create(user=self.user, completed=True)
        # assert gh_assignments.MakeRepository in assignment.get_missing_pre_reqs()
        # gh_assignments.MakeRepository.objects.create(user=self.user, completed=True)
        # assert not assignment.get_missing_pre_reqs()

    # def test_pre_reqs_check_at_least_one_level(self):
    #     assignment = gh_assignments.MakeRepository.objects.create(user=self.user)
    #     assert gh_assignments.GithubSignUp in assignment.get_missing_pre_reqs()
    #     gh_assignments.GithubSignUp.objects.create(user=self.user, completed=True)
    #     assert not assignment.get_missing_pre_reqs()
    #
    # def test_pre_reqs_check_work_inherited(self):
    #     # To make a github page we need to make a repo but before that we need to sign up on github!
    #     assignment = gh_assignments.MakeGHPage.objects.create(user=self.user)
    #     assert gh_assignments.MakeRepository in assignment.get_missing_pre_reqs()
    #     # So we sign up, but still not all pre-reqs supplied
    #     gh_assignments.GithubSignUp.objects.create(user=self.user, completed=True)
    #     assert gh_assignments.MakeRepository in assignment.get_missing_pre_reqs()
    #     gh_assignments.MakeRepository.objects.create(user=self.user, completed=True)
    #     assert not assignment.get_missing_pre_reqs()
    #
    # def test_do_pre_req_check_overload_works(self):
    #     assignment = gh_assignments.GithubSignUp.objects.create(user=self.user)
    #     missing_pre_reqs = assignment.get_missing_pre_reqs()
    #     assert missing_pre_reqs == "I need your github username first"
