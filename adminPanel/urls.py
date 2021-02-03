from django.urls import path, include

from adminPanel.views import UserListView, UserDetailView, TopicAdminListView, TopicAdminDetailView, ModerListView, \
    ModerDetailView

urlpatterns = [
    path('users', UserListView.as_view(), name='users'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('topics',TopicAdminListView.as_view(), name='topics'),
    path('topics/<int:pk>/', TopicAdminDetailView.as_view(), name='topic-detail'),
    path('moders/', ModerListView.as_view(), name='moders'),
    path('moders/<int:pk>/', ModerDetailView.as_view(), name='moder-detail')
]