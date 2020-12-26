from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ParseError

from accounts.models import CustomUser as User, Profile


# User Serializer
class UserRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email',)


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_moder', 'is_staff')


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(many=False, read_only=True, slug_field='username')

    class Meta:
        model = Profile
        fields = ['user', 'image']


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user


# Change password Serializer
class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
