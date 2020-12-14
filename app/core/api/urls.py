from django.urls import path, include

from .viewset import RegisterUserAPI

app_name = 'core'

register = RegisterUserAPI.as_view({'post': 'create'})


urlpatterns = [
    path('register/', register, name='register'),
]