from django.db import models

# Create your models here.

class UserTable(models.Models):
    id = models.CharField(max_length = 100 , primary_key = True);
    username = models.CharField(max_length = 100);
    heading = models.CharField(max_length = 100);
    pwd = models.CharField(max_length = 100);
    registetime = models.DateTimeField(auto_now_add=True);
    issudit = models.BooleanField(default = True);
    phone = models.IntegerField(max_length=11);


