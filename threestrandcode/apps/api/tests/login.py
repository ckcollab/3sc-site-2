import json

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase


class TestLogin(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test", email="test@test.com")

    def test_login_with_username_returns_200(self):
        resp = self.client.post(reverse("rest_login"), {"username": "test", "password": "test"})
        assert resp.status_code == 200

    def test_login_with_username_returns_400_when_wrong_password(self):
        resp = self.client.post(reverse("rest_login"), {"username": "test", "password": "wrong"})
        assert resp.status_code == 400
        data = json.loads(resp.content.decode('utf8'))
        assert "Unable to log in with provided credentials." in data["non_field_errors"]

    def test_login_with_email_returns_200(self):
        resp = self.client.post(reverse("rest_login"), {"email": "test@test.com", "password": "test"})
        print(resp.content)
        assert resp.status_code == 200

    def test_login_with_email_returns_400_when_wrong_password(self):
        resp = self.client.post(reverse("rest_login"), {"email": "test@test.com", "password": "wrong"})
        assert resp.status_code == 400
        data = json.loads(resp.content.decode('utf8'))
        assert "Unable to log in with provided credentials." in data["non_field_errors"]
