from django.contrib import admin
from django.urls import path, include
from .views import TopicListView, TopicUpdateView, TopicDetailView, TopicDeleteView

urlpatterns = [
    path('',TopicListView.as_view(), name='topic_list'),
    path('<int:pk>/edit',TopicUpdateView.as_view(),name='topic_edit'),
    path('<int:pk>/',TopicDetailView.as_view(),name='topic_detail'),
    path('<int:pk>/delete',TopicDeleteView.as_view(),name='topic_delete')
]
