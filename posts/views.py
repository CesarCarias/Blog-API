from django.shortcuts import render
from rest_framework import generics
from posts.serializers import PostSerializer
from posts.models import Post
from posts.permissions import IsAuthorOrReadOnly

# Create your views here.

class postList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class postDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)

