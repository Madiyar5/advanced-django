from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.tokens import default_token_generator
from .utils import send_verification_email

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email', 'role']
        #extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data['role']
        )
        token = default_token_generator.make_token(user)
        user.is_active = False
        send_verification_email(user)

        return user

class PasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, min_length=2)

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']