from rest_framework import serializers

from comments.serializers import CommentSerializer
from .choices import Role
from .models import Topic, Membership


class TopicSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False, read_only=True, slug_field='username')
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        model = Topic
        fields = ['id', 'title', 'body', 'date', 'author', 'comments']

    def create(self, validated_data):
        topic = Topic.objects.create(**validated_data)
        Membership.objects.create(user=self.context['request'].user,
                                  topic=topic,
                                  role=Role.MODER)

        return topic
