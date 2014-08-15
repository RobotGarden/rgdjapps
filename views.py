from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django import forms
from models import *

class WaiverForm(forms.ModelForm):
    "A form for submitting waivers"
    class Meta:
        model = RGUser
        fields = ['name', 'email', 'address', 'zip_code', 'emergency_contact', 'emergency_care', 'url']
