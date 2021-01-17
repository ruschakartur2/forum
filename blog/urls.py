from django.urls import path

from .views import (TopicListView,
                    TopicUpdateView,
                    TopicDetailView,
                    TopicDeleteView,
                    TopicCreateView,
                    TopicDetailAPI,
                    TopicListAPI
                    )

urlpatterns = [
    path('', TopicListView.as_view(), name='topic_list'),
    path('<int:pk>/edit/', TopicUpdateView.as_view(), name='topic_edit'),
    path('<int:pk>/', TopicDetailView.as_view(), name='topic_detail'),
    path('<int:pk>/delete/', TopicDeleteView.as_view(), name='topic_delete'),
    path('new/', TopicCreateView.as_view(), name='topic_new'),

    path('api/<int:pk>/', TopicDetailAPI.as_view(), name='topic-api-detail'),
    path('api', TopicListAPI.as_view(),name='topic-api-list')

]
