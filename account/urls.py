from django.urls import path
from . import views
from  django.contrib.auth import views as django_auth_view

urlpatterns = [
    #this is login url
    path('login/',views.user_login,name='login'),
    path('djangologin/',django_auth_view.LoginView.as_view(),name='djangologin'),
    path('djangologout/',django_auth_view.LogoutView.as_view(),name='djangologout'),
    path('djangologoutin/',django_auth_view.logout_then_login,name='djangologoutin'),
]

