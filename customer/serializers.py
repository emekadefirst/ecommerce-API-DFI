import re
from .models import Customer
from rest_framework import serializers
from rest_framework.validators import ValidationError


def check_password(user_password):
    password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    match = re.match(password_pattern, string=user_password)
    return bool(match)


def validate_password(password):
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")
    if check_password(password) != True:
        raise ValidationError(
            "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character."
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "username",
            "email",
            "phone_number" "password",
            "created_at",
            "email",
        ]

    extra_kwargs = {
        "password": {"write_only": True},
        "created_at": {"read_only": True},
    }

    def create(self, validated_data):
        password = validated_data["password"]
        if not check_password(password):
            raise ValidationError("Poor Password")
        user = Customer.objects.create(**validated_data)
        validate_password(user.password)
        return user
