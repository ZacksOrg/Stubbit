from .models import *
from django.utils import timezone

class Backend:
    def CreateTestLicense():
        newLicense = License(LicenseType="Trial", LicenseContent="7b14a00p")
        newLicense.save()
    
    def CreateTestOrganization():
        newOrganization = Organization(OrganizationName="Test Organization",LicenseID=License.objects.get(LicenseContent="7b14a00p"), StartDate=timezone.now(), AddressCountry="USA", AddressState="MI", AddressZip=48306, AddressCity="Rochester", AddressStreet="University Dr", AddressBuildingNumber="ODH", PhoneNumber="+19998887777")
        newOrganization.save()
        
    def CreateTestUser():
        newUser = UserFile(Username="TestUser1", FirstName="Test", LastName="User", Email="TestUser1@gmail.com", OrganizationID=Organization.objects.get(OrganizationName="Test Organization"), Department="Controls", Administrator=True)
        newUser.save()
        
    def CreateTestUserPass():
        newUserPass = UserPass(UserFileID=UserFile.objects.get(Username="TestUser1"), EncryptedPassword="Iig1Q00eW0x+EAlVOUTDNw==", EncrpytionMethod="AES-ECB-128", EncryptionKey="1234567890123456")
        newUserPass.save()
    
    def CreateTestUserMeta():
        newUserMeta = UserMeta(UserFileID=UserFile.objects.get(Username="TestUser1"), AccountCreationDate=timezone.now(), LastLogInDate=timezone.now())
        newUserMeta.save()
    
    def CreateTestStub():
        newStub = Stub(Title="Test Stub", Overview="Hello, this is a test stub overview.", Category="Request", Urgency="When You Have Time", Domain="Mechanical Engineering", IssuerUserFileID=UserFile.objects.get(Username="TestUser1"), DeveloperUserFileID=UserFile.objects.get(Username="TestUser1"), StartDate=timezone.now(), EstimatedCompletionTime="10", EstimatedCompletionTimeUOM="Days", PriorityInQueue=5.0, InProcess=True, Completed=False, CreationDate=timezone.now())
        newStub.save()
    
    def CreateTestStubAttachment():
        newStubAttachment = StubAttachment(StubID=Stub.objects.get(Title="Test Stub"),TotalSize=1024, CompressedSize=1000, FileServerPath="/root/Folder1/File1.txt")
        newStubAttachment.save()
    
    def PrintLicenses():
        outputString = ""
        for license in License.objects.all():
            outputString += license.__str__()
            if license.pk != License.objects.all()[License.objects.all().count() - 1].pk:
                outputString += ","
        return outputString
    
    def PrintOrganizations():
        outputString = ""
        for organization in Organization.objects.all():
            outputString += organization.__str__()
            if organization.pk != Organization.objects.all()[Organization.objects.all().count() - 1].pk:
                outputString += ","
        return outputString
    
    def PrintUsers():
        outputString = ""
        for user in UserFile.objects.all():
            outputString += user.__str__()
            if user.pk != UserFile.objects.all()[UserFile.objects.all().count() - 1].pk:
                outputString += ","
        return outputString

    def PrintUserPasses():
        outputString = ""
        for userPass in UserPass.objects.all():
            outputString += userPass.__str__()
            if userPass.pk != UserPass.objects.all()[UserPass.objects.all().count() - 1].pk:
                outputString += ","
        return outputString
    
    def PrintUserMetas():
        outputString = ""
        for userMeta in UserMeta.objects.all():
            outputString += userMeta.__str__()
            if userMeta.pk != UserMeta.objects.all()[UserMeta.objects.all().count() - 1].pk:
                outputString += ","
        return outputString
    
    def PrintStubs():
        outputString = ""
        for stub in Stub.objects.all():
            outputString += stub.__str__()
            if stub.pk != Stub.objects.all()[Stub.objects.all().count() - 1].pk:
                outputString += ","
        return outputString
    
    def PrintStubAttachments():
        outputString = ""
        for stubAttachment in StubAttachment.objects.all():
            outputString += stubAttachment.__str__()
            if stubAttachment.pk != StubAttachment.objects.all()[StubAttachment.objects.all().count() - 1].pk:
                outputString += ","
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