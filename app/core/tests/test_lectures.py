from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse
from rest_framework.test import APIClient

create_url = api_reverse('api-core:create-speaker')
create_lecture_url = api_reverse('api-core:create_lecture')


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
        if self.assertEqual(res.status_code, status.HTTP_201_CREATED):

            """Test creating lecture success"""
            payload = {
                "nome": "Tom Jobim",
                'titulo': 'A nossa Bossa Nova',
                'descricao': 'O grande compositor Tom Jobim fala do impacto da bossa nova na culura americana.',
                'data': ' 2020-12-16 18:19:34',
                'hora': "00:08:30",

            }
            res = self.client.post(create_lecture_url, payload)
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)
