from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import (PasswordChangeForm)

class LoginForm(forms.Form):
    username = forms.CharField(label='User Name',required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password ',required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))


class WoodPasswordChangeForm(PasswordChangeForm):
    #template_name='registration/djangopassword_change_form.html'
    old_password = forms.CharField(label='Old Password',required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label='New Password', required= True, widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password', required = True, widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

class WoodUserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password',required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Repeat Password',required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','email')

    def clean_password1(self):
        form_clean_data = self.cleaned_data

        if form_clean_data['password'] != form_clean_data['password1']:
            raise forms.ValidationError('Password doesn\'t match')

        return form_clean_data['password1']