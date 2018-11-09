from django.shortcuts import render
from django.http import HttpResponse  #woodpeck
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


#customised login
from .forms import LoginForm
from django.contrib.auth.views import PasswordChangeView
from .models import WoodUser
from .forms import (WoodPasswordChangeForm,
                    WoodUserRegisterForm,
                    UserEditForm,
                    WoodUserEditForm)

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

            #add this to add extra dob field from  wooduser model
            wooduser = WoodUser.objects.create(user=new_user)

            return render(request,'account/user_success_register.html',{'new_user' : new_user})
    else:
        user_form = WoodUserRegisterForm()

    return render(request,'account/user_register_form.html',{'register_form': user_form})

@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',\
                    {'section' : 'dashboard'})
@login_required
def editwooduser(request):
    if request.method == POST:
        edituserform = UserEditForm(instance=request.user, data=request.POST)
        editwooduserform = WoodUserEditForm(instance=request.user.wooduser,data=request.POST)

        if edituserform.is_valid() and editwooduserform.is_valid():
            edituserform.save()
            editwooduserform.save()
        else:
            edituserform = UserEditForm(instance=request.user)
            editwooduserform = WoodUserEditForm(instance=request.user.wooduser)

        return render(request,'account/wooduseredit.html',{'edituserform':edituserform,'editwoouserform':editwooduserform})

