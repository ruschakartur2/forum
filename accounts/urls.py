from django.conf import settings

from knox import views as knox_views

from django.contrib.auth import logout
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from .views import profile, RegisterAPI, LoginAPI, ChangePasswordView, ProfileViewSet
from .views import SignUpView

router = DefaultRouter()
router.register('', ProfileViewSet, basename='profiles')

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('profile/', profile, name='profile'),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/profiles', include(router.urls)),
    path('auth/', include('rest_framework_social_oauth2.urls')),

]
