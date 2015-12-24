from .assignment import Assignment


class GithubSignUp(Assignment):

    def get_missing_pre_reqs(self):
        return "I need your github username first"

    def do_completed_check(self):
        super()


class MakeRepository(Assignment):

    pre_reqs = (GithubSignUp,)

    def do_completed_check(self):
        # check if name exists
        super()


class MakeGHPage(Assignment):

    pre_reqs = (MakeRepository,)

    def do_completed_check(self):
        # check if name exists
        super()
