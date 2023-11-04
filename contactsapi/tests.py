from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from contacts.models import Contact
import json


# Create your tests here.

class TestContactApi(APITestCase):
    
    def setUp(self) -> None:
        Contact.objects.create(
            name="Contact" , telephone="01020304" , visible=True
        )
        Contact.objects.create(
            name="ContactA" , telephone="04050607" , visible=True
        )
        
        self.contact = Contact.objects.all()
        
        
        self.client = APIClient()
        self.data =  {
            "name": "contact",
            "telephone": "78654390",
            "visible": True
        }
        self.url = "/api/contacts/"
    
    
    def test_get_contacts(self):
        
        url = reverse("contactsapi:list_contact")
        res = self.client.get(url)
        
        self.assertEqual(res.status_code , status.HTTP_200_OK)
        
    def test_get_one_contact(self):
        
        contact = self.contact.first()
        
        url = reverse("contactsapi:contact" , args=(contact.id,))
        res = self.client.get(url , format="json")
        
        data = json.loads(res.content.decode("utf-8"))
        
        self.assertEqual(res.status_code , status.HTTP_200_OK)
        # print(data)
        self.assertEqual(data['name'] , contact.name)
        self.assertEqual(data['telephone'] , contact.telephone)
        self.assertEqual(data['visible'] , contact.visible)
        
    
    def test_post_contact(self):
        
        data = self.data
        url = reverse("contactsapi:save_contact")
        res = self.client.post(url , data)
        
        data_res = json.loads(res.content.decode("utf-8"))
        
        self.assertEqual(res.status_code , status.HTTP_201_CREATED)
        self.assertEqual(data_res['name'] , data.get("name"))
        self.assertEqual(data_res['telephone'] , data.get("telephone"))
        
    def test_update_contact(self):
        
        contact = self.contact.first() # To update
        
        new_data = {
            "name": "New Contact",
            "telephone": "11223344"
        }
        
        url = reverse("contactsapi:update_contact" , args=(contact.id,))
        res = self.client.put(url , new_data)
        
        data_res = json.loads(res.content.decode("utf-8"))
        
        self.assertEqual(res.status_code , status.HTTP_200_OK)
        self.assertEqual(data_res["name"] , new_data.get("name"))
        self.assertEqual(data_res["telephone"] , new_data.get("telephone"))
        
        
    
    def test_change_visible_false_contact(self):
        
        contact = self.contact.first() # To change visible to False
        
        url = reverse("contactsapi:not_visible" , args=(contact.id,))
        data_visible = {"visible":"false"}
        
        res = self.client.put(url , data_visible)
        data_res = json.loads(res.content.decode("utf-8"))
        
        self.assertEqual(res.status_code , status.HTTP_200_OK)
        self.assertFalse(data_res['visible'])
        
    
    def test_delete_contact(self):
        
        contact = self.contact.first() # To change visible to False
        
        url = reverse("contactsapi:delete_contact" , args=(contact.id,))
        
        res = self.client.delete(url)
        
        self.assertEqual(res.status_code , status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.contact.count() , 1) # We have now 1 contact in Database