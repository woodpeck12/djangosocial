from django.contrib import admin

# Register your models here.
from .models import WoodUser

class WoodUserAdmin(admin.ModelAdmin):
    pass
admin.site.register(WoodUser,WoodUserAdmin)

