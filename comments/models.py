from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from blog.models import Topic


class Comment(models.Model):
    topic = models.ForeignKey(
        Topic, related_name='comments',
        on_delete=models.CASCADE
    )

    content = models.CharField(max_length=1254)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='replies')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content

    @property
    def owner(self):
        return self.author