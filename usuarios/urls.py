from django.urls import path
from .views import login, detalle_usuario

urlpatterns = [
    path('login/', login, name='login'),
    path('usuario/<int:pk>', detalle_usuario, name='detalle_usuario'),
    #path('', funcion, name=),
]