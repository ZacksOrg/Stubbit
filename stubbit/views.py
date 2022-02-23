from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate, logout
from .models import tbl_Authentication
from django.http import HttpResponse
from django.template import loader
from .models import *
from .backend import *

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
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

#Form for User Creation
from .forms import CreateUserForm


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

    all_stubs = Stub.objects.all()
    user = UserFile.objects.all()[0]
    dict = {'all_stubs':all_stubs, 'user_stubs':all_stubs.filter(IssuerUserFileID=user.pk)}
    return render(request, 'home.html', dict)
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST' :
        username = request.POST['username']
        email = request.POST['email_address']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        licenseKey = request.POST['license_key']
        developer = request.POST['developer']
#Database Username is a SQL Queries to see if it has been taken
        if username == "Database Username":
            messages.error(request, "Username already taken")
        else:
            if password1 == password2:
#All data needs to be taken and place into the Database here            
                return redirect('/login/')
                messages.success(request, "Your Account has been successfully created")
            else:
                return redirect('/signup/')
                messages.error(request, "Your passwords do not match!")
    return render(request, 'signup.html')
     
 
def login(request):
     
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
#SQL Query needed to search user tables for username and password
        if (username == "thomas") & (password == "apples"):
            return redirect('/')
        else:
            return redirect ('/login/')
    else:
        return render(request, 'login.html')



def profile(request):
    return render('profile.html')
