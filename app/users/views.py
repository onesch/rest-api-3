from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

from app.users.models import User
from app.users.serializers import UserSerializer, PasswordSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    @action(detail=True, methods=["post"])
    def change_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(
            data=request.data,
            context={"user": user}
        )

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "password changed"})

        return Response(serializer.errors, status=400)
