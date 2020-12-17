from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse
from rest_framework.test import APIClient


create_url = api_reverse('api-core:create-speaker')


class PrivateUserApiTests(TestCase):
    """Test API requests that require authentication"""

    def setUp(self):
        email = 'testuser@email.com'
        password = 'testando123456789'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        user.save()

        self.client = APIClient()
        self.client.force_authenticate(user=user)

    def test_create_speaker_user_success(self):
        payload = {
            "nome": "Tom Jobim",
            "bio": "Antônio Carlos Brasileiro de Almeida Jobim ,"
                   " mais conhecido pelo seu nome artístico Tom Jobim, "
                   "foi um compositor, maestro, pianista, cantor, "
                   "arranjador e violonista brasileiro. "
                   "É considerado o maior expoente de todos os tempos da música popular brasileira pela revista "
                   "Rolling Stones e um dos criadores e das principais forças do movimento da bossa nova. "
        }
        res = self.client.post(create_url, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)


class PublicUserApiTests(TestCase):
    """Test the user API (public)"""

    def setUp(self) -> None:
        self.client = APIClient()

    def test_create_speaker_fail(self):
        """Test creating speaker, user unauthorized"""

        payload = {
            "nome": "Tom Jobim",
            "bio": "Antônio Carlos Brasileiro de Almeida Jobim ,"
                   " mais conhecido pelo seu nome artístico Tom Jobim, "
                   "foi um compositor, maestro, pianista, cantor, "
                   "arranjador e violonista brasileiro. "
                   "É considerado o maior expoente de todos os tempos da música popular brasileira pela revista "
                   "Rolling Stones e um dos criadores e das principais forças do movimento da bossa nova. "
        }
        res = self.client.post(create_url, payload)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
