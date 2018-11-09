## 1-11-2018 : testing git kraken

## 1-11-2018 using django original login form

### @login_required   --- it required "from django.contrib.auth.decorators import login_required"
 if fail to authentication, it redirect to login. to customise where it goes, need to add LOGIN_URL at `setting.py`
 LOGIN_URL = 'djangologin'

### customise passwordchangeform
1. forms.py - from django.contrib.auth.forms import (PasswordChangeForm)
```python
class WoodPasswordChangeForm(PasswordChangeForm):
    template_name='registration/djangopassword_change_form.html'
    old_password = forms.CharField(label='Old Password',required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label='New Password', required= True, widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password', required = True, widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
 ```
 2. views.py -create WoodPasswordChangeForm from forms.py
 ```python
 # Create your views here.
class WoodChangePasswordView(PasswordChangeView):
    template_name = 'registration/djangopassword_change_form.html'
    form_class = WoodPasswordChangeForm


 ```
 3. linked to urls.py
 ```python
 path('djangopasswordchange/',WoodChangePasswordView.as_view(),name='djangopasswordchange'),
 ```

 ### reutn passwordchange
 1. must use URL name as 'password_change_done'
 - cause after changing password, iDjango automatically find 'password_change_done' to reverse re-direct
 ```python
 path('djangopasswordchangedone/',django_auth_view.PasswordChangeDoneView.as_view(template_name='registration/djangopasswordchangedone_form.html'),name='password_change_done'),
 ```

 ### customise password reset form
 1. add path into urls.py
```python
path('djangopasswordreset/',django_auth_view.PasswordResetView.as_view(template_name='registration/djangopasswordreset_form.html'),name='djangopasswordreset'),
```
 2. for testing purpose add below at settings.py
 - pretend to send email and showing at console
 ```python
 EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
 ```
 
 3. after run step 1, django call "password_reset_done"
 - it will show success sent email. but, if user doesn't have email, it will die silently

 4. When user grep link from recevied email
 - Django run "password_reset_confirm"
 - example received link: http://localhost:8000/account/djangopasswordresetconfirm/Mg/514-1dc6d5be843db93621a9/
 - URL format to process user link
```python
 path('djangopasswordresetconfirm/<uidb64>/<token>/', django_auth_view.PasswordResetConfirmView.as_view(template_name='registration/djangopasswordresetconfirm.html'), name='password_reset_confirm'),
```

### make user creation
1. when save password from form, use set_passwrd('received password') for django do encryption
2. User modeform is the easiest way
```python
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
```

### how to customise Django User model
1. create Class inheritance from User
- setting.AUTH_USER_MODEL is better than get_user()--why??? without fail, can get User
```python
class WoodUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete='cascade')
    dob = models.DateField(blank=True,null=True)

    def __str__(self):
        return 'Wooduser for user class is {}'.format(self.user.username)
```
2. create form to linked expand User model
```python
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class WoodUserEditForm(forms.ModelForm):
    class Meta:
        model = WoodUser
        fields = ('dob',)
```

3. create coneection two formd at views.py
```python
        edituserform = UserEditForm(instance=request.user, data=request.POST)
        editwooduserform = WoodUserEditForm(instance=request.user.wooduser,data=request.POST)
``` 

### message handling
1. it must be included at settings.py INSTALLED_APP ==== django.contrib.messages
2. Also, another middleware must be in settings.py 
- 'django.contrib.messages.middleware.MessageMiddleware'
3. how to use --- views.py 
- put error message as below:
```python
from django.contrib import messages
messages.error(request, 'Something went wrong')
```

-- retrieve message as below:
```html
{% if messages %}
<ul class="messages">
{% for message in messages %}
<li class="{{ message.tags }}">
{{ message|safe }}
<a href="#" class="close">✖</a>
</li>
{% endfor %}
</ul>
{% endif %}
```

### Divert User authentication handling
1. AUTHENTICATION_BACKENDS = (django.contrib.auth.backends.ModelBackend) handle general Authetication using UserID and password
2. try to login with Email also.
```python
from django.contrib.auth.models import User

class EmailAuthenticationProcessBackend(object):
    # using email to check user

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email = username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

AUTHENTICATION_BACKENDS = [
'django.contrib.auth.backends.ModelBackend',
'account.emailauthentication.EmailAuthenticationProcessBackend',
]
```

### how to add social media authentication
step 1: install module : pip install python-social-auth and pip install social-auth-app-django
step 2: add above module to INSTALLED_APPS = {'social_django',}
step 3: python manage.py migrates  --- it create all social account related databse
step 4: add AUTHENTICATION_BACKENDS = [
'django.contrib.auth.backends.ModelBackend',
'social_core.backends.facebook.FacebookOAuth2',
'social_core.backends.twitter.TwitterOAuth',
'social_core.backends.google.GoogleOAuth2',
]



https://simpleisbetterthancomplex.com/tutorial/2016/10/24/how-to-add-social-login-to-django.html