from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet

from forum import settings
router = DefaultRouter()
router.register(r'',CommentViewSet, basename='comments')


urlpatterns = [

    path('api/',include(router.urls), name='comments'),

]