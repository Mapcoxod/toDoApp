from django.contrib.auth.models import User
from rest_framework import generics, permissions

from core.serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.none()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
