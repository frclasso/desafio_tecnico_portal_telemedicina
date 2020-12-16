from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse


class ModelTests(TestCase):
    """Classe de teste para os models/tabelas"""

    def setUp(self):
        email = 'testuser@email.com'
        password = 'testando123456789'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        user.save()

    def test_created_user(self):
        qs = get_user_model().objects.filter(email='testuser@email.com')
        self.assertEquals(qs.count(), 1)

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email successful"""
        email = 'anotheruser@email.com'
        password = 'testando123456789'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'teste1234567')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'teste@email.com',
            'test1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_register_user_api_fail(self):
        url = api_reverse('api-core:register')
        data = {
            'name': 'NewUser',
            'email': 'newuser@gmail.com',
            'password': 'senha12345',
        }
        response = self.client.post(url, data, follow='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_api_success(self):
        url = api_reverse('api-core:register')
        data = {
            'name': 'NewUser',
            'email': 'newuser@gmail.com',
            'password': 'senha12345',
            'password2': 'senha12345',
        }
        response = self.client.post(url, data, follow='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
