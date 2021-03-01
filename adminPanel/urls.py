from django.urls import path, include

from rest_framework.routers import DefaultRouter

from adminPanel.views import TopicAdminViewSet, UserViewSet, MembershipAdminViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'topics', TopicAdminViewSet, basename='topics')
router.register(r'memberships',MembershipAdminViewSet,basename='memberships')
urlpatterns = [
    path('', include(router.urls)),
]
