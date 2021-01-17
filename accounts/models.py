from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    is_moder = models.BooleanField('moderator status', default=False)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


