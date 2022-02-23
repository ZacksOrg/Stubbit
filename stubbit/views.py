from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
# Create your views here.
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
    
    Backend.CreateTestLicense()
    Backend.CreateTestOrganization()
    Backend.CreateTestUser()
    Backend.CreateTestUserPass()
    Backend.CreateTestUserMeta()
    Backend.CreateTestStub()
    Backend.CreateTestStubAttachment()
    
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
    
    Backend.CreateTestLicense()
    Backend.CreateTestOrganization()
    Backend.CreateTestUser()
    Backend.CreateTestUserPass()
    Backend.CreateTestUserMeta()
    Backend.CreateTestStub()
    Backend.CreateTestStubAttachment()

    all_stubs = Stub.objects.all()
    user = UserFile.objects.all()[0]
    dict = {'all_stubs':all_stubs, 'user_stubs':all_stubs}
    return render(request, 'home.html', dict)
