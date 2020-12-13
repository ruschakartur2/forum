import generics as generics
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from rest_framework import generics

from .models import Topic, Comment

from .serializers import TopicSerializer


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
    model = Topic
    template_name = 'topic/topic_list.html'
    login_url = 'login'


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


# Write API
class TopicList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
