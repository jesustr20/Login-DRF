from rest_framework import serializers
from .models import Usuario, Rol, User
#from django.contrib.auth.models import User

#MODEL SERIALIZERS

class AuthSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']

class RolSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id','rol']   

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','user', 'age', 'rol', 'location']

#HIPERLINKEDSERIALIZERS
class AuthHySerializers(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='rol-detail')
    #url = serializers.HyperlinkedIdentityField(read_only=True, view_name='user-detail')
    class Meta:
        model = User
        fields = ['id', 'username', 'password','email', 'url']

class RolHySerializers(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='rol-detail')
    #url = serializers.HyperlinkedIdentityField(read_only=True, view_name='user-detail')
    class Meta:
        model = Rol
        fields = ['id','rol','url']

class UsuarioHySerializers(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='rol-detail')
    #url = serializers.HyperlinkedIdentityField(read_only=True, view_name='user-detail')
    #rol = RolHySerializers(many=True, read_only=True)
    rol = RolHySerializers()
    user = AuthHySerializers()
    class Meta:
        model = Usuario
        fields = ['id','user','rol','location','age','url']