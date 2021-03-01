from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django_filters.rest_framework import DjangoFilterBackend
from dry_rest_permissions.generics import DRYPermissions
from rest_framework import generics, viewsets, renderers
from rest_framework.decorators import action, renderer_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .choices import Role
from .models import Topic, Membership
from .serializers import TopicSerializer
from .permissions import IsBanned, IsClosed, IsModerToTopic


class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    template_name = 'topic/topic_new.html'
    fields = ('title', 'body')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('topic_detail', kwargs={'pk': self.object.pk})


class TopicListView(LoginRequiredMixin, ListView):
    template_name = 'topic/topic_list.html'
    login_url = 'login'
    model = Topic


class TopicDetailView(LoginRequiredMixin, DetailView):
    model = Topic
    template_name = 'topic/topic_detail.html'
    login_url = 'login'


class TopicUpdateView(LoginRequiredMixin, UpdateView):
    model = Topic
    fields = ('title', 'body')
    template_name = 'topic/topic_edit.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
            # return HttpResponseForbidden("403 Forbidden, you don't have access")
        return super().dispatch(request, *args, **kwargs)


class TopicDeleteView(LoginRequiredMixin, DeleteView):
    model = Topic
    template_name = 'topic/topic_delete.html'
    success_url = reverse_lazy('topic_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
            # return HttpResponseForbidden("403 Forbidden, you don't have access")
        return super().dispatch(request, *args, **kwargs)


class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
    permission_classes_by_action = {'create': [IsAuthenticated, IsBanned],
                                    'list': [AllowAny, IsBanned],
                                    'update': [IsModerToTopic, IsBanned],
                                    'partial_update': [IsModerToTopic],
                                    'retrieve': [AllowAny, IsBanned, IsModerToTopic], }

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]
