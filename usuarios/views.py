from django.shortcuts import render

# Create your views here.
def detalle_usuario(request):
    return render(request, 'usuarios/detalle_usuario.html', {} )

def login(request):
    return render(request, 'usuarios/login.html', {} )