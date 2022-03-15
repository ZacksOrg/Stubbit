
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate, logout
from django.http import HttpResponse
from django.template import loader
from .models import *
from .backend import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, OrganizationForm

from django.contrib.messages import *

from .forms import CreateUserForm
from django.contrib import messages

def index(request):
    outputHTTP_string = ""

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

    outputHTTP_string = Backend.PrintLicenses() + "\n\n\n" + Backend.PrintOrganizations() + "\n\n\n" + Backend.PrintUsers() + "\n\n\n" + Backend.PrintUserPasses() + "\n\n\n" + Backend.PrintUserMetas() + "\n\n\n" + Backend.PrintStubs() + "\n\n\n" + Backend.PrintStubAttachments()

    return HttpResponse(outputHTTP_string, content_type="text/plain")

def home(request):

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

from django.contrib import messages
import time

def refresh(request):
    Backend.DatabaseRefreshWithTestData()
    return HttpResponse("Database Refresh Complete", content_type="text/plain")

def index(request):
    outputHTTP_string = ""
    outputHTTP_string = Backend.PrintLicenses() + "\n\n\n" + Backend.PrintOrganizations() + "\n\n\n" + Backend.PrintUsers() + "\n\n\n" + Backend.PrintUserPasses() + "\n\n\n" + Backend.PrintUserMetas() + "\n\n\n" + Backend.PrintStubs() + "\n\n\n" + Backend.PrintStubAttachments()
    return HttpResponse(outputHTTP_string, content_type="text/plain")

def home(request):
    all_stubs = Stub.objects.all()
    loggedInUser = Backend.GetLoggedInUserObj(request)    
    stub_inprocess = None
    received_stubs = None
    sent_stubs = None
    
    try:        
        stub_inprocess = all_stubs.filter(InProcess=True).get(RecipientUserFileID=loggedInUser.pk)
    except:
        stub_inprocess = None
        
    try:        
        received_stubs = all_stubs.filter(RecipientUserFileID=loggedInUser.pk)
    except:
        received_stubs = None
        
    try:        
        sent_stubs = all_stubs.filter(IssuerUserFileID=loggedInUser.pk)
    except:
        sent_stubs = None
    dict = {'received_stubs':received_stubs, 'sent_stubs':sent_stubs, 'stub_inprocess':stub_inprocess}
    return render(request, 'home.html', dict)

def signup(request):
    if request.method == 'POST' :
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email_address']
        password2 = request.POST['password2']
        password1 = request.POST['password1']
        licenseKey = request.POST['license_key']
        department = request.POST['department']
#Database Username is a SQL Queries to see if it has been taken
        if not Backend.Check_UserName_Availability(username):
            messages.error(request, "Username already taken")
        else:
            if password1 == password2:
#All data needs to be taken and place into the Database here
                try:
                    licenseValue = License.objects.get(LicenseContent=licenseKey)
                except Exception as identifier:
                    messages.error(request, "You did not enter a valid license kay!")
                    return redirect('/signup/')
                organization = Organization.objects.get(LicenseID=licenseValue.pk)
                newUser = UserFile(Username=username, FirstName=firstname, LastName=lastname, Email=email, OrganizationID=organization, Department=department, Administrator=False)
                newUser.save()
                newUserPass = UserPass(UserFileID=newUser, EncryptedPassword=password2, EncrpytionMethod="AES-ECB-128", EncryptionKey="1234567890123456")
                newUserPass.save()
                newUserMeta = UserMeta(UserFileID=newUser, AccountCreationDate=timezone.now())
                newUserMeta.save()
                return redirect('/signupsuccess/')
            else:
                messages.error(request, "Your passwords do not match!")
                return redirect('/signup/')
    return render(request, 'signup.html')

def signupsuccess(request):
    messages.success(request, "You have signed up successfully!")
    return render(request, 'signupsuccess.html')

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if Backend.Authentication(username, password) == True:
            user = UserFile.objects.get(Username=username)
            Backend.LogInSuccess_UpdateUserMeta(username, request)
            return redirect('/login_message_homeredirect/')
        else:
            messages.error(request, "Incorrect Credentials! Please makes sure your username and password are correct!")
            return redirect ('/login/')
    else:
        return render(request, 'login.html')

def loginwelcome(request):
    messages.success(request, "Your credentials were authenticated successfully. Welcome to Stubbit!")
    return render(request, 'message_homeredirect.html')

def addOrganizationSuccess(request):
    messages.success(request, "Adding that Organization was successful!")
    return render(request, 'message_homeredirect.html')

def addStubSuccess(request):
    messages.success(request, "The Create Stub Operation was successful!")
    return render(request, 'message_homeredirect.html')

def profile(request):
    loggedInUser = Backend.GetLoggedInUserObj(request)
    context = {'loggedInUser':loggedInUser}
    return render(request,'profile.html', context)

def AddOrganization(request):
    form = OrganizationForm()
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            Backend.AddLicenseForMostRecentOrganizationRow(request)
            return redirect('/addOrganization_message_homeredirect/')

    context = {'form':form}
    return render(request, 'organization.html', context)

def createstub(request):
    loggedInUser = Backend.GetLoggedInUserObj(request)
    allDevelopers = UserFile.objects.all()
    context = {'allDevelopers':allDevelopers}
    if request.method == 'POST' :
        stubtitle = request.POST['stubTitle']
        stuboverview = request.POST['stubOverview']
        stubcategory = request.POST['stubCategory']
        stuburgency = request.POST['stubUrgency']
        stubdomain = request.POST['stubDomain']
        developer = request.POST['developer']
        dev = UserFile.objects.get(Username=developer)
        newstub = Stub(Title=stubtitle, Overview=stuboverview, Category=stubcategory, Urgency=stuburgency, Domain=stubdomain, IssuerUserFileID_id=loggedInUser.pk, RecipientUserFileID_id=dev.pk, StartDate=timezone.now(), EstimatedCompletionTime="1", EstimatedCompletionTimeUOM="Days", PriorityInQueue=1.0, InProcess=False, Completed=False, CreationDate=timezone.now())
        newstub.save()
        return redirect('/createStub_message_homeredirect/')
    return render(request, 'createstub.html', context)
