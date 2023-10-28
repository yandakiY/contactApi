from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from posts.models import Post
from .serializers import PostCreateSerializer , PostListSerializer

# Create your views here.

class ListPostView(ListAPIView):
    
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    

class CreatePostView(CreateAPIView):
    
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
