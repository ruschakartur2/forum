from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.exceptions import APIException

from blog.choices import Role
from blog.models import Topic, Membership


class BannedForbidden(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_code = "You are banned"


class IsClosed(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.is_closed == False


class IsBanned(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_banned == False


class IsModerToTopic(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        q = Membership.objects.filter(user=request.user, topic=obj, role=Role.MODER).exists()
        return q
