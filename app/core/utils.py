import datetime
from django.utils import timezone
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
from rest_framework import serializers

expire_delta = api_settings.JWT_REFRESH_EXPIRATION_DELTA


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': user.username,
        'expires': timezone.now() + expire_delta - datetime.timedelta(seconds=200)
    }


def get_and_authenticate_user(email, password):
    user = authenticate(username=email, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid username/password. Please try again!")
    return user