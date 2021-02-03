from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone

from accounts.models import CustomUser


class Topic(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    is_closed = models.BooleanField('closed topic', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('topic_detail', args=[str(self.id)])

    @property
    def owner(self):
        return self.author


class Moder(models.Model):
    user = models.ForeignKey(get_user_model(),unique=True, on_delete=models.CASCADE, related_name='users')
    topics = models.ManyToManyField(Topic, related_name='topics')

    def __str__(self):
        return self.user.username
