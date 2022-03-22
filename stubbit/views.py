
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
import time

def refresh(request):
    Backend.DatabaseRefreshWithTestData()
    return HttpResponse("Database Refresh Complete", content_type="text/plain")

def home(request):
    if (Backend.GetLoggedInUserObj(request) == None):
        return redirect('/login/')
    else:
        all_stubs = Stub.objects.all()
        loggedInUser = Backend.GetLoggedInUserObj(request)    
        stubs = None
        requestType = 'home'

        dict = {'stubs':stubs, 'requestType':requestType}
        return render(request, 'home_new.html', dict)

def home1(request):
    if (Backend.GetLoggedInUserObj(request) == None):
        return redirect('/login/')
    else:
        all_stubs = Stub.objects.all()
        loggedInUser = Backend.GetLoggedInUserObj(request)    
        stubs = None
        requestType = 'home1'
        
        try:        
            stubs = all_stubs.filter(InProcess=True, RecipientUserFileID=loggedInUser.pk)     
        except:
            stubs = None

        dict = {'stubs':stubs, 'requestType':requestType}
        return render(request, 'home_new.html', dict)

def home2(request):
    if (Backend.GetLoggedInUserObj(request) == None):
        return redirect('/login/')
    else:
        all_stubs = Stub.objects.all()
        loggedInUser = Backend.GetLoggedInUserObj(request)    
        stubs = None
        requestType = 'home2'
        
        try:        
            stubs = all_stubs.filter(RecipientUserFileID=loggedInUser.pk).order_by('-PriorityInQueue')       
        except:
            stubs = None

        dict = {'stubs':stubs, 'requestType':requestType}
        return render(request, 'home_new.html', dict)

def home3(request):
    if (Backend.GetLoggedInUserObj(request) == None):
        return redirect('/login/')
    else:
        all_stubs = Stub.objects.all()
        loggedInUser = Backend.GetLoggedInUserObj(request)    
        stubs = None
        requestType = 'home3'
        
        try:        
            stubs = all_stubs.filter(IssuerUserFileID=loggedInUser.pk).order_by('-PriorityInQueue')        
        except:
            stubs = None

        dict = {'stubs':stubs, 'requestType':requestType}
        return render(request, 'home_new.html', dict)

def home_old(request):
    if (Backend.GetLoggedInUserObj(request) == None):
        return redirect('/login/')
    else:
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
        if not Backend.Check_UserName_Availability(username):
            messages.error(request, "Username already taken")
        else:
            if password1 == password2:
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

def stubbitlogout(request):
    if (Backend.GetLoggedInUserObj(request) == None):
        return redirect('/login/')
    else:
        Backend.SignUserOut(request)
        messages.success(request, "Thank you for using Stubbit, you have been successfully logged out.")
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

def addOrganizationSuccess(request, context={}):
    messages.success(request, "Adding that Organization was successful! The generated license key for the organization is: " + License.objects.last().LicenseContent)
    return render(request, 'message_homeredirect.html')

def addStubSuccess(request):
    messages.success(request, "The Create Stub Operation was successful!")
    return render(request, 'message_homeredirect.html')

def profile(request):
    if (Backend.GetLoggedInUserObj(request) == None):
        return redirect('/login/')
    else:
        loggedInUser = Backend.GetLoggedInUserObj(request)
        context = {'loggedInUser':loggedInUser}
        return render(request,'profile.html', context)

def AddOrganization(request):
    if (Backend.GetLoggedInUserObj(request) == None):
        return redirect('/login/')
    else:
        form = OrganizationForm()
        if request.method == 'POST':
            form = OrganizationForm(request.POST)
            if form.is_valid():
                form.save()
                newLicense = Backend.AddLicenseForMostRecentOrganizationRow(request)
                return redirect('/addOrganization_message_homeredirect/')

        context = {'form':form}
        return render(request, 'organization.html', context)

def createstub(request):
    if (Backend.GetLoggedInUserObj(request) == None):
        return redirect('/login/')
    else:
        loggedInUser = Backend.GetLoggedInUserObj(request)
        allDevelopers = UserFile.objects.all()
        context = {'allDevelopers':allDevelopers}
        if (Backend.GetLoggedInUserObj(request) == None):
            return redirect('/login/')
        else:
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

def edit(request):
    if (Backend.GetLoggedInUserObj(request) == None):
        return redirect('/login/')
    else:
        global StubId
        if request.method == 'POST':
            StubId = request.POST['stubId']
        stub = Stub.objects.get(id=StubId)
        context = {'stub':stub}
        return render(request, 'edit.html', context)

def view(request):
    if (Backend.GetLoggedInUserObj(request) == None):
        return redirect('/login/')
    else:
        global StubId
        if request.method == 'POST':
            StubId = request.POST['stubId']
        stub = Stub.objects.get(id=StubId)
        context = {'stub':stub}
    return render(request, 'view.html', context)

def updatesuccess(request):
    global StubId
    stub = Stub.objects.get(id=StubId)
    if request.method == 'POST':
        inProcess = request.POST.get('inProcess')
        completed = request.POST.get('completed')
        if inProcess == None:
            inProcess = stub.InProcess
        if completed == None:
            completed = stub.Completed
        Stub.objects.filter(id=StubId).update(InProcess = inProcess)
        Stub.objects.filter(id=StubId).update(Completed = completed)
    messages.success(request, "Stub was successfully updated!")
    return render(request, 'updatesuccess.html')

def deletesuccess(request):
    global StubId
    stub = Stub.objects.get(id=StubId)
    stub.delete()
    messages.success(request, "Stub was successfully deleted!")
    return render(request, 'deletesuccess.html')

def about(request):
    return render(request, 'about.html')
