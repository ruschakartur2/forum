from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from knox.models import AuthToken

from blog.permissions import IsOwnerOrReadOnly, IsModer
from .models import Profile
from .serializers import RegisterSerializer, ChangePasswordSerializer, ProfileSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer

from django.contrib.auth.models import User

from .forms import CustomUserCreationForm, ProfileUpdateForm, UserUpdateForm
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import generics

from .serializers import UserSerializer, UserDetailSerializer, UserRegSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'registration/profile.html', context)


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserRegSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileListView(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    model = Profile
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    model = Profile
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Profile.objects.all()


class UserListView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    model = get_user_model()
    permission_classes = (IsAdminUser,IsModer,)
    queryset = get_user_model().objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    model = get_user_model()
    permission_classes = (IsAdminUser,IsModer,)
    queryset = get_user_model().objects.all()
