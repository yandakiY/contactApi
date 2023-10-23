from django.contrib import admin
from django.urls import path , include
from django.views.generic import TemplateView


app_name = "contacts"
urlpatterns = [
    path('', TemplateView.as_view(template_name="contacts/index.html") , name="index"),
    # path('' ,include('contactsapi.urls'))
]
