from rest_framework import generics
from .serializers import PostSerializer, UserSerializer, LickSerializer
from .models import Post, Lick
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
# Create your views here


class CreatePostView(generics.ListCreateAPIView):
    """this class defines the create behavior of our restAPI"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Post."""
        serializer.save(owner=self.request.user)


class CreateUserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class CreateLickView(generics.ListCreateAPIView):
    queryset = Lick.objects.all()
    serializer_class = LickSerializer


class UserPostView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Post.objects.filter(owner=user)
        return queryset.order_by('-created')


class UserProfileView(generics.ListAPIView):
    serializer_class = UserSerializer

    def display_user_information(self):
        user = self.request.user
        queryset = User.objects.filter(username=user)
        return queryset


