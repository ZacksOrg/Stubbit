
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate, logout
from django.http import HttpResponse
from django.template import loader
from .models import *
from .backend import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, OrganizationForm
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
    user = UserFile.objects.all()[0]
    stub_inprocess = Stub.objects.filter(InProcess=True).get(RecipientUserFileID=user.pk)
    dict = {'all_stubs':all_stubs, 'user_stubs':all_stubs.filter(IssuerUserFileID=user.pk), 'stub_inprocess':stub_inprocess}
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
            return redirect('/loginwelcome/')
        else:
            messages.error(request, "Incorrect Credentials! Please makes sure your username and password are correct!")
            return redirect ('/login/')
    else:
        return render(request, 'login.html')

def loginwelcome(request):       
    messages.success(request, "Welcome to Stubbit!")
    return render(request, 'loginwelcome.html')



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
            return redirect('/')
    
    context = {'form':form}
    return render(request, 'organization.html', context)
 
def createstub(request):
    if request.method == 'POST' :
        stubtitle = request.POST['stubTitle']
        stuboverview = request.Post['stubOverview']
        stubcategory = request.Post['StubCategory']
        stuburgency = request.POST['stubUrgency']
        stubdomain = request.POST['stubDomain']
        attachments = request.POST['attachments']
        developer = request.POST['developer']
        newstub = Stub(Title=stubtitle, Overview=stuboverview, Category=stubcategory, Urgency=stuburgency, Domain=stubdomain, IssuerUserFileID=UserFile.objects.get(Username=Backend.Retrieve_CurrentUser_Username()), RecipientUserFileID=UserFile.objects.get(Username=developer), StartDate=timezone.now(), EstimatedCompletionTime="1", EstimatedCompletionTimeUOM="Days", PriorityInQueue=1.0, InProcess=True, Completed=False, CreationDate=timezone.now())
    return render(request, 'createstub.html')