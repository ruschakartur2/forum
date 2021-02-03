from django.contrib.auth import get_user_model
from rest_framework import serializers

from blog.models import Topic
from comments.serializers import CommentSerializer


class UserModerSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'is_banned', 'is_mutted']
        read_only_fields = ['username', 'name', 'email']


class TopicModerSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False, read_only=True, slug_field='username')
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        model = Topic
        fields = ['id', 'title', 'body', 'date', 'author', 'comments', 'is_closed']
