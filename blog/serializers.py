from rest_framework import serializers

from comments.serializers import CommentSerializer
from .models import Topic


class TopicSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False, read_only=True, slug_field='username')
    comments = CommentSerializer(many=True, required=False)
    class Meta:
        model = Topic
        fields = ['id', 'title', 'body', 'date', 'author','comments']
