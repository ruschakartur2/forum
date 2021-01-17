from django.urls import path, include

from adminPanel.views import UserListView, UserDetailView, TopicAdminListView, TopicAdminDetailView

urlpatterns = [
    path('users', UserListView.as_view(), name='users'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('topics',TopicAdminListView.as_view(), name='topics'),
    path('topics/<int:pk>/', TopicAdminDetailView.as_view(), name='topic-detail')
]