from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','password1','email','password2']

    # def __str__(self):
    #     return self.us\\


class UpdateUser(forms.ModelForm):
    pass 
