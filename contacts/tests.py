from django.test import TestCase
from contacts.models import Contact
from posts.models import Post

# Create your tests here.

class TestContact(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        contact = Contact.objects.create(name="Contact" , telephone="11111111" , visible = True)
        
        
    def test_contact(self):
        contact = Contact.objects.first()
        
        name = contact.name
        telephone = contact.telephone
        visible = contact.visible
        
        self.assertEqual(name , "Contact")
        self.assertEqual(telephone , "11111111")
        self.assertTrue(visible)
        self.assertEqual(f'{contact}' , name+" - "+telephone)