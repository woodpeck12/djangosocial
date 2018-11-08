from django.db import models

# Create your models here.
from django.conf import settings

class WoodUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete='cascade')
    dob = models.DateField(blank=True,null=True)

    def __str__(self):
        return 'Wooduser for user class is {}'.format(self.user.username)