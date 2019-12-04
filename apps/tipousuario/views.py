from django.shortcuts import render
from rest_framework import generics
from .serializers import UsuarioSerializers, RolSerializers, AuthSerializers
from .models import Usuario, Rol, User
#from django.contrib.auth.models import User
# Create your views here.

class AuthApiList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = AuthSerializers

class UsuarioApiList(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializers

class RolApiList(generics.ListAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializers