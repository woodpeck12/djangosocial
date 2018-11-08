from django.shortcuts import render
from django.http import HttpResponse  #woodpeck
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


#customised login
from .forms import LoginForm
from django.contrib.auth.views import PasswordChangeView
from .forms import WoodPasswordChangeForm,WoodUserRegisterForm

# Create your views here.
class WoodChangePasswordView(PasswordChangeView):
    template_name = 'registration/djangopassword_change_form.html'
    form_class = WoodPasswordChangeForm





def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data

            user = authenticate(username=cleaned_data['username'],
                                password=cleaned_data['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('logined')
                else:
                    return HttpResponse('suspended')
            else:
                return HttpResponse('what are you doing')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})

def user_register(request):
    if request.method == 'POST':
        user_form = WoodUserRegisterForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,'account/user_success_register.html',{'new_user' : new_user})
    else:
        user_form = WoodUserRegisterForm()

    return render(request,'account/user_register_form.html',{'register_form': user_form})

@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',\
                    {'section' : 'dashboard'})
