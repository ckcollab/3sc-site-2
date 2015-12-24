from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Applicant(models.Model):
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        help_text="When an Applicant is given a user account, that basically means they've been accepted into 3SC"
    )
    name = models.CharField(max_length=64)
    email = models.EmailField()
    essay = models.TextField()
    github_name = models.CharField(max_length=64, blank=True, null=True)


# Add some helpers to User class so we can get profiles/game profiles easily
# TODO: uuuuuuuuuuuuuuuuuuuugggggggggghhhhhhhhh should probably just rename this to profile and make it proper
User.application = property(lambda u: Applicant.objects.get_or_create(user=u)[0])
