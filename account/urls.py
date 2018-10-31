from django.urls import path
from .views import user_login

urlpatterns = [
    #this is login url
    path('login/',user_login,name='login'),
]