from rest_framework import viewsets, filters, permissions
from .models import Usuario, User, Rol
from .serializers import UsuarioSerializers, AuthSerializers, RolSerializers
from .serializers import RolHySerializers, AuthHySerializers, UsuarioHySerializers

#Model Serializers
class AuthViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AuthSerializers

class UsuarioViewSets(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializers

class RolViewSets(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializers

#HyperlinkedModelSerializers
class RolHypViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolHySerializers

class AuthHypViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AuthHySerializers

class UsuarioHypViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioHySerializers