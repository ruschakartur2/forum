from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import generics

from api.serializers import TopicSerializer, CommentSerializer
from blog.models import Topic, Comment


class TopicList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
