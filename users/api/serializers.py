from ..models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

    def is_valid(self, *args, **kwargs):
        # is called by the create to insure that the data is valid
        return super().is_valid(*args, **kwargs)

    def save(self, *args, **kwargs):
        # create the new database entry and stores it
        return super().save(*args, **kwargs)