from django.db import models
from django.contrib.auth import hashers
import datetime
from enum import unique
from django.utils import timezone


class License(models.Model):
    LICENSETYPE = (('Trial', 'Trial'),
                   ('Tier 1', 'Tier 1'),
                   ('Tier 2', 'Tier 2'),
                   ('Tier 3', 'Tier 3'),
                   ('Tier 4', 'Tier 4'),
                   ('Tier 5', 'Tier 5'))
    LicenseType = models.CharField(max_length=15, choices=LICENSETYPE, default='Trial')
    LicenseContent = models.CharField(unique=True, max_length=50)
    def __str__(self):
        return "\nLicense record with Primary Key = {PrimaryKey}\n--------------------------------------\nLicenseType: {LicenseType}\nLicenseContent: {LicenseContent}".format(PrimaryKey=self.pk, LicenseType=self.LicenseType, LicenseContent=self.LicenseContent)

class Organization(models.Model):
    OrganizationName = models.CharField(max_length=255)
    LicenseID = models.ForeignKey(License, on_delete=models.CASCADE, null=True)
    StartDate = models.DateTimeField(auto_now_add=True)
    AddressCountry = models.CharField(max_length=20)
    AddressState = models.CharField(max_length=2)
    AddressZip = models.IntegerField()
    AddressCity = models.CharField(max_length=20)
    AddressStreet = models.CharField(max_length=20)
    AddressBuildingNumber = models.CharField(null=True, max_length=20)
    PhoneNumber = models.CharField(null=True, max_length=12)
    def __str__(self):
        return "\nOrganization record with Primary Key = {PrimaryKey}\n--------------------------------------\nOrganizationName: {OrganizationName}\nLicenseID: {LicenseID}\nStartDate: {StartDate}\nAddressCountry: {AddressCountry}\nAddressState: {AddressState}\nAddressZip: {AddressZip}\nAddressCity: {AddressCity}\nAddressStreet: {AddressStreet}\nAddressBuildingNumber: {AddressBuildingNumber}\nPhoneNumber: {PhoneNumber}".format(PrimaryKey=self.pk, OrganizationName=self.OrganizationName,LicenseID=self.LicenseID.pk, StartDate=self.StartDate, AddressCountry=self.AddressCountry, AddressState=self.AddressState, AddressZip=self.AddressZip, AddressCity=self.AddressCity, AddressStreet=self.AddressStreet, AddressBuildingNumber=self.AddressBuildingNumber, PhoneNumber=self.PhoneNumber)

class UserFile(models.Model):
    Username = models.CharField(unique=True, max_length=20)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Name = models.CharField(max_length=510, default='')
    Email = models.CharField(max_length=255)
    OrganizationID = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    Department = models.CharField(max_length=20)
    Administrator = models.BooleanField()
    def __str__(self):
        return "\nUserFile record with Primary Key = {PrimaryKey}\n--------------------------------------\nUsername: {Username}\nFirstName: {FirstName}\nLastName: {LastName}\nEmail: {Email}\nOrganizationID: {OrganizationID}\nDepartment: {Department}\nAdministrator: {Administrator}".format(PrimaryKey=self.pk, Username=self.Username, FirstName=self.FirstName, LastName=self.LastName, Email=self.Email, OrganizationID=self.OrganizationID.pk, Department=self.Department, Administrator=self.Administrator)
    
class UserPass(models.Model):
    UserFileID = models.ForeignKey(UserFile, on_delete=models.CASCADE)
    EncryptedPassword = models.CharField(max_length=60)
    EncrpytionMethod = models.CharField(max_length=10)
    EncryptionKey = models.CharField(max_length=255)
    def __str__(self):
        return "\nUserPass record with Primary Key = {PrimaryKey}\n--------------------------------------\nUserFileID: {UserFileID}\nEncryptedPassword: {EncryptedPassword}\nEncrpytionMethod: {EncrpytionMethod}\nEncryptionKey: {EncryptionKey}".format(PrimaryKey=self.pk, UserFileID=self.UserFileID.pk, EncryptedPassword=self.EncryptedPassword, EncrpytionMethod=self.EncrpytionMethod, EncryptionKey=self.EncryptionKey)

