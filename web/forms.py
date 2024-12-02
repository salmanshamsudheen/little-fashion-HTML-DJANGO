from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):             
    class Meta:                            #dont need to add contact.object. create in views.py for save to database
        model = Contact
        fields = ['name', 'email', 'subject', 'detail']     
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-floating form-control',}),                   #to add class
            'email': forms.EmailInput(attrs={'class': 'form-control',}),
            'subject': forms.TextInput(attrs={'class': 'form-control',}), 
            'detail': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 110px;',}),           
        } 
        
        
