from django.contrib import admin
from django.urls import path , include
from django.views.generic import TemplateView
from .views import ListContactApi , AddContact , GetContact , DeleteContact , UpdateNotVisibleContact


app_name = "contactsapi"
urlpatterns = [
    
    path('contacts/', ListContactApi.as_view() , name="list_contact"), # lists of contact
    path('save_contact/' , AddContact.as_view() , name="save_contact"), # save contact
    
    path('contact/<str:pk>/' , GetContact.as_view() , name="contact"), # get contact by id (uuid)
    
    path('contact/delete/<str:pk>' , DeleteContact.as_view() , name="delete_contact"),# delete a contact by id
    path('contact/not_visible/<str:pk>' , UpdateNotVisibleContact.as_view() , name="not_visible"), # change value visible to false
    
]
