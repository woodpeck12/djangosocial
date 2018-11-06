from django import forms

from django.contrib.auth.forms import (PasswordChangeForm)

class LoginForm(forms.Form):
    username = forms.CharField(label='User Name',required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password ',required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))


class WoodPasswordChangeForm(PasswordChangeForm):
    template_name='registration/djangopassword_change_form.html'
    old_password = forms.CharField(label='Old Password',required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label='New Password', required= True, widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password', required = True, widget=forms.PasswordInput(attrs={'class' : 'form-control'}))