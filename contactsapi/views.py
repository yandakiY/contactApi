from django.shortcuts import render
from rest_framework.views import Response
from rest_framework.generics import ListAPIView , CreateAPIView , RetrieveAPIView , DestroyAPIView , UpdateAPIView
from contacts.models import Contact
from .serializers import ContactSerializer , SaveContactSerializer, ChangeVisbleContactSerializer , UpdateContactSerializer

# Create your views here.


#  Get list of contacts
class ListContactApi(ListAPIView):
    queryset = Contact.objects.all().filter(visible = True)
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


class UpdateContact(UpdateAPIView):
    
    queryset = Contact.objects.all()
    serializer_class = UpdateContactSerializer
    
    def update(self, request, *args, **kwargs):
        
        instance = self.get_object()
        serializer = self.get_serializer(instance , data = request.data , partial = True)
        serializer.is_valid(raise_exception = True)
        serializer.save() # update of object
        
        return Response(serializer.data)
        
    
class UpdateVisibleContact(UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ChangeVisbleContactSerializer
    
    def get_queryset(self):
        return Contact.objects.all()
    

# Views contacts with prop visible = False
class ListContactFalse(ListAPIView):
    queryset = Contact.objects.all().filter(visible = False)
    serializer_class = ContactSerializer
  