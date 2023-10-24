from rest_framework import serializers
from contacts.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        fields = "__all__"
        

class SaveContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        fields = ["name" , "telephone"]
        

class UpdateContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        fields = ["name" , "telephone"]

class ChangeVisbleContactSerializer(serializers.ModelSerializer):
    
    # visible = serializers.ModelSerializer(source="visible" , data=False)
    
    class Meta:
        model = Contact
        fields = ["visible"]
    