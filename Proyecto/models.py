from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    Nombres = models.CharField(max_length=50)
    aPaterno = models.CharField(max_length=50)
    aMaterno = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    tipoU = models.CharField(max_length=50)
    correoE = models.EmailField(max_length=50)
    contra = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class Grupo(models.Model):
    idProgramaEducativo = models.IntegerField()
    cuatrimestre = models.IntegerField(null=True,blank=True)
    grupoLetra =models.CharField(max_length=1)

class asignacionAlumno(models.Model):
    idGrupo =models.ForeignKey(Grupo,on_delete=models.CASCADE,blank=True,null=True,)
    idUsuario =models.ForeignKey(Usuario,on_delete=models.CASCADE,blank=True,null=True,)


class programaEducativo(models.Model):
    nombrePE = models.TextField(max_length=200)
    descrpcionPe = models.TextField(max_length=200)
    perfilIngreso = models.TextField(max_length=200)
    perfilEgreso = models.TextField(max_length=200)

class Asignatura(models.Model):
     nombreAsignatura = models.CharField(max_length=100)
     descripcionAsignatura = models.CharField(max_length=100)
     idProgramaEducativo = models.ForeignKey(programaEducativo,on_delete=models.CASCADE,blank=True,null=True,)


class Curso(models.Model):
    idAsignatura = models.ForeignKey(Asignatura,on_delete=models.CASCADE,blank=True,null=True,)
    idGrupo = models.ForeignKey(Grupo,on_delete=models.CASCADE,blank=True,null=True,)
    tipoCurso = models.CharField(max_length=100)
    fechainicio = models.DateField(blank=True,null=True)
    fechaFin = models.DateField(blank=True,null=True)


class Evidencia ( models.Model):
    nombreEvidencia = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    anexo = models.FileField(upload_to='archivos/')
    idCurso = models.ForeignKey(Curso,on_delete=models.CASCADE,blank=True,null=True,)
    tipoEvidencia = models.CharField(max_length=100)

class asignacionEvidencia(models.Model):
    idEvidencia = models.ForeignKey(Evidencia,on_delete=models.CASCADE,blank=True,null=True,)
    idGrupo = models.ForeignKey(Grupo,on_delete=models.CASCADE,blank=True,null=True,)
    fechaEntrega = models.DateField(blank=True,null=True)

class evidenciaEntregada(models.Model):
    idasignacionEvidencia = models.ForeignKey(asignacionEvidencia,on_delete=models.CASCADE,blank=True,null=True,)
    idasignacionAlumno = models.ForeignKey(asignacionAlumno,on_delete=models.CASCADE,blank=True,null=True,)
    ArchivoEntregado = models.FileField(upload_to='archivos/')
    calificacionEvidencia = models.DecimalField(decimal_places=2,max_digits=2)


