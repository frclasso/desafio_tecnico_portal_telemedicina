from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Classe de teste para os models/tabelas"""

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email successful"""
        email = 'fabio@email.com'
        password = 'testando123456789'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))