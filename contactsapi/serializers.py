from rest_framework import serializers
from contacts.models import Contact
from postsapi.serializers import PostListSerializer

class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        fields = "__all__"

class ContactSerializerForPost(serializers.ModelSerializer):
    
    id = serializers.UUIDField()
    name = serializers.CharField()
    telephone = serializers.CharField()
    posts = PostListSerializer(many = True)
    
    # class Meta:
    #     fields = ['id' , 'name' , 'telephone' ,'posts']

class SaveContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        fields = ["name" , "telephone"]
        

class UpdateContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        fields = ["name" , "telephone"]

class ChangeVisbleContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        fields = ["visible"]
    