from django.conf import settings

from knox import views as knox_views

from django.contrib.auth import logout
from django.urls import path, include
from .views import profile, RegisterAPI, LoginAPI, ChangePasswordView, ProfileListView, ProfileDetailView

from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('profile/',profile, name='profile'),

    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/profiles', ProfileListView.as_view(),name='profiles'),
    path('api/profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),

    path('auth/', include('rest_framework_social_oauth2.urls')),

]


