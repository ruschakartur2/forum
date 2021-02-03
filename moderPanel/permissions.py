from rest_framework import permissions

from blog.models import Topic, Moder


class IsModer(permissions.BasePermission):
    def has_permission(self, request, view):
        moder = Moder.objects.get(user=request.user.id)
        return moder


class IsModerTopic(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        modered_topics = Moder.objects.get(topics=Topic.objects.get(id=obj.id))
        return (modered_topics.user == request.user) or request.user.is_staff
