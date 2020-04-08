from django.db import models

class adminModel(models.Model):
    name = models.CharField(max_length=30)
    passwod = models.CharField(max_length=20)
    desgination =models.CharField(max_length=30)
    address =models.CharField(max_length=30)
    contact = models.IntegerField()
    email =models.EmailField()

