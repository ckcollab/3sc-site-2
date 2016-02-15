import os

from django.shortcuts import HttpResponseRedirect
from social.exceptions import AuthException


def ensure_logged_in(backend, user, response, *args, **kwargs):
    if not user:
        raise AuthException("Registration is required to connect to social sites.")


def save_github_name(backend, user, response, *args, **kwargs):
    if backend.name == 'github':
        application = user.application
        application.github_name = response["login"]
        application.save()
        redirect_url = os.environ.get("OAUTH_COMPLETE_REDIRECT_URL", "/")
        return HttpResponseRedirect(redirect_url)
