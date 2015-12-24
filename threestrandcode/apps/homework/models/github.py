import requests

from .assignment import Assignment


class GithubSignUp(Assignment):

    def get_missing_pre_reqs(self):
        return "I need your github username first"

    def do_completed_check(self):
        if self.user.application.github_name:
            resp = requests.get('https://github.com/%s' % self.user.application.github_name)
            self.completed = resp.status_code == 200
        else:
            self.completed = False
        self.save()
        return self.completed


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
