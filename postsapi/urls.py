from django.contrib import admin
from django.urls import path , include
from django.views.generic import TemplateView
from postsapi.views import ListPostView , CreatePostView , PostViewById

app_name = "postsapi"
urlpatterns = [
    path('', ListPostView.as_view() , name="listpost"), # lists of all posts
    path('create-post/' , CreatePostView.as_view() , name="createpost"), # create a new post
    path('<str:pk>/' , PostViewById.as_view() , name="postbyid"), # post by id
]
