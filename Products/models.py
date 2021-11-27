from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    name = models.CharField(blank=False,max_length=100)
    weight = models.IntegerField(blank=True)
    price= models.IntegerField(blank=True)
    created_at= models.DateField(auto_now=True)
    updated_at= models.DateField(auto_now=True)
    def __str__(self):
        return self.name
 