import random

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase
from faker import Factory
from loremipsum import generate_paragraph


User = get_user_model()


class TestPermissions(TestCase):

    def test_check_admin_priviledges_are_required_for_applicants_list(self):
        assert "rest_framework.permissions.IsAdminUser" in settings.REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES']
        resp = self.client.get(reverse("api:applicants-list"))
        assert resp.status_code == 403

        User.objects.create_superuser(username="admin", password="admin", email="admin@admin.com")
        self.client.login(username="admin", password="admin")
        resp = self.client.get(reverse("api:applicants-list"))
        assert resp.status_code == 200

    def test_non_logged_in_can_post_applications(self):
        fake = Factory.create()
        resp = self.client.post(reverse("api:applicants-list"), {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "essay": "\n\n".join([generate_paragraph()[2] for _ in range(random.randint(2, 5))])
        })
        assert resp.status_code == 201
