from django.db import models

class recuirtmentModel(models.Model):
    oppertunitycode=models.IntegerField(primary_key=True)
    qualification=models.CharField(max_length=30)
    startregistration=models.DateField()
    agelimit=models.IntegerField()
    lastregistration=models.DateField()
    departmentid=models.CharField(max_length=10)
    positions=models.IntegerField()
    description=models.CharField(max_length=100)
    responsibilities=models.CharField(max_length=250)
    contactno=models.IntegerField()


class InterviewSeheduleModel(models.Model):
    applicantId = models.IntegerField()
    employeeId = models.IntegerField()
    scheduleDate = models.DateField()



