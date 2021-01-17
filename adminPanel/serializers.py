from django.contrib.auth import get_user_model
from rest_framework import serializers
from social_core.tests.models import User

from blog.models import Topic
from comments.serializers import CommentSerializer


class UserAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class TopicAdminSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False, read_only=True, slug_field='username')
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        model = Topic
        fields = '__all__'
