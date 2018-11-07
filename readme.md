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
 2. views.py -create WoodPasswordChangeForm from forms.py
 ```
 # Create your views here.
class WoodChangePasswordView(PasswordChangeView):
    template_name = 'registration/djangopassword_change_form.html'
    form_class = WoodPasswordChangeForm


 ```
 3. linked to urls.py
 ```
 path('djangopasswordchange/',WoodChangePasswordView.as_view(),name='djangopasswordchange'),
 ```

 ### reutn passwordchange
 1. must use URL name as 'password_change_done'
 - cause after changing password, iDjango automatically find 'password_change_done' to reverse re-direct
 ```
 path('djangopasswordchangedone/',django_auth_view.PasswordChangeDoneView.as_view(template_name='registration/djangopasswordchangedone_form.html'),name='password_change_done'),
 ```

 ### customise password reset form
 1. add path into urls.py
```
path('djangopasswordreset/',django_auth_view.PasswordResetView.as_view(template_name='registration/djangopasswordreset_form.html'),name='djangopasswordreset'),
```
 2. for testing purpose add below at settings.py
 - pretend to send email and showing at console
 ```
 EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
 ```
 
 3. after run step 1, django call "password_reset_done"
 - it will show success sent email. but, if user doesn't have email, it will die silently

 4. When user grep link from recevied email
 - Django run "password_reset_confirm"
 - example received link: http://localhost:8000/account/djangopasswordresetconfirm/Mg/514-1dc6d5be843db93621a9/
 - URL format to process user link
 ```
 path('djangopasswordresetconfirm/<uidb64>/<token>/', django_auth_view.PasswordResetConfirmView.as_view(template_name='registration/djangopasswordresetconfirm.html'), name='password_reset_confirm'),
```

### make user creation