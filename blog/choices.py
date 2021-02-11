from django.db import models


class Role(models.IntegerChoices):
    MEMBER = 1
    MODER = 2
    ADMIN = 3
