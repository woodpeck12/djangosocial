from django.contrib import admin

# Register your models here.
from .models import WoodUser

class WoodUserAdmin(admin.ModelAdmin):
    list_display = ['user','dob']
    pass
admin.site.register(WoodUser,WoodUserAdmin)

