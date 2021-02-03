from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from blog.models import Topic
from moderPanel.permissions import IsModer, IsModerTopic
from moderPanel.serializers import UserModerSerializer, TopicModerSerializer


class UserModerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserModerSerializer
    model = get_user_model()
    queryset = get_user_model().objects.all()
    permission_classes = (IsModer,)


class UserModerListView(generics.ListAPIView):
    serializer_class = UserModerSerializer
    model = get_user_model()
    queryset = get_user_model().objects.all()
    permission_classes = (IsModer,)


class TopicModerListView(generics.ListCreateAPIView):
    serializer_class = TopicModerSerializer
    model = Topic
    queryset = Topic.objects.all()
    permission_classes = (IsModer,)



class TopicModerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TopicModerSerializer
    model = Topic
    queryset = Topic.objects.all()
    permission_classes = (IsModer, IsModerTopic)
