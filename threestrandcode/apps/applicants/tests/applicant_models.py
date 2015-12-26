from django.test import TestCase
from model_mommy import mommy

from ..models import Applicant


class ApplicantModelTests(TestCase):
    def test_saving_applicant_creates_user(self):
        applicant = mommy.make(Applicant)
        assert applicant.user
        assert applicant.user.email == applicant.email
