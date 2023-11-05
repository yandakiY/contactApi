from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from posts.models import Post
from contacts.models import Contact
import json

# Create your tests here.

class PostApiTest(APITestCase):
    
    def setUp(self) -> None:
        Contact.objects.create(
            name="Contact" , telephone="01020304" , visible=True
        )
        Contact.objects.create(
            name="ContactA" , telephone="04050607" , visible=True
        )
        
        Post.objects.create(
            title="Post 1" , description="Description 1"
        )
        Post.objects.create(
            title="Post2" , description="Description 2"
        )
        
        self.post1 = Post.objects.first()
        self.post1.author.set((Contact.objects.first(),))
        
        self.post2 = Post.objects.last()
        self.post2.author.set((Contact.objects.first() , Contact.objects.last()))
        
        
        self.posts = Post.objects.all()
        self.contact = Contact.objects.all()
        
    
    def test_get_posts(self):
        
        url = reverse("postsapi:listpost")
        
        res = self.client.get(url)
        data_res = json.loads(res.content.decode("utf-8"))
        
        self.assertEqual(res.status_code , status.HTTP_200_OK)
        self.assertEqual(len(data_res) , self.posts.count())
        # print(data_res)
        self.assertEqual(data_res[0].get("title") , self.post1.title)
        self.assertEqual(data_res[1].get("title") , self.post2.title)
        self.assertEqual(data_res[0].get("description") , self.post1.description)
        self.assertEqual(data_res[1].get("description") , self.post2.description)
        

    def test_get_one_post(self):
        
        post = Post.objects.first()
        
        url = reverse("postsapi:postbyid" , args=(post.id,))
        res = self.client.get(url)
        
        data_res = json.loads(res.content.decode("utf-8"))
        
        self.assertEqual(res.status_code , status.HTTP_200_OK)
        self.assertEqual(data_res['title'] , post.title)
        self.assertEqual(data_res['description'] , post.description)
        

    def test_create_a_post(self):
        
        
        data = {
            "title" : "Title post",
            "description": "Description post",
            "author": self.contact.first().id
        }
        
        url = reverse("postsapi:createpost")
        res = self.client.post(url , data)
        data_res = json.loads(res.content.decode("utf-8"))
        
        
        # print(data_res)
        self.assertEqual(res.status_code , status.HTTP_201_CREATED)
        self.assertEqual(data_res['title'] , data.get('title'))
        self.assertEqual(data_res['description'] , data.get('description'))
        