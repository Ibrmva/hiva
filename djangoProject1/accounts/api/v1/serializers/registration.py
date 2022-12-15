from django.utils.translation import gettext

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from accounts.exceptions import InvalidPasswordError
from accounts.models import UserAccount
from accounts.services.password import PasswordService


class RegistrationSerializer(serializers.ModelSerializer):
    passwordConfirm = serializers.CharField(write_only=True, max_length=128)

    class Meta:
        model = UserAccount
        fields = ("email", "password",  "passwordConfirm")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.password_service = PasswordService()

    def validate_email(self, email):
        if UserAccount.objects.filter(email=email).exists():
            raise ValidationError(gettext("Could not create account with this email."))
        return super().validate(email)

    def validate_password(self, new_password):
        try:
            self.password_service.validate_password(new_password)
        except InvalidPasswordError as e:
            raise serializers.ValidationError(e.messages) from e
        return new_password

    def validate(self, attrs):
        if not attrs["passwordConfirm"] == attrs["password"]:
            raise serializers.ValidationError("Passwords should match")
        return attrs

    def save(self, **kwargs):
        self.instance = super().save(**kwargs)
        raw_password = self.validated_data.get("password")
        self.instance.set_password(raw_password)
        self.instance.save()
        return self.instance
