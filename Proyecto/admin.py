from django.contrib import admin

from .models import *
# Register your models here.


admin.site.register(Usuario)
admin.site.register(Grupo)
admin.site.register(asignacionAlumno)
admin.site.register(ProgramaEducativo)
admin.site.register(Asignatura)
admin.site.register(Curso)
admin.site.register(Evidencia)
admin.site.register(asignacionEvidencia)
admin.site.register(evidenciaEntregada)