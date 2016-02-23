from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models, IntegrityError
from django.db.models.signals import post_save


class Applicant(models.Model):
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        help_text="When an Applicant is given a user account, that basically means they've been accepted into 3SC"
    )
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
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
            User = get_user_model()
            self.user, _ = User.objects.get_or_create(email=self.email)
            self.save()


# Connect to User model just in case for some reason we make a User without
# first submitting an application
def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        try:
            Applicant.objects.get_or_create(user=user, email=user.email)
        except IntegrityError:
            # Sometimes email may already exist and although get_or_create should succeed, it
            # fails here?
            pass


post_save.connect(create_profile, sender=settings.AUTH_USER_MODEL)
