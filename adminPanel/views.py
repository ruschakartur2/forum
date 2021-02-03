from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from adminPanel.serializers import UserAdminSerializer, TopicAdminSerializer, ModerSerializer
from blog.models import Topic, Moder


class UserListView(generics.ListCreateAPIView):
    serializer_class = UserAdminSerializer
    model = get_user_model()
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserAdminSerializer
    model = get_user_model()
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()


class TopicAdminListView(generics.ListCreateAPIView):
    serializer_class = TopicAdminSerializer
    model = Topic
    permission_classes = (IsAdminUser,)
    queryset = Topic.objects.all()


class TopicAdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TopicAdminSerializer
    model = Topic
    permission_classes = (IsAdminUser,)
    queryset = Topic.objects.all()


class ModerListView(generics.ListCreateAPIView):
    serializer_class = ModerSerializer
    model = Moder
    permission_classes = (IsAdminUser,)
    queryset = Moder.objects.all()




class ModerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ModerSerializer
    model = Moder
    permission_classes = (IsAdminUser,)
    queryset = Moder.objects.all()
