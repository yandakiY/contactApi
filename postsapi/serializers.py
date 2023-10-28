from rest_framework import serializers
from posts.models import Post


class PostListSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'description',
            'created',
            'status',
            'author',
        ]
        

class PostCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'author'
        ]