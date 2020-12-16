from django.urls import path
from django.views.generic import TemplateView

from rest_framework.schemas import get_schema_view

from api.views import TopicList, TopicDetail, CommentList, CommentDetail


urlpatterns = [
    path('topic/', TopicList.as_view(), name='topic/api'),
    path('topic/<int:pk>', TopicDetail.as_view(), name='topic_detail/api'),
    path('comment/', CommentList.as_view(), name='comment/api'),
    path('comment/<int:pk>', CommentDetail.as_view(), name='comment_detail/api'),

    path('openapi/', get_schema_view(
        title="Topics",
        description="API developers hpoing to use our service"
    ), name='openapi-schema'),

    path('docs/', TemplateView.as_view(
        template_name='documentatiW2on.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),

]

