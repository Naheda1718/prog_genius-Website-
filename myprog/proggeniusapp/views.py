from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings

from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'Android_development.html')

def webservice(request):
    return render(request, 'web_application.html')

def qatest(request):
    return render(request, 'software_testing.html')

def about(request):
    return render(request, 'about-us.html')

def contact(request):
        return render(request, 'contact-us.html')
def uiux(request):
        return render(request, 'Uiux.html')


