from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from .Forms import *
from .models import *

from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def ProgramasEducativo(request):
    programa = programaEducativo.objects.all()
    return render(request, 'programaeducativo.html', {'programa': programa})

from django.contrib import messages

def create_programaeducativo(request):
    if request.method == 'POST':
        form = ProgramaEducativoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El programa educativo se ha creado correctamente.')
            return redirect('programaeducativo')
        else:
            messages.error(request, 'Ha ocurrido un error al intentar crear el programa educativo. Por favor, verifica los datos ingresados.')
    else:
        form = ProgramaEducativoForm()
    
    return render(request, 'create_programaeducativo.html', {'form': form})


def delete_programaEducativo(request, programa_id):
    programas = get_object_or_404(programaEducativo, pk=programa_id)
    programas.delete()
    return redirect(reverse('programaeducativo'))

def update_programaEducativo(request, programa_id):
    programas = get_object_or_404(programaEducativo, pk=programa_id)
    if request.method == 'POST':
        form = ProgramaEducativoForm(request.POST, instance=programas)
        if form.is_valid():
            form.save()
            # Redireccionar a alguna página de éxito o mostrar un mensaje de éxito
            return redirect('programaeducativo')
    else:
        form = ProgramaEducativoForm(instance=programas)
    return render(request, 'update_programaeducativo.html', {'form': form})



def Users(request):
    usuarios = Usuario.objects.all()

    return render(request, 'usuarios.html', {'usuarios': usuarios})

def create_user(request):
    
    if request.method == 'POST':
        # Si el formulario ha sido enviado, procesa los datos del formulario
        form = UsuarioForm(request.POST)
        if form.is_valid():
            # Guarda el usuario u realiza cualquier otra acción necesaria
            form.save()
            # Redirige a alguna página de éxito o a donde desees
            return redirect('usuarios')  # Cambia 'home' al nombre de tu URL de inicio

    else:
        # Si el formulario no ha sido enviado, crea una instancia del formulario vacío
        form = UsuarioForm()

    # Renderiza la plantilla con el formulario como contexto
    return render(request, 'create_user.html', {'form': form})

def delete_user(request, user_id):
    usuario = get_object_or_404(Usuario, pk=user_id)
    usuario.delete()
    return redirect(reverse('usuarios'))



def update_user(request, user_id):
    usuario = get_object_or_404(Usuario, pk=user_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            # Redireccionar a alguna página de éxito o mostrar un mensaje de éxito
            return redirect('usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'update_user.html', {'form': form})


# ASIGNATURAS
def asignaturas(request):
    asignatura = Asignatura.objects.all()
    return render(request, 'asignaturas.html', {'asignatura': asignatura})

def create_asignatura(request):

    if request.method == 'POST':
        # Si el formulario ha sido enviado, procesa los datos del formulario
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            # Guarda el usuario u realiza cualquier otra acción necesaria
            form.save()
            # Redirige a alguna página de éxito o a donde desees
            return redirect('asignaturas')  # Cambia 'home' al nombre de tu URL de inicio

    else:
        # Si el formulario no ha sido enviado, crea una instancia del formulario vacío
        form = AsignaturaForm()

    # Renderiza la plantilla con el formulario como contexto
    return render(request, 'create_asignatura.html', {'form': form})

def delete_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, pk=asignatura_id)
    asignatura.delete()
    return redirect(reverse('asignaturas'))

def update_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, pk=asignatura_id)
    if request.method == 'POST':
        form = AsignaturaForm(request.POST, instance=asignatura)
        if form.is_valid():
            form.save()
            # Redireccionar a alguna página de éxito o mostrar un mensaje de éxito
            return redirect('asignatura')
    else:
        form = AsignaturaForm(instance=asignatura)
    return render(request, 'update_asignatura.html', {'form': form})

def curso(request):
    curso = Curso.objects.all()
    return render(request, 'cursos.html', {'curso': curso})

