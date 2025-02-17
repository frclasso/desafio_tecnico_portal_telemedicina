from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have email')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        """Create and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model tha supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Palestrante(models.Model):
    nome = models.CharField(max_length=255)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Palestra(models.Model):

    nome = models.ForeignKey(Palestrante, on_delete=models.CASCADE,
                             default=None, related_name='palestras')
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, null=True, blank=True)
    data = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.nome}  {self.titulo}"
