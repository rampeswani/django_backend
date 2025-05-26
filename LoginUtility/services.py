# services.py

from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.exceptions import ValidationError


def register_user(data):
    serializer = RegisterSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return {"message": "User created"}
    raise ValidationError(serializer.errors)


def login_user(data):
    serializer = LoginSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        return serializer.validated_data
    raise ValidationError(serializer.errors)


def get_user_info(user):
    return {
        'id': user.id,
        'username': user.username,
        'name': user.first_name,
        'role': user.role  # Ensure this exists on your custom user model
    }
