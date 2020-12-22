from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentCreateSerializer, CommentListSerializer


class CommentCreateView(generics.CreateAPIView):
    model = Comment
    serializer_class = CommentCreateSerializer


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    model = Comment
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer

    permission_classes = [IsOwnerOrReadOnly]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class CommentListView(generics.ListAPIView):
    model = Comment
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['topic', 'author', 'content']
