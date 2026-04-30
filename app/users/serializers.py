from rest_framework import serializers

from app.users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class PasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def save(self, **kwargs):
        user = self.context["user"]

        if not user.check_password(self.validated_data["old_password"]):
            raise serializers.ValidationError("Wrong password")

        user.set_password(self.validated_data["new_password"])
        user.save()

        return user
