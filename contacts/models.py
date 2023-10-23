from django.db import models
from utils.models import Model as MyModel

# Create your models here.
class Contact(MyModel):
    
    name = models.CharField(max_length=200 , default=None)
    telephone = models.TextField(verbose_name="Telephone")
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        ordering = ["-id"]
    

