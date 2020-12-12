from rest_framework import serializers
from .models import Topic

class TopicSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author', read_only=True)
    class Meta:
        model = Topic
        fields = ['id','title','body','date','author_name']