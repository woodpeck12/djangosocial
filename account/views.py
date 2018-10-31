from django.shortcuts import render
from django.http import HttpResponse  #woodpeck
from django.contrib.auth import authenticate, login


#customised login
from .forms import LoginForm

# Create your views here.


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


