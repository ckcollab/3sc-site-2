from django.contrib.auth import get_user_model
from django.test import TestCase
from model_mommy import mommy

from ..models import Applicant


User = get_user_model()


class ApplicantModelTests(TestCase):
    def test_saving_applicant_creates_user(self):
        applicant = mommy.make(Applicant)
        assert applicant.user
        assert applicant.user.email == applicant.email

    def creating_user_creates_applicant(self):
        user = mommy.make(User)
        assert user.applicant
