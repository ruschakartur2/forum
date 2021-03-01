from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from blog.permissions import IsBanned
from .models import Comment
from .permissions import IsOwnerOrReadOnly
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    permission_classes_by_action = {'create': [IsAuthenticated, IsBanned],
                                    'list': [AllowAny, IsBanned],
                                    'update': [IsOwnerOrReadOnly, IsBanned],
                                    'partial_update': [IsOwnerOrReadOnly],
                                    'retrieve': [AllowAny, IsBanned, IsOwnerOrReadOnly],
                                    'destroy': [IsOwnerOrReadOnly],}

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]
