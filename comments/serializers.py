from rest_framework import serializers

from comments.models import Comment


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False, read_only=True, slug_field='username')

    class Meta:
        model = Comment
        fields = ('author', 'content', 'date_posted')




class CommentListSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False, read_only=True, slug_field='username')
    topic = serializers.SlugRelatedField(many=False, read_only=True, slug_field='title')

    class Meta:
        model = Comment
        fields = '__all__'
