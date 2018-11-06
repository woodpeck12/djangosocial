from django.urls import path
from . import views
from .views import WoodChangePasswordView
from  django.contrib.auth import views as django_auth_view

urlpatterns = [
    #this is login url
    path('login/',views.user_login,name='login'),
    #the below is django login
    path('djangologin/',django_auth_view.LoginView.as_view(),name='djangologin'),
    path('djangologout/',django_auth_view.LogoutView.as_view(),name='djangologout'),
    path('djangopasswordchange/',WoodChangePasswordView.as_view(),name='djangopasswordchange'),
    path('djangopasswordchangedone/',django_auth_view.PasswordChangeDoneView.as_view(template_name='registration/djangopasswordchangedone_form.html'),name='password_change_done'),
    #the below is django password reset
    path('djangopasswordreset/',django_auth_view.PasswordResetView.as_view(template_name='registration/djangopasswordreset_form.html'),name='djangopasswordreset'),

    path('',views.dashboard,name='dashboard'),

]

