from django.urls import path
from .viewset import RegisterUserAPI, AuthAPIView

app_name = 'core'

register = RegisterUserAPI.as_view({'post': 'create'})
login = AuthAPIView.as_view({'post': 'login'})
logout = AuthAPIView.as_view({'post': 'logout'})
new_password = AuthAPIView.as_view({'post': 'password_change'})

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('change-password/', new_password, name='change-password'),

]
