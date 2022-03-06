'''
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']


class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        labels = { "OrganizationName": "Organization Name",
                   "AddressCountry": "Country",
                   "AddressState": "State",
                   "AddressCity": "City",
                   "AddressZip": "Zip",
                   "AddressStreet": "Street",
                   "AddressBuildingNumber": "Building Number",
                   "PhoneNumber": "Phone Number"
                  }
        fields = ['OrganizationName','AddressCountry','AddressState','AddressCity','AddressZip','AddressStreet', 'AddressBuildingNumber', 'PhoneNumber']
        '''