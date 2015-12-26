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
    email = models.EmailField(unique=True)
    essay = models.TextField()
    github_name = models.CharField(max_length=64, blank=True, null=True)

    def save(self, *args, **kwargs):
        # check if created before saving
        created = not self.pk
        # do our save first, to ensure we have email field and all that jazz
        super().save(*args, **kwargs)
        if created:
            # creating new Applicant so also make user and shoot out activation/registration
            self.user, _ = User.objects.get_or_create(email=self.email)
            self.save()


# Add some helpers to User class so we can get applicant info easily
User.application = property(lambda u: Applicant.objects.get_or_create(user=u)[0])
