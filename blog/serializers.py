from rest_framework import serializers
from .models import Topic


class TopicSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = ['id', 'title', 'body', 'date', 'author']

    def get_author(self, obj):
        return obj.author.username
