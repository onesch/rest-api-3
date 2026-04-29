from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from app.users.models import User
from app.users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
