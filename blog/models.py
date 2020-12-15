from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import TextField
from django.urls import reverse
from django.utils import timezone

from pygments.lexers import get_all_lexers


class Topic(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    @property
    def number_of_comments(self):
        return Comment.objects.filter(topic_connected=self).count()

    def get_absolute_url(self):
        return reverse('topic_detail', args=[str(self.id)])


class Comment(models.Model):
    topic_connected = models.ForeignKey(
        Topic, related_name='comments', on_delete=models.CASCADE)

    content = TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='replies')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('topic_list')
