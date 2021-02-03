from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.exceptions import APIException

from blog.models import Moder, Topic


class BannedForbidden(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_code = "You are banned"


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user


class IsClosed(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.is_closed == False


class IsBanned(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_banned == False
