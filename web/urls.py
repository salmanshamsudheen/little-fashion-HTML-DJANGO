from django.urls import path
from . import views

app_name = 'web'       # registering web in url    used when include is used in main url 

urlpatterns = [
    path('', views.index, name='index'),
    path('story/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),                  #name is used to get from html page
    path('faq/', views.faq, name='faq'), 
    path('contact-submit/', views.contact_view, name='contact_form')
]