from django.db import models

class Users(models.Model):
    Name=models.TextField(max_length=100)
    Password=models.TextField()
 
