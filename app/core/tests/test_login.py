from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse


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

    def test_login_user_api_success(self):
        url = api_reverse('api-core:login')
        data = {
            'email': 'testuser@email.com',
            'password': 'testando123456789'

        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)




