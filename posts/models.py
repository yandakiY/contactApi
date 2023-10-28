from django.db import models
# from rest_framework import 
from django_extensions.db.models import TitleSlugDescriptionModel,ActivatorModel,TimeStampedModel
from utils.models import Model
from contacts.models import Contact

# Create your models here.

class Post(
    Model,TitleSlugDescriptionModel, ActivatorModel, TimeStampedModel, models.Model
):
    
    author = models.ManyToManyField(Contact)
    
    
    def __str__(self):
        author_str = ", ".join(str(a) for a in self.author.all())
        return f'{self.title} ( {author_str} )'
    class Meta:
        ordering = ['title']