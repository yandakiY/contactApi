from django.test import TestCase
from contacts.models import Contact
from posts.models import Post

class TestPosts(TestCase):
    

    @classmethod    
    def setUpTestData(cls):
        
        Contact.objects.create(
            name="Contact" , telephone="11111111" , visible = True
        )
        
        Contact.objects.create(
            name="ContactA" , telephone="00112233" , visible = True
        )
        
        Post.objects.create(
            title = "Title",
            description ="Description post",
        )
        
        post = Post.objects.get(title = "Title")
        contact = Contact.objects.get(name="Contact")
        
        post.author.set((contact,))
        
    
    def test_post(self):
        
        post = Post.objects.first()
        title_post = post.title
        description_post = post.description
        
        
        first_contact = Contact.objects.first()
        
        name_first_contact = first_contact.name
        tel_first_contact = first_contact.telephone
        
        self.assertEqual(post.title , title_post)
        self.assertEqual(post.description , description_post)
        self.assertEqual(f'{post}' , title_post + " ("+name_first_contact +" - "+ tel_first_contact +")")