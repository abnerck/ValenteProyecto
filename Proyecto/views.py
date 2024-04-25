from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from .Forms import *
from .models import *


# Create your views here.

def home(request):
    return render(request, 'home.html')

def create_user(request):
    
    if request.method == 'POST':
        # Si el formulario ha sido enviado, procesa los datos del formulario
        form = UsuarioForm(request.POST)
        if form.is_valid():
            # Guarda el usuario u realiza cualquier otra acción necesaria
            form.save()
            # Redirige a alguna página de éxito o a donde desees
            return redirect('home')  # Cambia 'home' al nombre de tu URL de inicio

    else:
        # Si el formulario no ha sido enviado, crea una instancia del formulario vacío
        form = UsuarioForm()

    # Renderiza la plantilla con el formulario como contexto
    return render(request, 'create_user.html', {'form': form})
    