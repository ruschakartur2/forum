from blog.views import TopicViewSet
from rest_framework.routers import DefaultRouter

topic_list = TopicViewSet.as_view({'get': 'list'})
topic_detail = TopicViewSet.as_view({'get': 'retrieve'})
