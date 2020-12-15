from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .viewset import (
    RegisterUserAPI,
    AuthAPIView,
    PalestranteAPIView,
    PalestraAPIView,
)

app_name = 'core'

"""Métodos relacionados a usuários"""
register = RegisterUserAPI.as_view({'post': 'create'})
login = AuthAPIView.as_view({'post': 'login'})
logout = AuthAPIView.as_view({'post': 'logout'})
new_password = AuthAPIView.as_view({'post': 'password_change'})

"""Palestrantes/Speakers"""
create = PalestranteAPIView.as_view({'post': 'create'})
all_speakers = PalestranteAPIView.as_view({'get': 'list'})
speaker = PalestranteAPIView.as_view({'get': 'retrieve'})
update = PalestranteAPIView.as_view({'put': 'update'})
delete = PalestranteAPIView.as_view({'delete': 'destroy'})


"""Palestras/Lecture"""
create_lecture = PalestraAPIView.as_view({'post': 'create'})
all_lectures = PalestraAPIView.as_view({'get': 'list'})
lectures_detail = PalestraAPIView.as_view({'get': 'retrieve'})
update_lecture = PalestraAPIView.as_view({'put': 'update'})
delete_lecture = PalestraAPIView.as_view({'delete': 'destroy'})

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('change-password/', new_password, name='change-password'),
    path('get-token/', obtain_jwt_token),
    path('refresh-token/', refresh_jwt_token),

    path('speakers/new/', create, name='create-speaker'),
    path('speakers/', all_speakers, name='all_speakers'),
    path('speakers/<int:pk>/', speaker, name='speaker'),
    path('speakers/<int:pk>/update/', update, name='update'),
    path('speakers/<int:pk>/delete/', delete, name='delete'),


    path('lectures/new/', create_lecture, name='create_lecture'),
    path('lectures/', all_lectures, name='all_lectures'),
    path('lectures/<int:pk>/', lectures_detail, name='lectures_detail'),
    path('lectures/<int:pk>/update/', update_lecture, name='update_lecture'),
    path('lectures/<int:pk>/delete/', delete_lecture, name='delete_lecture'),



]