class UserMeta(models.Model):
    UserFileID = models.ForeignKey(UserFile, on_delete=models.CASCADE)
    AccountCreationDate = models.DateTimeField(null=True, auto_now_add=True)
    LastLogInDate = models.DateTimeField(null=True)
    LastIPAddress = models.CharField(null=True, max_length=15, default="")
    def __str__(self):
        return "\nUserMeta record with Primary Key = {PrimaryKey}\n--------------------------------------\nUserFileID: {UserFileID}\nAccountCreationDate: {AccountCreationDate}\nLastLogInDate: {LastLogInDate}".format(PrimaryKey=self.pk, UserFileID=self.UserFileID.pk, AccountCreationDate=self.AccountCreationDate, LastLogInDate=self.LastLogInDate)

class Stub(models.Model):
    CATEGORY = (('Request', 'Request'),
               ('Bug', 'Bug'),
               ('New Feature', 'New Feature'),
               ('Upgrade', 'Upgrade'),
               ('Improvement', 'Improvement'),
               ('Suggestion', 'Suggestion'),
               ('System Failure', 'System Failure'),
        )
    URGENCY = (('Immediate', 'Immediate'),
               ('Highly Important', 'Highly Important'),
               ('Important', 'Important'),
               ('Somewhat Important', 'Somewhat Important'),
               ('When You Have Time', 'When You Have Time'),
        )
    
    Title = models.CharField(max_length=255)
    Overview = models.CharField(max_length=65535)
    Category = models.CharField(max_length=14, choices=CATEGORY)
    Urgency = models.CharField(max_length=18, choices=URGENCY)
    Domain = models.CharField(max_length=20)
    IssuerUserFileID = models.ForeignKey(UserFile, on_delete=models.CASCADE, related_name="IssuerUserFileID")
    RecipientUserFileID = models.ForeignKey(UserFile, on_delete=models.CASCADE, related_name="RecipientUserFileID")
    StartDate = models.DateTimeField(null=True)
    EstimatedCompletionTime = models.IntegerField(null=True)
    EstimatedCompletionTimeUOM = models.CharField(null=True, max_length=1)
    PriorityInQueue = models.FloatField(null=True)
    InProcess = models.BooleanField()
    Completed = models.BooleanField()
    CreationDate = models.DateField(auto_now_add=True)
    def __str__(self):
        return "\nStub Record with Primary Key = {PrimaryKey}\n--------------------------------------\nTitle: {Title}\nOverview: {Overview}\nCategory: {Category}\nUrgency: {Urgency}\nDomain: {Domain}\nDeveloperUserFileID: {RecipientUserFileID}\nStartDate: {StartDate}\nEstimatedCompletionTime: {EstimatedCompletionTime}\nEstimatedCompletionTimeUOM: {EstimatedCompletionTimeUOM}\nPriorityInQueue: {PriorityInQueue}\nInProcess: {InProcess}\nCompleted: {Completed}\nCreationDate: {CreationDate}".format(PrimaryKey=self.pk, Title=self.Title, Overview=self.Overview, Category=self.Category, Urgency=self.Urgency, Domain=self.Domain, RecipientUserFileID=self.RecipientUserFileID.pk, StartDate=self.StartDate, EstimatedCompletionTime=self.EstimatedCompletionTime, EstimatedCompletionTimeUOM=self.EstimatedCompletionTimeUOM, PriorityInQueue=self.PriorityInQueue, InProcess=self.InProcess, Completed=self.Completed, CreationDate=self.CreationDate)

class tbl_Authentication(models.Model):
    Empcode = models.IntegerField()
    username = models.CharField(max_length=50,default='')
    password = models.CharField(max_length=50,default='')
    is_active = models.IntegerField(null=True)
 
    def __str__(self):
        return self.username
 
    empAuth_objects = models.Manager()
    