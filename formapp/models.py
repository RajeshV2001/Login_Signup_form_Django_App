from django.db import models

# Create your models here.
class form_details(models.Model):
    email=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=20,null=False,unique=False)
    
