
from .models import *
from django.utils import timezone
from ipware import get_client_ip
from django.contrib import messages

import time
ActiveUser = ""

class _Stub_:
    def __init__(self) -> None:
        title = ""
        overview = ""
        category = ""
        urgency = ""
        domain = ""
        issuerUserFileID = ""
        recipientUserFileID = ""
        startDate = ""
        estimatedCompletionTime = 0
        estimatedCompletionTimeUOM = ""
        priorityInQueue = 0.0
        inProcess = False
        completed = False
        creationDate = ""
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
    
    title = ""
    overview = ""
    category = ""
    urgency = ""
    domain = ""
    issuerUserFileID = ""
    recipientUserFileID = ""
    startDate = ""
    estimatedCompletionTime = 0
    estimatedCompletionTimeUOM = ""
    priorityInQueue = 0.0
    inProcess = False
    completed = False
    creationDate = ""

class Backend:
    def Timer():
        timesec = 3
        while timesec > 0:
            timesec -= 1
            time.sleep(1)
        return True
    def Authentication(username, password):
        try:
            user = UserFile.objects.get(Username=username)
            userPassword = UserPass.objects.get(UserFileID=user.pk, EncryptedPassword=password)
            return True
        except Exception as identifier:
            return False

    def Attempt_SignIn_User(username, password):
        return True
    def Attempt_SignUp_User(username, emailAddress, department, licenseKey, Password):
        return True
    def Check_UserName_Availability(username):
        return True
    def Retrieve_CurrentUser_Username():
        return "Test Username"
    def Retrieve_CurrentUser_PrimaryKey():
        return UserFile.objects.all[0].pk
    def Retrieve_CurrentUser_EmailAddress():
        return "Test Email Address"
    def Retrieve_CurrentUser_Department():
        return "Test Department"
    def Retrieve_CurrentUser_Organization():
        return "Test Organization"
    def Retrieve_CurrentUser_Name():
        return "Test Name"
    def Retrieve_CurrentUser_Administrator():
        return False
    def CreateStub(title, overview, category, urgency, domain, recipient):
        return True
    def Retrieve_Stub_Title(primaryKey):
        return "Test Title"
    def Retrieve_Stub_Overview(primaryKey):
        return "Test Overview"
    def Retrieve_Stub_Category(primaryKey):
        return _Stub_.CATEGORY[0]
    def Retrieve_Stub_Urgency(primaryKey):
        return _Stub_.URGENCY[0]
    def Retrieve_Stub_Domain(primaryKey):
        return "Test Domain"
    def Retrieve_Stub_IssuerName(primaryKey):
        return "Test Issuer Name"
    def Retrieve_Stub_RecipientName(primaryKey):
        return "Test Recipient Name"
    def Retrieve_Stub_StartDate(primaryKey):
        return "Test Start Date"
    def Retrieve_Stub_EstimatedCompletionTime(primaryKey):
        return 0
    def Retrieve_Stub_EstimatedCompletionTimeUOM(primaryKey):
        return "Test UoM"
    def Retrieve_Stub_PriorityInQueue(primaryKey):
        return 0
    def Retrieve_Stub_InProcess(primaryKey):
        return _Stub_()
    def Retrieve_Stub_Completed(primaryKey):
        return False
    def Retrieve_Stub_CreationDate(primaryKey):
        return "01/01/2000"
    def Update_Stub_StartDate(primaryKey, startDate):
        return True
    def Update_Stub_EstimatedCompletionTime(primaryKey, estimatedCompletionTime):
        return True
    def Update_Stub_EstimatedCompletionTimeUOM(primaryKey, estimatedCompletionTimeUOM):
        return True
    def Update_Stub_PriorityInQueue(primaryKey, priorityInQueue):
        return True
    def Attempt_Add_Organization(organizationName, addressCountry, addressState, addressCity, addressZip, addressStreet, addressBuildingNumber, phoneNumber):
        return True
    def Retrieve_StubInProcess():
        return _Stub_()
    def Retrieve_ReceivedStubs():
        return [_Stub_()]
    def Retrieve_SentStubs():
        return [_Stub_()]
    def Retrieve_OrganizationStubs():
        return [_Stub_()]
    def Retrieve_HistoryReceivedStubs():
        return [_Stub_()]
    def Retrieve_HistorySentStubs():
        return [_Stub_()]
    def Retrieve_HistoryOrganizationStubs():
        return [_Stub_()]

    def CreateTestLicenses():
        newLicense = License(LicenseType="Trial", LicenseContent="7b14a00p")
        newLicense.save()
    
    def CreateTestOrganizations():
        newOrganization = Organization(OrganizationName="Test Organization",LicenseID=License.objects.get(LicenseContent="7b14a00p"), StartDate=timezone.now(), AddressCountry="USA", AddressState="MI", AddressZip=48306, AddressCity="Rochester", AddressStreet="University Dr", AddressBuildingNumber="ODH", PhoneNumber="+19998887777")
        newOrganization.save()
        
    def CreateTestUsers():
        newUser1 = UserFile(Username="TestUser1", FirstName="Test", LastName="User", Email="TestUser1@gmail.com", OrganizationID=Organization.objects.get(OrganizationName="Test Organization"), Department="Controls", Administrator=True)
        newUser2 = UserFile(Username="TestUser2", FirstName="Test2", LastName="User2", Email="TestUser2@gmail.com", OrganizationID=Organization.objects.get(OrganizationName="Test Organization"), Department="Accounting", Administrator=True)
        newUser1.save()
        newUser2.save()
        
    def CreateTestUserPasses():
        newUserPass1 = UserPass(UserFileID=UserFile.objects.get(Username="TestUser1"), EncryptedPassword="apples", EncrpytionMethod="AES-ECB-128", EncryptionKey="1234567890123456")
        newUserPass2 = UserPass(UserFileID=UserFile.objects.get(Username="TestUser2"), EncryptedPassword="+a002abdd21122ba0201fjaj", EncrpytionMethod="AES-ECB-128", EncryptionKey="1111111111111111")
        newUserPass1.save()
        newUserPass2.save()
    
    def CreateTestUserMetas():
        newUserMeta1 = UserMeta(UserFileID=UserFile.objects.get(Username="TestUser1"), AccountCreationDate=timezone.now(), LastLogInDate=timezone.now())
        newUserMeta2 = UserMeta(UserFileID=UserFile.objects.get(Username="TestUser2"), AccountCreationDate=timezone.now(), LastLogInDate=timezone.now())
        newUserMeta1.save()
        newUserMeta2.save()

    def CreateTestStubs():
        newStub1 = Stub(Title="Crank Shaft Fix", Overview="Fix this so we can get production rolling!", Category="System Failure", Urgency="Immediate", Domain="Mechanical Engineering", IssuerUserFileID=UserFile.objects.get(Username="TestUser1"), RecipientUserFileID=UserFile.objects.get(Username="TestUser2"), StartDate=timezone.now(), EstimatedCompletionTime="1", EstimatedCompletionTimeUOM="Days", PriorityInQueue=1.0, InProcess=True, Completed=False, CreationDate=timezone.now())
        newStub2 = Stub(Title="Rounding Error", Overview="I'm pretty sure that .49 should round to 0 not 1. See attachment below.", Category="Bug", Urgency="When You Have Time", Domain="Database", IssuerUserFileID=UserFile.objects.get(Username="TestUser1"), RecipientUserFileID=UserFile.objects.get(Username="TestUser2"), StartDate=timezone.now(), EstimatedCompletionTime="3", EstimatedCompletionTimeUOM="Days", PriorityInQueue=5.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub3 = Stub(Title="Spare Parts By Product Line", Overview="Need this ASAP for management.", Category="Request", Urgency="Highly Important", Domain="Accounting", IssuerUserFileID=UserFile.objects.get(Username="TestUser2"), RecipientUserFileID=UserFile.objects.get(Username="TestUser1"), StartDate=timezone.now(), EstimatedCompletionTime="2", EstimatedCompletionTimeUOM="Hours", PriorityInQueue=1.0, InProcess=True, Completed=False, CreationDate=timezone.now())
        newStub1.save()
        newStub2.save()
        newStub3.save()
    
    def CreateTestStubAttachments():
        newStubAttachment = StubAttachment(StubID=Stub.objects.get(Title="Rounding Error"),TotalSize=1024, CompressedSize=1000, FileServerPath="/root/Folder1/File1.txt")
        newStubAttachment.save()
    
    def PrintLicenses():
        outputString = ""
        for license in License.objects.all():
            outputString+= license.__str__()
            if license.pk != License.objects.all()[License.objects.all().count() - 1].pk:
                outputString+= ","
        return outputString
    
    def PrintOrganizations():
        outputString= ""
        for organization in Organization.objects.all():
            outputString+= organization.__str__()
            if organization.pk != Organization.objects.all()[Organization.objects.all().count() - 1].pk:
                outputString+= ","
        return outputString
    
    def PrintUsers():
        outputString= ""
        for user in UserFile.objects.all():
            outputString+= user.__str__()
            if user.pk != UserFile.objects.all()[UserFile.objects.all().count() - 1].pk:
                outputString+= ","
        return outputString

    def PrintUserPasses():
        outputString= ""
        for userPass in UserPass.objects.all():
            outputString+= userPass.__str__()
            if userPass.pk != UserPass.objects.all()[UserPass.objects.all().count() - 1].pk:
                outputString+= ","
        return outputString
    
    def PrintUserMetas():
        outputString= ""
        for userMeta in UserMeta.objects.all():
            outputString+= userMeta.__str__()
            if userMeta.pk != UserMeta.objects.all()[UserMeta.objects.all().count() - 1].pk:
                outputString+= ","
        return outputString
    
    def PrintStubs():
        outputString= ""
        for stub in Stub.objects.all():
            outputString+= stub.__str__()
            if stub.pk != Stub.objects.all()[Stub.objects.all().count() - 1].pk:
                outputString+= ","
        return outputString
    
    def PrintStubAttachments():
        outputString= ""
        for stubAttachment in StubAttachment.objects.all():
            outputString+= stubAttachment.__str__()
            if stubAttachment.pk != StubAttachment.objects.all()[StubAttachment.objects.all().count() - 1].pk:
                outputString+= ","
        return outputString

    def WipeLicenses():
        for license in License.objects.all():
            license.delete()
            
    def WipeOrganizations():
        for organization in Organization.objects.all():
            organization.delete()
            
    def WipeUsers():
        for user in UserFile.objects.all():
            user.delete()

    def WipeUserPasses():
        for userPass in UserPass.objects.all():
            userPass.delete()
    
    def WipeUserMetas():
        for userMeta in UserMeta.objects.all():
            userMeta.delete()  
            
    def WipeStubs():
        for stub in Stub.objects.all():
            stub.delete()   
    
    def WipeStubAttachments(): 
        for stubAttachment in StubAttachment.objects.all():
            stubAttachment.delete()
    
    def DatabaseRefreshWithTestData():
        Backend.WipeStubAttachments()
        Backend.WipeStubs()
        Backend.WipeUserMetas()
        Backend.WipeUserPasses()
        Backend.WipeUsers()
        Backend.WipeOrganizations()
        Backend.WipeLicenses()
        
        Backend.CreateTestLicenses()
        Backend.CreateTestOrganizations()
        Backend.CreateTestUsers()
        Backend.CreateTestUserPasses()
        Backend.CreateTestUserMetas()
        Backend.CreateTestStubs()
        Backend.CreateTestStubAttachments()
    
    def LogInSuccess_UpdateUserMeta(username, request):
        client_ip, is_routable = get_client_ip(request)
        user_obj = UserFile.objects.get(Username=username)
        usermeta_obj = UserMeta.objects.get(UserFileID=user_obj)
        usermeta_obj.LastLogInDate = timezone.now()
        usermeta_obj.LastIPAddress = client_ip
        usermeta_obj.save()
    
    def GetLoggedInUserObj(request):
        client_ip, is_routable = get_client_ip(request)
        usermeta_obj = UserMeta.objects.get(LastIPAddress=client_ip)
        timeSinceLastLogin = datetime.datetime.now(timezone.utc) - usermeta_obj.LastLogInDate   
        if (timeSinceLastLogin.seconds//60) < 60:
            user_obj = UserFile.objects.get(id=usermeta_obj.UserFileID.pk)
            return user_obj
        
        return None