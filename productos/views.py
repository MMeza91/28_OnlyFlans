from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'componentes/home.html', {} )

def about(request):
    return render(request, 'componentes/about.html', {} )

def ubicacion(request):
    return render(request, 'componentes/ubicacion.html', {} )

def lista_productos(request):
    return render(request, 'productos/lista_productos.html', {} )

def lista_premium(request):
    return render(request, 'productos/lista_premium.html', {} )

def detalle_producto(request):
    return render(request, 'productos/detalle_producto.html', {} )

def formulario_producto(request):
    return render(request, 'productos/formulario_producto.html', {} )