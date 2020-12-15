from django.utils import timezone
from rest_framework import serializers
from .models import Topic, Comment


class TopicSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = ['id', 'title', 'body', 'date', 'author']

    def get_author(self, obj):
        return obj.author.username


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    topic_connected = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'author', 'date_posted', 'topic_connected', 'content']

    def get_author(self, obj):
        return obj.author.username

    def get_topic_connected(self, obj):
        return obj.topic_connected.title
