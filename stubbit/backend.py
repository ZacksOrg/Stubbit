
from audioop import add
from .models import *
from django.utils import timezone
from ipware import get_client_ip
from django.contrib import messages
import random
import string
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
        newLicense1 = License(LicenseType="Trial", LicenseContent="7b14a00p")
        newLicense2 = License(LicenseType="Company", LicenseContent="j54h9u20")
        newLicense1.save()
        newLicense2.save()

    def CreateTestOrganizations():
        newOrganization1 = Organization(OrganizationName="Nova Electronics",LicenseID=License.objects.get(LicenseContent="7b14a00p"), StartDate=timezone.now(), AddressCountry="USA", AddressState="MD", AddressZip=90266, AddressCity="Bethesda", AddressStreet="South Oak Rd", AddressBuildingNumber="455", PhoneNumber="+18447639233")
        newOrganization2 = Organization(OrganizationName="Aristo Industries",LicenseID=License.objects.get(LicenseContent="j54h9u20"), StartDate=timezone.now(), AddressCountry="USA", AddressState="MI", AddressZip=48127, AddressCity="Detroit", AddressStreet="West Grand Boulevard", AddressBuildingNumber="219", PhoneNumber="+13132489116")
        newOrganization3 = Organization(OrganizationName="Tanaka Manufacturing",LicenseID=License.objects.get(LicenseContent="j54h9u20"), StartDate=timezone.now(), AddressCountry="USA", AddressState="WA", AddressZip=72715, AddressCity="Seattle", AddressStreet="North Winsome St", AddressBuildingNumber="368", PhoneNumber="+12861743885")
        newOrganization1.save()
        newOrganization2.save()
        newOrganization3.save()

    def CreateTestUsers():
        newUser1 = UserFile(Username="BobFitz", FirstName="Bob", LastName="Fitzgerald", Name="Bob Fitzgerald", Email="bob_fitzgerald@gmail.com", OrganizationID=Organization.objects.get(OrganizationName="Nova Electronics"), Department="Manufacturing", Administrator=True)
        newUser2 = UserFile(Username="JasonM", FirstName="Jason", LastName="Miller", Name="Jason Miller", Email="jason_miller@gmail.com", OrganizationID=Organization.objects.get(OrganizationName="Nova Electronics"), Department="Accounting", Administrator=True)
        newUser3 = UserFile(Username="Arthur_T", FirstName="Arthur", LastName="Thompson", Name="Arthur Thompson", Email="arthur_thompson@gmail.com", OrganizationID=Organization.objects.get(OrganizationName="Aristo Industries"), Department="Human Resource", Administrator=True)
        newUser4 = UserFile(Username="KellyNichols", FirstName="Kelly", LastName="Nichols", Name="Kelly Nichols", Email="kelly_nichols@gmail.com", OrganizationID=Organization.objects.get(OrganizationName="Tanaka Manufacturing"), Department="Marketing", Administrator=True)
        newUser5 = UserFile(Username="BrettNes", FirstName="Brett", LastName="Nesbitt", Name="Brett Nesbitt", Email="brett_nesbitt@gmail.com", OrganizationID=Organization.objects.get(OrganizationName="Tanaka Manufacturing"), Department="Production", Administrator=True)
        newUser1.save()
        newUser2.save()
        newUser3.save()
        newUser4.save()
        newUser5.save()

    def CreateTestUserPasses():
        newUserPass1 = UserPass(UserFileID=UserFile.objects.get(Username="BobFitz"), EncryptedPassword="apples", EncrpytionMethod="AES-ECB-128", EncryptionKey="1234567890123456")
        newUserPass2 = UserPass(UserFileID=UserFile.objects.get(Username="JasonM"), EncryptedPassword="+a002abdd21122ba0201fjaj", EncrpytionMethod="AES-ECB-128", EncryptionKey="1111111111111111")
        newUserPass3 = UserPass(UserFileID=UserFile.objects.get(Username="Arthur_T"), EncryptedPassword="lksn453f9dnw9f", EncrpytionMethod="AES-ECB-128", EncryptionKey="1111111111111111")
        newUserPass4 = UserPass(UserFileID=UserFile.objects.get(Username="KellyNichols"), EncryptedPassword="9s0ausdf0a2hk", EncrpytionMethod="AES-ECB-128", EncryptionKey="1111111111111111")
        newUserPass5 = UserPass(UserFileID=UserFile.objects.get(Username="BrettNes"), EncryptedPassword="9sg93jf83ncm2c", EncrpytionMethod="AES-ECB-128", EncryptionKey="1111111111111111")
        newUserPass1.save()
        newUserPass2.save()
        newUserPass3.save()
        newUserPass4.save()
        newUserPass5.save()

    def CreateTestUserMetas():
        newUserMeta1 = UserMeta(UserFileID=UserFile.objects.get(Username="BobFitz"), AccountCreationDate=timezone.now(), LastLogInDate=timezone.now())
        newUserMeta2 = UserMeta(UserFileID=UserFile.objects.get(Username="JasonM"), AccountCreationDate=timezone.now(), LastLogInDate=timezone.now())
        newUserMeta3 = UserMeta(UserFileID=UserFile.objects.get(Username="Arthur_T"), AccountCreationDate=timezone.now(), LastLogInDate=timezone.now())
        newUserMeta4 = UserMeta(UserFileID=UserFile.objects.get(Username="KellyNichols"), AccountCreationDate=timezone.now(), LastLogInDate=timezone.now())
        newUserMeta5 = UserMeta(UserFileID=UserFile.objects.get(Username="BrettNes"), AccountCreationDate=timezone.now(), LastLogInDate=timezone.now())
        newUserMeta1.save()
        newUserMeta2.save()
        newUserMeta3.save()
        newUserMeta4.save()
        newUserMeta5.save()

    def CreateTestStubs():
        newStub1 = Stub(Title="Crank Shaft Fix", Overview="Fix this so we can get production rolling!", Category="System Failure", Urgency="Immediate", Domain="Mechanical Engineering", IssuerUserFileID=UserFile.objects.get(Username="BobFitz"), RecipientUserFileID=UserFile.objects.get(Username="KellyNichols"), StartDate=timezone.now(), EstimatedCompletionTime="1", EstimatedCompletionTimeUOM="Days", PriorityInQueue=1.0, InProcess=True, Completed=False, CreationDate=timezone.now())
        newStub2 = Stub(Title="Rounding Error", Overview="I'm pretty sure that .49 should round to 0 not 1. See attachment below.", Category="Bug", Urgency="When You Have Time", Domain="Database", IssuerUserFileID=UserFile.objects.get(Username="BobFitz"), RecipientUserFileID=UserFile.objects.get(Username="JasonM"), StartDate=timezone.now(), EstimatedCompletionTime="3", EstimatedCompletionTimeUOM="Days", PriorityInQueue=5.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub3 = Stub(Title="Spare Parts By Product Line", Overview="Need this ASAP for management.", Category="Request", Urgency="Highly Important", Domain="Accounting", IssuerUserFileID=UserFile.objects.get(Username="BrettNes"), RecipientUserFileID=UserFile.objects.get(Username="BobFitz"), StartDate=timezone.now(), EstimatedCompletionTime="2", EstimatedCompletionTimeUOM="Hours", PriorityInQueue=1.0, InProcess=True, Completed=False, CreationDate=timezone.now())
        newStub4 = Stub(Title="Rotary Girder Specification in AutoCAD", Overview="Check the endline specs on the rotary girder.", Category="Suggestion", Urgency="When You Have Time", Domain="Mechanical Engineering", IssuerUserFileID=UserFile.objects.get(Username="JasonM"), RecipientUserFileID=UserFile.objects.get(Username="BobFitz"), StartDate=timezone.now(), EstimatedCompletionTime="5", EstimatedCompletionTimeUOM="Minutes", PriorityInQueue=1.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub5 = Stub(Title="Parts Order", Overview="Need to order more parts from supplier.", Category="Request", Urgency="Highly Important", Domain="Supplier", IssuerUserFileID=UserFile.objects.get(Username="BobFitz"), RecipientUserFileID=UserFile.objects.get(Username="BrettNes"), StartDate=timezone.now(), EstimatedCompletionTime="10", EstimatedCompletionTimeUOM="Minutes", PriorityInQueue=3.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub6 = Stub(Title="Employee Information Required", Overview="Need information for payroll.", Category="Request", Urgency="Highly Important", Domain="Finance", IssuerUserFileID=UserFile.objects.get(Username="JasonM"), RecipientUserFileID=UserFile.objects.get(Username="BobFitz"), StartDate=timezone.now(), EstimatedCompletionTime="30", EstimatedCompletionTimeUOM="Minutes", PriorityInQueue=4.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub7 = Stub(Title="Missing URL Paths", Overview="Some web pages are missing their URL paths.", Category="Bug", Urgency="Important", Domain="Development", IssuerUserFileID=UserFile.objects.get(Username="BobFitz"), RecipientUserFileID=UserFile.objects.get(Username="KellyNichols"), StartDate=timezone.now(), EstimatedCompletionTime="20", EstimatedCompletionTimeUOM="Minutes", PriorityInQueue=2.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub8 = Stub(Title="Project Percentage of Complete General Ledger WIP Rotation Issue", Overview="Request for parts form displaying incorrectly", Category="Bug", Urgency="Important", Domain="Development", IssuerUserFileID=UserFile.objects.get(Username="Arthur_T"), RecipientUserFileID=UserFile.objects.get(Username="BobFitz"), StartDate=timezone.now(), EstimatedCompletionTime="10", EstimatedCompletionTimeUOM="Minutes", PriorityInQueue=1.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub9 = Stub(Title="Product Line Failure", Overview="Line production has been halted from a failure.", Category="System Failure", Urgency="Immediate", Domain="Production", IssuerUserFileID=UserFile.objects.get(Username="Arthur_T"), RecipientUserFileID=UserFile.objects.get(Username="BobFitz"), StartDate=timezone.now(), EstimatedCompletionTime="35", EstimatedCompletionTimeUOM="Minutes", PriorityInQueue=3.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub10 = Stub(Title="Office Help", Overview="I need some assistance moving things in the office.", Category="Request", Urgency="When You Have Time", Domain="Office", IssuerUserFileID=UserFile.objects.get(Username="JasonM"), RecipientUserFileID=UserFile.objects.get(Username="BobFitz"), StartDate=timezone.now(), EstimatedCompletionTime="45", EstimatedCompletionTimeUOM="Minutes", PriorityInQueue=3.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub11 = Stub(Title="Special Part Pickup", Overview="Need to get a specific part from the supplier.", Category="Request", Urgency="Important", Domain="Supplier", IssuerUserFileID=UserFile.objects.get(Username="BobFitz"), RecipientUserFileID=UserFile.objects.get(Username="BrettNes"), StartDate=timezone.now(), EstimatedCompletionTime="30", EstimatedCompletionTimeUOM="Minutes", PriorityInQueue=1.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub12 = Stub(Title="Deliver Box Of Parts", Overview="Deliver these parts to the industrial sector.", Category="Request", Urgency="When You Have Time", Domain="Production", IssuerUserFileID=UserFile.objects.get(Username="JasonM"), RecipientUserFileID=UserFile.objects.get(Username="BobFitz"), StartDate=timezone.now(), EstimatedCompletionTime="2", EstimatedCompletionTimeUOM="Hours", PriorityInQueue=1.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub13 = Stub(Title="Access Issue", Overview="Change group policy to allow portal access.", Category="Request", Urgency="Important", Domain="IT", IssuerUserFileID=UserFile.objects.get(Username="KellyNichols"), RecipientUserFileID=UserFile.objects.get(Username="BobFitz"), StartDate=timezone.now(), EstimatedCompletionTime="2", EstimatedCompletionTimeUOM="Hours", PriorityInQueue=1.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub14 = Stub(Title="Network Connection", Overview="Users keep disconnecting from wifi.", Category="Issue", Urgency="Highly Important", Domain="IT", IssuerUserFileID=UserFile.objects.get(Username="JasonM"), RecipientUserFileID=UserFile.objects.get(Username="BobFitz"), StartDate=timezone.now(), EstimatedCompletionTime="2", EstimatedCompletionTimeUOM="Hours", PriorityInQueue=1.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub15 = Stub(Title="Submit Button", Overview="Submit button for profile page not working.", Category="Bug", Urgency="Highly Important", Domain="Development", IssuerUserFileID=UserFile.objects.get(Username="KellyNichols"), RecipientUserFileID=UserFile.objects.get(Username="BobFitz"), StartDate=timezone.now(), EstimatedCompletionTime="2", EstimatedCompletionTimeUOM="Hours", PriorityInQueue=1.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub16 = Stub(Title="PC Set Up", Overview="Carol in accounting needs help with setting up her PC", Category="Request", Urgency="When You Have Time", Domain="Accounting", IssuerUserFileID=UserFile.objects.get(Username="JasonM"), RecipientUserFileID=UserFile.objects.get(Username="BobFitz"), StartDate=timezone.now(), EstimatedCompletionTime="2", EstimatedCompletionTimeUOM="Hours", PriorityInQueue=1.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub17 = Stub(Title="Apperance Of Profile", Overview="Can we change the look of the profile page to match the other pages.", Category="Upgrade", Urgency="Important", Domain="Development", IssuerUserFileID=UserFile.objects.get(Username="JasonM"), RecipientUserFileID=UserFile.objects.get(Username="BobFitz"), StartDate=timezone.now(), EstimatedCompletionTime="2", EstimatedCompletionTimeUOM="Hours", PriorityInQueue=1.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub18 = Stub(Title="Stub Attachments", Overview="Stub attachments are not saving the uploaded content.", Category="Bug", Urgency="Highly Important", Domain="Development", IssuerUserFileID=UserFile.objects.get(Username="Arthur_T"), RecipientUserFileID=UserFile.objects.get(Username="BobFitz"), StartDate=timezone.now(), EstimatedCompletionTime="2", EstimatedCompletionTimeUOM="Hours", PriorityInQueue=1.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub19 = Stub(Title="Database Addition", Overview="Addition of project table to the DB.", Category="Suggestion", Urgency="Important", Domain="Development", IssuerUserFileID=UserFile.objects.get(Username="KellyNichols"), RecipientUserFileID=UserFile.objects.get(Username="BobFitz"), StartDate=timezone.now(), EstimatedCompletionTime="2", EstimatedCompletionTimeUOM="Hours", PriorityInQueue=1.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub20 = Stub(Title="Photo Required", Overview="Need company photo.", Category="Request", Urgency="Important", Domain="Marketing", IssuerUserFileID=UserFile.objects.get(Username="JasonM"), RecipientUserFileID=UserFile.objects.get(Username="BobFitz"), StartDate=timezone.now(), EstimatedCompletionTime="2", EstimatedCompletionTimeUOM="Hours", PriorityInQueue=1.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub21 = Stub(Title="Additional Employee Details", Overview="Some minor information required for finance department.", Category="Request", Urgency="Somewhat Important", Domain="Finance", IssuerUserFileID=UserFile.objects.get(Username="JasonM"), RecipientUserFileID=UserFile.objects.get(Username="BobFitz"), StartDate=timezone.now(), EstimatedCompletionTime="2", EstimatedCompletionTimeUOM="Hours", PriorityInQueue=1.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub22 = Stub(Title="Enlarge Text", Overview="Can the text be enlarged on the home page?", Category="Suggestion", Urgency="Somewhat Important", Domain="Development", IssuerUserFileID=UserFile.objects.get(Username="JasonM"), RecipientUserFileID=UserFile.objects.get(Username="BobFitz"), StartDate=timezone.now(), EstimatedCompletionTime="2", EstimatedCompletionTimeUOM="Hours", PriorityInQueue=1.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub23 = Stub(Title="Stub Categories", Overview="Category choices should be set for users.", Category="Request", Urgency="Highly Important", Domain="Development", IssuerUserFileID=UserFile.objects.get(Username="Arthur_T"), RecipientUserFileID=UserFile.objects.get(Username="BobFitz"), StartDate=timezone.now(), EstimatedCompletionTime="2", EstimatedCompletionTimeUOM="Hours", PriorityInQueue=1.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub24 = Stub(Title="Peripheral Order", Overview="Need to order more peripherals for employees.", Category="Suggestion", Urgency="Important", Domain="IT", IssuerUserFileID=UserFile.objects.get(Username="Arthur_T"), RecipientUserFileID=UserFile.objects.get(Username="BobFitz"), StartDate=timezone.now(), EstimatedCompletionTime="2", EstimatedCompletionTimeUOM="Hours", PriorityInQueue=1.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub25 = Stub(Title="Company Quarterly Review", Overview="Need report on company quarterly earnings.", Category="Request", Urgency="Important", Domain="Accounting", IssuerUserFileID=UserFile.objects.get(Username="BrettNes"), RecipientUserFileID=UserFile.objects.get(Username="BobFitz"), StartDate=timezone.now(), EstimatedCompletionTime="2", EstimatedCompletionTimeUOM="Hours", PriorityInQueue=1.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub26 = Stub(Title="Job Application", Overview="Review job application for potential prospect.", Category="Request", Urgency="Highly Important", Domain="Human Resource", IssuerUserFileID=UserFile.objects.get(Username="Arthur_T"), RecipientUserFileID=UserFile.objects.get(Username="JasonM"), StartDate=timezone.now(), EstimatedCompletionTime="2", EstimatedCompletionTimeUOM="Hours", PriorityInQueue=1.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub27 = Stub(Title="Push Rod Failure", Overview="Warped push rods need replacing.", Category="Issue", Urgency="Immediate", Domain="Mechanical Engineering", IssuerUserFileID=UserFile.objects.get(Username="BobFitz"), RecipientUserFileID=UserFile.objects.get(Username="BrettNes"), StartDate=timezone.now(), EstimatedCompletionTime="2", EstimatedCompletionTimeUOM="Hours", PriorityInQueue=1.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub28 = Stub(Title="Blown Head Gasket", Overview="Replace head gasket.", Category="Bug", Urgency="Important", Domain="Mechanical Engineering", IssuerUserFileID=UserFile.objects.get(Username="BobFitz"), RecipientUserFileID=UserFile.objects.get(Username="JasonM"), StartDate=timezone.now(), EstimatedCompletionTime="2", EstimatedCompletionTimeUOM="Hours", PriorityInQueue=1.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub29 = Stub(Title="Update Client Information", Overview="Client information needs updating.", Category="Request", Urgency="Highly Important", Domain="Accounting", IssuerUserFileID=UserFile.objects.get(Username="BobFitz"), RecipientUserFileID=UserFile.objects.get(Username="Arthur_T"), StartDate=timezone.now(), EstimatedCompletionTime="2", EstimatedCompletionTimeUOM="Hours", PriorityInQueue=1.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub30 = Stub(Title="Upcoming Meeting", Overview="Reminder for board meeting tonight at 6PM.", Category="Request", Urgency="Important", Domain="Marketing", IssuerUserFileID=UserFile.objects.get(Username="BobFitz"), RecipientUserFileID=UserFile.objects.get(Username="Arthur_T"), StartDate=timezone.now(), EstimatedCompletionTime="2", EstimatedCompletionTimeUOM="Hours", PriorityInQueue=1.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub31 = Stub(Title="Page Background Color", Overview="Changing the background color for the pages should be considered.", Category="Suggestion", Urgency="When You Have Time", Domain="Development", IssuerUserFileID=UserFile.objects.get(Username="BobFitz"), RecipientUserFileID=UserFile.objects.get(Username="JasonM"), StartDate=timezone.now(), EstimatedCompletionTime="2", EstimatedCompletionTimeUOM="Hours", PriorityInQueue=1.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newStub32 = Stub(Title="Add New Users", Overview="Make sure to create new user accounts for the new employees.", Category="Request", Urgency="Highly Important", Domain="IT", IssuerUserFileID=UserFile.objects.get(Username="BobFitz"), RecipientUserFileID=UserFile.objects.get(Username="KellyNichols"), StartDate=timezone.now(), EstimatedCompletionTime="2", EstimatedCompletionTimeUOM="Hours", PriorityInQueue=1.0, InProcess=False, Completed=False, CreationDate=timezone.now())

        newStub1.save()
        newStub2.save()
        newStub3.save()
        newStub4.save()
        newStub5.save()
        newStub6.save()
        newStub7.save()
        newStub8.save()
        newStub9.save()
        newStub10.save()
        newStub11.save()
        newStub12.save()
        newStub13.save()
        newStub14.save()
        newStub15.save()
        newStub16.save()
        newStub17.save()
        newStub18.save()
        newStub19.save()
        newStub20.save()
        newStub21.save()
        newStub22.save()
        newStub23.save()
        newStub24.save()
        newStub25.save()
        newStub26.save()
        newStub27.save()
        newStub28.save()
        newStub29.save()
        newStub30.save()
        newStub31.save()
        newStub32.save()

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

    def DatabaseRefreshWithTestData():
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

    def LogInSuccess_UpdateUserMeta(username, request):
        client_ip, is_routable = get_client_ip(request)
        user_obj = UserFile.objects.get(Username=username)
        usermeta_obj = UserMeta.objects.get(UserFileID=user_obj)
        usermeta_obj.LastLogInDate = timezone.now()
        usermeta_obj.LastIPAddress = client_ip
        usermeta_obj.save()

    def GetLoggedInUserObj(request):
        try:
            client_ip, is_routable = get_client_ip(request)
            usermeta_obj = UserMeta.objects.order_by('-LastLogInDate').filter(LastIPAddress=client_ip).first()
            timeSinceLastLogin = datetime.datetime.now(timezone.utc) - usermeta_obj.LastLogInDate
            if (timeSinceLastLogin.seconds//60) < 60:
                user_obj = UserFile.objects.get(id=usermeta_obj.UserFileID.pk)
                return user_obj
            return None
        except:
            return None
    
    def SignUserOut(request):
        user_obj = Backend.GetLoggedInUserObj(request)
        try:
            usermeta_obj = UserMeta.objects.get(UserFileID=user_obj)
            usermeta_obj.LastIPAddress = ""
            usermeta_obj.save()
        except:
            i = 0

    def GetNewLicenseString():
        newLicense = ""
        while (True):
            letters = string.ascii_letters + string.digits
            newLicense = ( ''.join(random.choice(letters) for i in range(10)) )
            checkLicenseCount = License.objects.filter(LicenseContent=newLicense).count()
            if checkLicenseCount == 0:
                break
            else:
                continue
        return newLicense
    
    def AddLicenseForMostRecentOrganizationRow(request):
        addedOrganization = Organization.objects.last()
        newLicenseString = Backend.GetNewLicenseString()
        newLicense = License(LicenseType="Organization", LicenseContent=newLicenseString)
        newLicense.save()
        addedOrganization.LicenseID = newLicense
        addedOrganization.save()
        return newLicenseString