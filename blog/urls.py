from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

from .views import TopicListView, TopicUpdateView, TopicDetailView, TopicDeleteView, TopicCreateView, TopicList, TopicDetail

urlpatterns = [
    path('', TopicListView.as_view(), name='topic_list'),
    path('<int:pk>/edit/', TopicUpdateView.as_view(), name='topic_edit'),
    path('<int:pk>/', TopicDetailView.as_view(), name='topic_detail'),
    path('<int:pk>/delete/', TopicDeleteView.as_view(), name='topic_delete'),
    path('new/', TopicCreateView.as_view(), name='topic_new'),
    path('api/', TopicList.as_view(),name = 'api/topic'),
    path('api/<int:pk>',TopicDetail.as_view(),name='api/topic_detail'),


    path('openapi/', get_schema_view(
        title="Topics",
        description="API developers hpoing to use our service"
    ), name='openapi-schema'),

    path('docs/', TemplateView.as_view(
        template_name='documentatiW2on.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]
