from django.db import models
from django.contrib import admin

# Create your models here.

class UserTable(models.Model):
   id = models.AutoField(max_length = 100 , primary_key = True);
   username = models.CharField(max_length = 100);
   heading = models.CharField(max_length = 100);
   pwd = models.CharField(max_length = 100);
   registetime = models.DateTimeField(auto_now_add=True);
   issudit = models.BooleanField(default = True);
   phone = models.IntegerField();
# @admin.site.register(rootinfo)
# class root(admin.ModelAdmin):
#   usernme = models.CharField(max_length = 20 , primary_key = True);
#   pwd = models.CharField(max_length = 20);









