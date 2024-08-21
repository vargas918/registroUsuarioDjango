from django.urls import path
from .views import registerUser, listarUsuarios


urlpatterns = [
    path('registrar/', registerUser, name='registerUser'),
    path('',listarUsuarios,name='listarUsuarios')
]
