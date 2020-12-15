from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .viewset import RegisterUserAPI, AuthAPIView, PalestranteAPIView

app_name = 'core'

register = RegisterUserAPI.as_view({'post': 'create'})
login = AuthAPIView.as_view({'post': 'login'})
logout = AuthAPIView.as_view({'post': 'logout'})
new_password = AuthAPIView.as_view({'post': 'password_change'})

create = PalestranteAPIView.as_view({'post': 'create'})
all_speakers = PalestranteAPIView.as_view({'get': 'list'})
speaker = PalestranteAPIView.as_view({'get': 'retrieve'})
update = PalestranteAPIView.as_view({'put': 'update'})


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

]
