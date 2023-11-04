from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.views import Response
from posts.models import Post
from contacts.models import Contact
from contactsapi.serializers import ContactSerializer
from .serializers import PostCreateSerializer , PostListSerializer

# Create your views here.

class ListPostView(ListAPIView):
    
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    

class PostViewById(RetrieveAPIView):
    queryset = Post
    serializer_class = PostListSerializer    
    
class CreatePostView(CreateAPIView):
    
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)