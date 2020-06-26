from django.db import models
from django.core.validators import MaxValueValidator

from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, matricula, nombre, apellido_paterno, apellido_materno, carrera, semestre, edad, genero, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            matricula=matricula,
            nombre=nombre,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            carrera=carrera,
            semestre=semestre,
            edad=edad,
            genero=genero,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, matricula, nombre, apellido_paterno, apellido_materno, carrera, semestre, edad, genero, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            matricula=matricula,
            nombre=nombre,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            carrera=carrera,
            semestre=semestre,
            edad=edad,
            genero=genero,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
    matricula = models.IntegerField(unique=True, validators=[MaxValueValidator(99999999)])
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)
    semestre = models.IntegerField( validators=[MaxValueValidator(10)])
    edad = models.IntegerField()
    genero = models.CharField(max_length=50)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['matricula', 'nombre', 'apellido_paterno', 'apellido_materno', 'carrera', 'semestre', 'edad', 'genero']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Libro(models.Model):
    Informatica='Informatica'
    Agronomia='Agronomia'
    Biologia='Biologia'
    Administracion='Administracion'
    GestionEmpresarial='GestionEmpresarial'
    Tics='Tics'
    CARRERA_CHOICES = [
        ('Informatica', 'Informatica'),
        ('Agronomia', 'Agronomia'),
        ('Biologia', 'Biologia'),
        ('Administracion', 'Administracion'),
        ('GestionEmpresarial', 'GestionEmpresarial'),
        ('Tics', 'Tics'),
    ]
    nombre = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    area = models.CharField(max_length=50,choices=CARRERA_CHOICES, default=Informatica)
    imagen = models.ImageField(upload_to="libros/portada")
    archivo = models.FileField(upload_to="libros/archivo")

    def __str__(self):
        return self.area

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

class RevistaCientifica(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    fecha = models.DateField()
    portada = models.ImageField(upload_to="RevistaCientifica/portadas")
    link = models.URLField()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "RevistaCientifica"
        verbose_name_plural = "RevistaCientificas"

class RevistaOsio(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    fecha = models.DateField()
    portada = models.ImageField(upload_to="RevistaOsio/portadas")
    link = models.URLField()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "RevistaOsio"
        verbose_name_plural = "RevistasOsios"

class Residencia(models.Model):
    Informatica='Informatica'
    Agronomia='Agronomia'
    Biologia='Biologia'
    Administracion='Administracion'
    GestionEmpresarial='GestionEmpresarial'
    Tics='Tics'
    CARRERA_CHOICES = [
        ('Informatica', 'Informatica'),
        ('Agronomia', 'Agronomia'),
        ('Biologia', 'Biologia'),
        ('Administracion', 'Administracion'),
        ('GestionEmpresarial', 'GestionEmpresarial'),
        ('Tics', 'Tics'),
    ] 
    CARRERA_CHOICES = [
        ('Tesis de Residencia', 'Tesis de Residencia'),
        ('Informe de Manual Tecnico', 'Informe de Manual Tecnco'),
        ('Biologia', 'Biologia'),
        ('Administracion', 'Administracion'),
        ('GestionEmpresarial', 'GestionEmpresarial'),
        ('Tics', 'Tics'),
    ]

    matricula = models.IntegerField(null=False, validators=[MaxValueValidator(99999999)])
    autores = models.CharField(max_length=250)
    carrera = models.CharField(max_length=100, choices=CARRERA_CHOICES, default=Informatica)
    tipo_doc = models.CharField(max_length=100)
    nombre_doc = models.CharField(max_length=200)
    fecha_elaboracion = models.DateField()
    fecha_ingreso = models.DateField()
    archivo = models.FileField(upload_to="Residencia/archivos")
 
class Video(models.Model):
    video = models.FileField(upload_to="video_home")
    
    