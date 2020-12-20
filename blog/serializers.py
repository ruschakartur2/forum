from rest_framework import serializers

from .models import Topic


class TopicSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False, read_only=True, slug_field='username')

    class Meta:
        model = Topic
        fields = ['id', 'title', 'body', 'date', 'author']
