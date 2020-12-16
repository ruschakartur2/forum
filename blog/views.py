from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.http import HttpResponseRedirect

from blog.forms import NewCommentForm


from .models import Topic,Comment


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

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = Comment.objects.filter(
            topic_connected=self.get_object()).order_by('-date_posted')
        data['comments'] = comments_connected

        if self.request.user.is_authenticated:
            data['comment_form'] = NewCommentForm(instance=self.request.user)

        return data

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            comment_form = NewCommentForm(request.POST or None)
            if comment_form.is_valid():
                content = request.POST.get('content')
                reply_id = request.POST.get('comment_id')
                comment_qs = None
                if reply_id:
                    comment_qs = Comment.objects.get(id=reply_id)
                comment = Comment.objects.create(topic_connected=self.get_object(), author=self.request.user,
                                                 content=content, reply=comment_qs)
                comment.save()
                return HttpResponseRedirect(self.request.path_info)
        else:
            comment_form = NewCommentForm


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


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    login_url = 'login'

    def get_success_url(self):
        return reverse('topic_detail', kwargs={'pk': self.object.topic_connected.pk})

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author or obj.reply.author != self.request.user:
            raise PermissionDenied
            # return HttpResponseForbidden("403 Forbidden, you don't have access")
        return super().dispatch(request, *args, **kwargs)