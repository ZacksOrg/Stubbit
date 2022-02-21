from django.db import models
from django.contrib.auth import hashers

# Create your models here.

class Organization(models.Model):
    Name = models.CharField(max_length=50, null=True)
    Country = models.CharField(max_length=30, null=True)
    State = models.CharField(max_length=30, null=True)
    City = models.CharField(max_length=50, null=True)
    Address = models.CharField(max_length=100, null=True)
    Phone = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.Name

class Account(models.Model):
    OrganizationID = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL)
    Username = models.CharField(max_length=40, null=True)
    Email = models.CharField(max_length=60, null=True)
    Department = models.CharField(max_length=40, null=True)
    AccountCreationDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Username

class Stub(models.Model):
    URGENCY = (('High', 'High'),
               ('Medium', 'Medium'),
               ('Low', 'Low'),
        )

    Issuer = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL)
    Title = models.CharField(max_length=50, null=True)
    Overview = models.TextField(null=True)
    Category = models.CharField(max_length=40, null=True)
    Urgency = models.CharField(max_length=20, null=True, choices=URGENCY)
    CreationDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Title


    
