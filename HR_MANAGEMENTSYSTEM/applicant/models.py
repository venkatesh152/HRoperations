from django.db import models

class ApplicantModel(models.Model):

    name=models.CharField(max_length=30)
    dob=models.DateField()
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    gender=models.CharField(max_length=30)
    contact=models.IntegerField()
    address=models.TextField()
class ApplicationformModel(models.Model):
    name = models.CharField(max_length=30)
    dob = models.DateField()
    email = models.EmailField(max_length=30)
    gender = models.CharField(max_length=30)
    contact = models.IntegerField()
    address = models.TextField()
    qualification =models.CharField(max_length=20)
    post =models.CharField(max_length=30)
    percentage=models.DecimalField(max_digits=5,decimal_places=2)
    resume=models.FileField(upload_to="Application_Resumes/")