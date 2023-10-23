from django.contrib import admin
from django.urls import path , include
from django.views.generic import TemplateView
from .views import *


app_name = "contactsapi"
urlpatterns = [
    path('contacts/', ListContactApi.as_view() , name="listcontact"),
    path('save_contact/' , AddContact.as_view() , name="save_contact"),
    path('contact/<str:pk>/' , GetContact.as_view() , name="contact")
]
