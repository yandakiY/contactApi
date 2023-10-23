from django.shortcuts import render
from rest_framework.generics import ListAPIView , CreateAPIView , RetrieveAPIView
from contacts.models import Contact
from .serializers import ContactSerializer , SaveContactSerializer

# Create your views here.

# @api_view(["GET"])
class ListContactApi(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
    
class AddContact(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = SaveContactSerializer
    
class GetContact(RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
