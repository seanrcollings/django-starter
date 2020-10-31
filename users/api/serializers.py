from ..models import User
from rest_framework import serializers


class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]
