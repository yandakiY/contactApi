import uuid
from django.db import models

class Model(models.Model):
    
    """Generate an id based on uuid
    """
    id = models.UUIDField(verbose_name="Id" , primary_key=True, default=uuid.uuid4)
    
    class Meta:
        abstract = True