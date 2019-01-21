from rest_framework import serializers
from .models import Post, Lick

from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into JSON format"""
    # Glad to see you know about docstrings! We try to put them on every class, method, or function
    # as a way to explicitly indicate intent.  Sometimes we also add marked-up info re: the method
    # signature, but that is more optional.
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        # Meta classes really don't need docstrings though :p
        """Meta class to keep map serializer's fields with the model fields."""
        model = Post
        fields = ('id', 'owner', 'picture', 'text', 'created_at', 'count_licks')


class LickSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lick
        fields = ('id', 'post', 'licked_by')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'password', 'email')
