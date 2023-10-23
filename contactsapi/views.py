from django.shortcuts import render
from rest_framework.generics import ListAPIView , CreateAPIView , RetrieveAPIView , DestroyAPIView , UpdateAPIView
from contacts.models import Contact
from .serializers import ContactSerializer , SaveContactSerializer, ChangeVisbleContactSerializer

# Create your views here.


#  Get list of contacts
class ListContactApi(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
# Add new contact
class AddContact(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = SaveContactSerializer
    
# Retrieve or get a contact by id
class GetContact(RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
    
# Delete a contact by id
class DeleteContact(DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
class UpdateNotVisibleContact(UpdateAPIView):
    
    serializer_class = ChangeVisbleContactSerializer
    
    def get_queryset(self):
        return Contact.objects.all()
    
