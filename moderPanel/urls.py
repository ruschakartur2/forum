from django.urls import path

from moderPanel.views import UserModerDetailView, UserModerListView, TopicModerDetailView, TopicModerListView

urlpatterns = [
    path('users/<int:pk>/',UserModerDetailView.as_view(), name='moder-users-detail'),
    path('users/',UserModerListView.as_view(), name='moder-users-list'),
    path('topics/<int:pk>/', TopicModerDetailView.as_view(),name='moder-topics-detail'),
    path('topics/', TopicModerListView.as_view(), name='moder-topics-list'),
]