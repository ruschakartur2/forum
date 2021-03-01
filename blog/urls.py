from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from blog.views import TopicViewSet

from .views import (TopicListView,
                    TopicUpdateView,
                    TopicDetailView,
                    TopicDeleteView,
                    TopicCreateView,
                    )
router = DefaultRouter()
router.register(r'',TopicViewSet, basename='topics')

urlpatterns = [
    path('', TopicListView.as_view(), name='topic_list'),
    path('<int:pk>/edit/', TopicUpdateView.as_view(), name='topic_edit'),
    path('<int:pk>/', TopicDetailView.as_view(), name='topic_detail'),
    path('<int:pk>/delete/', TopicDeleteView.as_view(), name='topic_delete'),
    path('new/', TopicCreateView.as_view(), name='topic_new'),
    path('api/', include(router.urls))

]
