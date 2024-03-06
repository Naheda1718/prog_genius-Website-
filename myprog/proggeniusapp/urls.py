from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('Android_Application/', views.service, name="service"),
    path('Web_Application/', views.webservice, name="webservice"),
    path('QA_Testing/', views.qatest, name="qatest"),
    path('About_US/', views.about, name="about"),
    path('Contact_US/', views.contact, name="contact"),
    path('UI/UX_Design/', views.uiux, name="uiux"),
    
]
