from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase


class AccountTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path("", include("hello_world.urls")),
    ]

    def test_hello_world(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse("hello-world")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"msg": "Hello world"})
