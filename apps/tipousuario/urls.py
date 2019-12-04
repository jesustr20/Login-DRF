from django.urls import path, include
from rest_framework import routers
from .views import AuthApiList, RolApiList, UsuarioApiList
from .viewsets import AuthViewSets, RolViewSets, UsuarioViewSets
from .viewsets import RolHypViewSet, AuthHypViewSet, UsuarioHypViewSet

#ListApiViews - view
'''
urlpatterns = [
    path('usuarios/', UsuarioApiList.as_view()),
    path('auth/', AuthApiList.as_view()),
    path('rol/', RolApiList.as_view()),
]
'''

#ModelViewSets - Viewsets
router = routers.DefaultRouter()
'''
router.register(r'usuarios', UsuarioViewSets)
router.register(r'auth', AuthViewSets)
router.register(r'rol', RolViewSets)
'''
#HYPERLINKEDSERIALIZER - viewsets
router.register(r'rolv2', RolHypViewSet)
router.register(r'authv2', AuthHypViewSet)
router.register(r'usuariov2', UsuarioHypViewSet)

urlpatterns = [
    path('', include(router.urls))
]

