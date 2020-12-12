from django.contrib import admin
from django.urls import path, include
from .views import TopicListView, TopicUpdateView, TopicDetailView, TopicDeleteView, TopicCreateView
from . import views
urlpatterns = [
    path('', TopicListView.as_view(), name='topic_list'),
    path('<int:pk>/edit/', TopicUpdateView.as_view(), name='topic_edit'),
    path('<int:pk>/', TopicDetailView.as_view(), name='topic_detail'),
    path('<int:pk>/delete/', TopicDeleteView.as_view(), name='topic_delete'),
    path('new/', TopicCreateView.as_view(), name='topic_new'),
    path('api/',views.topic_list),
    path('api/<int:pk>', views.topic_detail),
]
