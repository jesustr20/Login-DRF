from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=8)

    def __str__(self):
        return f'{self.rol}'

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    age = models.IntegerField()
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'
        