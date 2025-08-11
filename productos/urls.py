from django.urls import path
from .views import home, about, ubicacion, lista_premium, lista_productos, detalle_producto, formulario_producto

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('ubicacion/', ubicacion, name='ubicacion'),
    path('productos/', lista_productos, name='lista_productos'),
    path('premium/', lista_premium, name='lista_premium'),
    path('producto/<int:pk>', detalle_producto, name='detalle_producto'),
    path('nuevo_producto/', formulario_producto, name='formulario_producto'),
    #path('', funcion, name=''),
]