from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import CommentCreateView

from forum import settings

urlpatterns = [
    path('api/create/', CommentCreateView.as_view(), name='comment-create'),

]