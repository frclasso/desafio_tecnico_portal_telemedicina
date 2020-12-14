from rest_framework import viewsets, status
from django.contrib.auth import get_user_model
from rest_framework.response import Response

from .serializers import UserRegisterSerializer
from .permissions import AnonPermissionOnly

User = get_user_model()


class RegisterUserAPI(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AnonPermissionOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )
