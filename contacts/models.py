from django.db import models
from utils.models import Model as MyModel

# Create your models here.
class Contact(MyModel):
    
    name = models.CharField(max_length=200)
    telephone = models.TextField(verbose_name="Telephone")
    
    class Meta:
        ordering = ["-id"]
    

