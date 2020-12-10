from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import Topic


class TopicListView(ListView):
    model = Topic
    template_name = 'topic/topic_list.html'

class TopicDetailView(DetailView):
    model = Topic
    template_name = 'topic_detail.html'

class TopicUpdateView(UpdateView):
    model = Topic
    fields = ('title','body')
    template_name = 'topic_edit.html'

class TopicDeleteView(DeleteView):
    model = Topic
    template_name = 'topic_delete.html'
    success_url = reverse_lazy('article_list')