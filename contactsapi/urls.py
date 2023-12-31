from django.contrib import admin
from django.urls import path , include
from django.views.generic import TemplateView
from .views import ListContactApi , AddContact , GetContact , DeleteContact , UpdateVisibleContact , UpdateContact , ListContactFalse, GetPostForContact


app_name = "contactsapi"
urlpatterns = [
    
    path('contacts/', ListContactApi.as_view() , name="list_contact"), # lists of contact
    path('contacts_false/', ListContactFalse.as_view() , name="list_contact_false"), # lists of contact with visible False
    
    path('save_contact/' , AddContact.as_view() , name="save_contact"), # save contact
    
    path('contact/<str:pk>/' , GetContact.as_view() , name="contact"), # get contact by id (uuid)
    
    path('contact/delete/<str:pk>' , DeleteContact.as_view() , name="delete_contact"),# delete a contact by id
    path('contact/not_visible/<str:pk>' , UpdateVisibleContact.as_view() , name="not_visible"), # change value visible to false
    path('contact/update_contact/<str:pk>' , UpdateContact.as_view() , name="update_contact"), # Update a contact
    
    
    path('contact/posts/<str:pk>/' , GetPostForContact.as_view() , name="postforcontact"), # get post for each contact

    
]
