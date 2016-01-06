from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class UserModelEmailBackend(ModelBackend):

    def authenticate(self, email="", password="", **kwargs):
        try:
            user = get_user_model().objects.get(email__iexact=email)
            if user.check_password(password):
                return user
            else:
                return None
        except get_user_model().DoesNotExist:
            # No user was found, return None - triggers default login failed
            return None
