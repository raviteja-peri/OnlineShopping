from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import models

User=get_user_model()

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label='Username'
        self.fields['email'].label='Email Address'

    def clean_email(self):
        email=self.cleaned_data['email']
        count=User.objects.filter(email=email).count()
        if count>0:
            raise forms.ValidationError("This user has already been registered please check the email")
        elif count==0:
            return email
