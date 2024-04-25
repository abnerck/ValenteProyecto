from django.forms import ModelForm
from .models import *

class UsuarioForm(ModelForm):
    class Meta:

        model = Usuario
        fields = ['Nombres','aPaterno','aMaterno','matricula','telefono','tipoU','correoE','contra',]
        labels ={
            'Nombres':'Nombre(s)',
            'aPaterno':'Apellido Paterno',
            'aMaterno':'Apellido Materno',
            'matricula': 'Matricula',
            'telefono': 'Telefono', 
            'tipoU': 'Tipo', 
            'correoE':'Correo Electronico' ,
            'contra':'Contraseña' 
        
            
        }

class GrupoForm (ModelForm):
    class Meta:
        model = Grupo
        fields = ['idProgramaEducativo','cuatrimestre','grupoLetra']
        labels = {
            'idProgramaEducativo':'Programa Educativo', 
            'cuatrimestre':'Cuatrimestre', 
            'grupoLetra':'Grupo'
        }
# TABLA QUE SOLO ES DE RELACION
'''class asignacionAlumnoForm(ModelForm):
    model = asignacionAlumno
    fields = ['idGrupo','idUsuario']
    labels = {
        'idGrupo':'Id Grupo',
        'idUsuario':'idUsuario',
    }
'''
class ProgramaEducativoForm(ModelForm):
    class Meta:
        model = ProgramaEducativo
        fields=[ 'nombrePE','descrpcionPe','perfilIngreso','perfilEgreso' ]
        labels = {
            'nombrePE':'Nombre Proyecto Educativo',
            'descrpcionPe':'Descripcion Proyecto Educativo',
            'perfilIngreso':'Perfil Ingreso',
            'perfilEgreso':'Perfil Egreso',
        }

class AsignaturaForm (ModelForm):
    class Meta:
        model = Asignatura
        fields = ['nombreAsignatura','descripcionAsignatura','idProgramaEducativo']
        labels = {
            'nombreAsignatura':'Nombre Asignatura',
            'descripcionAsignatura':'Descripcion Asignatura',
            'idProgramaEducativo':'Programa Educativo',        
        }

class CursoForm (ModelForm):
    class Meta:
        model = Curso

        fields = ['idAsignatura','idGrupo','tipoCurso','fechainicio','fechaFin']
        labels = {
            'idAsignatura':'Asignatura',
            'idGrupo':'Grupo',
            'tipoCurso':'Tipo de curso',
            'fechainicio':'Fecha de Inicio',
            'fechaFin':'Fecha Final'

        }

class EvidenciaForm ( ModelForm):
    class Meta:
        model = Evidencia 

        fields = ['nombreEvidencia','descripcion','anexo','idCurso','tipoEvidencia']
        labels = {
            'nombreEvidencia':'Nombre Evidencia',
            'descripcion':'Descripcion',
            'anexo':'Anexo',
            'idCurso':'Curso',
            'tipoEvidencia':'Tipo de Evidencia',
            
        }

class AsignacionEvidenciaForm(ModelForm):
    class Meta:
        model = asignacionEvidencia
        fields = ['idEvidencia','idGrupo','fechaEntrega']
        labels = {'idEvidencia':'Evidencia',
                'idGrupo':'Grupo',
                'fechaEntrega':'Fecha de Entrega'}

class evidenciaEntregadaForm(ModelForm):
    class Meta:
        model = evidenciaEntregada
        fields = ['idasignacionEvidencia','idasignacionAlumno','ArchivoEntregado','calificacionEvidencia']
        labels = {
            'idasignacionEvidencia':'Asignacion de Evidencia',
            'idasignacionAlumno':'Alumno',
            'ArchivoEntregado':'Archivo Entregado',
            'calificacionEvidencia':'Calificacion ',}
