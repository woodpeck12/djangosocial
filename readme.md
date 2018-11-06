## 1-11-2018 : testing git kraken

## 1-11-2018 using django original login form

### @login_required   --- it required "from django.contrib.auth.decorators import login_required"
 if fail to authentication, it redirect to login. to customise where it goes, need to add LOGIN_URL at `setting.py`
 LOGIN_URL = 'djangologin'

### customise passwordchangeform
1. forms.py - from django.contrib.auth.forms import (PasswordChangeForm)
```
class WoodPasswordChangeForm(PasswordChangeForm):
    template_name='registration/djangopassword_change_form.html'
    old_password = forms.CharField(label='Old Password',required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label='New Password', required= True, widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password', required = True, widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
 ```
 