def create_curso(request):

    asignaturas = Asignatura.objects.all()
    grupos = Grupo.objects.all()
    if request.method == 'POST':
        # Si el formulario ha sido enviado, procesa los datos del formulario
        form = CursoForm(request.POST)
        if form.is_valid():
            # Guarda el usuario u realiza cualquier otra acción necesaria
            form.save()
            # Redirige a alguna página de éxito o a donde desees
            return redirect('cursos')  # Cambia 'home' al nombre de tu URL de inicio

    else:
        # Si el formulario no ha sido enviado, crea una instancia del formulario vacío
        form = CursoForm()
        

    # Renderiza la plantilla con el formulario como contexto
    
    return render(request, 'create_curso.html', {'form': form,'asignaturas':asignaturas,'grupos':grupos})

    
def delete_curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    curso.delete()
    return redirect(reverse('cursos'))

def update_curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            # Redireccionar a alguna página de éxito o mostrar un mensaje de éxito
            return redirect('cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'update_curso.html', {'form': form})

    # EVIDENCIA

def evidencia(request):
    evidencia = Evidencia.objects.all()
    return render(request, 'evidencias.html', {'evidencia': evidencia})

def create_evidencia(request):
    
    if request.method == 'POST':
        # Si el formulario ha sido enviado, procesa los datos del formulario
        form = EvidenciaForm(request.POST)
        if form.is_valid():
            # Guarda el usuario u realiza cualquier otra acción necesaria
            form.save()
            # Redirige a alguna página de éxito o a donde desees
            return redirect('evidencias')  # Cambia 'home' al nombre de tu URL de inicio

    else:
        # Si el formulario no ha sido enviado, crea una instancia del formulario vacío
        form = Evidencia()

    # Renderiza la plantilla con el formulario como contexto
    return render(request, 'create_evidencia.html', {'form': form})




def delete_evidencia(request, evidencia_id):
    evidencia = get_object_or_404(Evidencia, pk=evidencia_id)
    evidencia.delete()
    return redirect(reverse('evidencias'))

def update_evidencia(request, evidencia_id):
    evidencia = get_object_or_404(Evidencia, pk=evidencia_id)
    if request.method == 'POST':
        form = EvidenciaForm(request.POST, instance=evidencia)
        if form.is_valid():
            form.save()
            # Redireccionar a alguna página de éxito o mostrar un mensaje de éxito
            return redirect('evidencias')
    else:
        form = AsignaturaForm(instance=evidencia)
    return render(request, 'update_evidencia.html', {'form': form})


#GRUPO

def grupos(request):
    grupos = Grupo.objects.all()

    return render(request, 'grupos.html', {'grupos': grupos})

def create_grupo(request):
    
    if request.method == 'POST':
        # Si el formulario ha sido enviado, procesa los datos del formulario
        form = GrupoForm(request.POST)
        if form.is_valid():
            # Guarda el usuario u realiza cualquier otra acción necesaria
            form.save()
            # Redirige a alguna página de éxito o a donde desees
            return redirect('grupos')  # Cambia 'home' al nombre de tu URL de inicio

    else:
        # Si el formulario no ha sido enviado, crea una instancia del formulario vacío
        form = GrupoForm()

    # Renderiza la plantilla con el formulario como contexto
    return render(request, 'create_grupo.html', {'form': form})

def delete_grupo(request, grupo_id):
    grupos = get_object_or_404(Grupo, pk=grupo_id)
    grupos.delete()
    return redirect(reverse('grupos'))




def update_grupo(request, grupo_id):
    grupo = get_object_or_404(Grupo, pk=grupo_id)
    if request.method == 'POST':
        form = GrupoForm(request.POST, instance=grupo)
        if form.is_valid():
            form.save()
            # Redireccionar a alguna página de éxito o mostrar un mensaje de éxito
            return redirect('grupos')
    else:
        form = GrupoForm(instance=grupo)
    return render(request, 'update_grupo.html', {'form': form})
