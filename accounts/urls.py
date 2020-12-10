from django.conf import settings
from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path, include

from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('',include('social_django.urls',namespace='social')),
    path('logout/',logout,{'next_page':settings.LOGOUT_REDIRECT_URL},name='logout'),
]
