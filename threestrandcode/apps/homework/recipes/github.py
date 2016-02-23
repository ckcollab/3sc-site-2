from .base_recipe import BaseRecipe


class SignUp(BaseRecipe):
    description = "Sign up on Github"

    @classmethod
    def do_completed_check(cls, user):
        return user.applicant.github_name is not None


class MakeRepository(BaseRecipe):
    description = "Make repository on Github"
    pre_reqs = (SignUp,)


class MakeGHPage(BaseRecipe):
    description = "Make GH page on GitHub"
    pre_reqs = (MakeRepository,)
