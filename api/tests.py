from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status

User = get_user_model()


class UserRegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {
            "username": "testcase",
            "password": "testing123",
            "first_name": "Test",
            "last_name": "Case",
            "email": "test@case.com"
        }
        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, "testcase")


class UserLoginTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test", password="testpass")
        self.token = Token.objects.create(user=self.user)

    def test_authentication(self):
        response = self.client.post("/api/login/", {"username": "test", "password": "testpass"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["token"], self.token.key)

class SendMessageTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)


    def test_get_messages(self):
        response = self.client.get("/api/get_messages/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
