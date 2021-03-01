from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from adminPanel.serializers import UserAdminSerializer, TopicAdminSerializer, MembershipSerializer
from blog.models import Topic, Membership


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    model = get_user_model()
    serializer_class = UserAdminSerializer
    permission_classes = (IsAdminUser,)


class TopicAdminViewSet(viewsets.ModelViewSet):
    serializer_class = TopicAdminSerializer
    permission_classes = (IsAdminUser,)
    queryset = Topic.objects.all()


class MembershipAdminViewSet(viewsets.ModelViewSet):
    serializer_class = MembershipSerializer
    permission_classes = (IsAdminUser,)
    queryset = Membership.objects.all()