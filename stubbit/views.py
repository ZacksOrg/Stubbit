from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
# Create your views here.

def home(request):

    all_stubs = Stub.objects.all()
    user = Account.objects.get(pk=1)
    user_stubs = user.stub_set.all()
    dict = {'all_stubs':all_stubs, 'user_stubs':user_stubs}
    return render(request, 'home.html', dict)
