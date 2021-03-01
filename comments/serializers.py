from datetime import datetime

from rest_framework import serializers

from blog.models import Topic
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False, read_only=True, slug_field='username')
    topic = serializers.SlugRelatedField(many=False, queryset=Topic.objects.all(), slug_field='title')

    class Meta:
        model = Comment
        fields = ['id','topic','author','content','reply']

