from django.contrib.auth import get_user_model
from rest_framework import serializers

from blog.choices import Role
from blog.models import Topic, Membership
from comments.serializers import CommentSerializer


class UserAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class TopicAdminSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False, read_only=True, slug_field='username')
    comments = CommentSerializer(many=True, required=False)
    members = serializers.SlugRelatedField(many=True, read_only=True, slug_field='username')

    class Meta:
        model = Topic
        fields = '__all__'


class MembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Membership
        fields = '__all__'
