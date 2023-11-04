from rest_framework import serializers
from rest_framework.fields import ListField
from posts.models import Post
# from .serializers import 
from contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

class PostListSerializer(serializers.ModelSerializer):
    
    author = ContactSerializer(many = True)
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'description',
            'created',
            'status',
            'author'
        ]
        

class PostCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = [
            "title", "description" , "author"
        ]
    
    
    