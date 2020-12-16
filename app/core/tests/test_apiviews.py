from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse
from rest_framework.test import APIClient


class APITest(TestCase):

    def setUp(self):
        email = 'testuser@email.com'
        password = 'testando123456789'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        user.save()

    def test_login_user_api_fail_user_not_found(self):
        url = api_reverse('api-core:login')
        data = {
            'email': 'joedoe@email.com',
            'password': 'joedoepassword'

        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_user_api(self):
        url = api_reverse('api-core:login')
        data = {
            'email': 'testuser@email.com',
            'password': 'testando123456789'

        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_speaker(self):
        """Test creating speaker, user unauthorized"""
        client = APIClient()
        create_url = api_reverse('api-core:create-speaker')

        payload = {
            "nome": "Tom Jobim",
            "bio": "Antônio Carlos Brasileiro de Almeida Jobim ,"
                   " mais conhecido pelo seu nome artístico Tom Jobim, "
                   "foi um compositor, maestro, pianista, cantor, "
                   "arranjador e violonista brasileiro. "
                   "É considerado o maior expoente de todos os tempos da música popular brasileira pela revista "
                   "Rolling Stones e um dos criadores e das principais forças do movimento da bossa nova. "
        }
        res = client.post(create_url, payload)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_speaker_user_logged_in(self):
        """Test creating speaker, user authorized"""
        url = api_reverse('api-core:login')
        data = {
            'email': 'testuser@email.com',
            'password': 'testando123456789'

        }
        response = self.client.post(url, data, format='json')
        if self.assertEqual(response.status_code, status.HTTP_200_OK):

            client = APIClient()
            create_url = api_reverse('api-core:create-speaker')

            payload = {
                "nome": "Tom Jobim",
                "bio": "Antônio Carlos Brasileiro de Almeida Jobim ,"
                       " mais conhecido pelo seu nome artístico Tom Jobim, "
                       "foi um compositor, maestro, pianista, cantor, "
                       "arranjador e violonista brasileiro. "
                       "É considerado o maior expoente de todos os tempos da música popular brasileira pela revista "
                       "Rolling Stones e um dos criadores e das principais forças do movimento da bossa nova. "
            }
            res = client.post(create_url, payload)
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)
