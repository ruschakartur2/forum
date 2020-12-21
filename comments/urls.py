from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import CommentCreateView, CommentListView, CommentDetailView

from forum import settings

urlpatterns = [
    path('api/create/', CommentCreateView.as_view(), name='comment-create'),
    path('api/', CommentListView.as_view(),name='comments'),
    path('api/<int:pk>/', CommentDetailView.as_view(), name='comment-detail')

]