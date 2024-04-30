"""
URL configuration for Valente project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proyecto import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    
 
    #PROGRAMA EDUCATIVO
    path('ProgramaEducativo/', views.ProgramasEducativo, name='programaeducativo'),
    path('programa/create/', views.create_programaeducativo, name='create_programaeducativo'),
    path('delete_programaEducativo/<int:programa_id>/', views.delete_programaEducativo, name='delete_programaEducativo'),
    path('update_programaEducativo/<int:programa_id>/', views.update_programaEducativo, name='update_programaEducativo'),

    #ASIGNATURAS    
    path('asignaturas/',views.asignaturas, name='asignaturas'),
    path('asignatura/create/', views.create_asignatura, name='create_asignatura'),
    path('delete_asignatura/<int:asignatura_id>/', views.delete_asignatura, name='delete_asignatura'),
    path('update_asignatura/<int:asignatura_id>/', views.update_asignatura, name='update_asignatura'),

    #CURSO
    path('curso/',views.curso, name='cursos'),
    path('curso/create/', views.create_curso, name='create_curso'),
    path('delete_curso/<int:curso_id>/', views.delete_curso, name='delete_curso'),
    path('update_curso/<int:curso_id>/', views.update_curso, name='update_curso'),

       # Ruta que queremos que lleve / vista que creamos / Pagina html que esta vinculada
    path('usuarios/',views.Users,name='usuarios'),
    path('users/create/', views.create_user,name='create_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('usuarios/update/<int:user_id>/', views.update_user, name='update_user'),


    #EVIDENCIA
    path('evidencia/',views.evidencia, name='evidencias'),
    path('evidencias/create/', views.create_evidencia, name='create_evidencia'),
    path('delete_evidencia/<int:evidencia_id>/', views.delete_evidencia, name='delete_evidencia'),
    path('update_evidencia/<int:evidencia_id>/', views.update_evidencia , name='update_evidencia'),

    #GRUPO
    path('grupos/',views.grupos, name='grupos'),
    path('grupos/create/', views.create_grupo, name='create_grupo'),
    path('delete_grupo/<int:grupo_id>/', views.delete_grupo, name='delete_grupo'),
    path('update_grupo/<int:grupo_id>/', views.update_grupo , name='update_grupo')



    

]

