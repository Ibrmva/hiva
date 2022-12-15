from rest_framework import serializers

from accounts.models import UserAccount


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField()

    class Meta:
        model = UserAccount
        fields = ("email",)

