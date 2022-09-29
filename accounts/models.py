from django.db import models
from django.contrib import auth

# Create your models here.
class User(auth.model.User,auth.models.PermissionMixin):
    def __str__(self):
          return str(self.username)