from django.db import models
from utils.models import Model as MyModel

# Create your models here.
class Contact(MyModel):
    
    name = models.CharField(max_length=200 , default=None , null=False, blank=False)
    telephone = models.TextField(verbose_name="Telephone")
    visible = models.BooleanField(verbose_name="Visible" , default=True)
    
    def __str__(self) -> str:
        return f'{self.name} - {self.telephone}'
    
    class Meta:
        ordering = ["name"]
    

