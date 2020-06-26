from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django .contrib.auth.decorators import login_required
from .models import MyUser
from django.contrib import messages
from Alumnos.models import MyUser, Libro, Video, RevistaCientifica, RevistaOsio, Residencia
from .admin import UserCreationForm, UserChangeForm, UserAdmin
from django.views.generic import CreateView
from Alumnos.forms import ResidenciaForm
from django.urls import reverse_lazy

# Vista para el logueo por email
def loginPage(request):
    variables={
        
    }
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        MyUser = authenticate(request, email=email, password=password)

        if MyUser is not None:
            login(request, MyUser)
            return redirect('home')
        else:
             messages.warning(request,'Tu Correo o Contraseña son Incorrectos')

    return render(request, 'Alumnos/login.html',variables)

#Vista de registro al sistema
def registro(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registro exitoso')

            if user is not None:
                login(request, user) 
                return redirect('loginPage')
        else:
            messages.success(request, 'Verifique que sus datos sean correctos')
    return render(request,'Alumnos/registro.html', {'form': form})

class CreateResidencia(CreateView):
    model = Residencia
    form_class = ResidenciaForm 
    template_name = 'Alumnos/subir_archivo.html'
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            messages.success(request,'Registro Guardado Correctamente')
            return self.form_valid(form, **kwargs)
        else:
            return self.render_to_response(context)
    success_url = reverse_lazy('residencia')
   

#vista para el cierre de sesion
def logoutUser(request):
    logout(request)
    messages.success(request,'Sesion Terminada Exitosamente')
    return redirect('loginPage')

#vista pricipal despues de logueo
@login_required(login_url='loginPage')
def home(request):
    video = Video.objects.all()

    return render(request, 'Alumnos/home.html',{
        'video':video
    })
@login_required(login_url='loginPage')
def perfil(request):
    usuario = MyUser.objects.filter(email=request.user)

    return render(request, 'Alumnos/perfil.html',{
        'usuario':usuario
    })
@login_required(login_url='loginPage')
def libros(request):
    libros = Libro.objects.all()

    return render(request, 'Alumnos/libros.html',{
        'libros':libros
    })
@login_required(login_url='loginPage')
def revistas(request):
    revistas = RevistaCientifica.objects.all()
    osio = RevistaOsio.objects.all()
    

    return render(request, 'Alumnos/revistas.html',{
        'revistas':revistas,
        'osio':osio
        
    })
@login_required(login_url='loginPage')
def residencia(request):
    archivos = Residencia.objects.all()

    return render(request, 'Alumnos/residencia.html',{
        'archivos':archivos
    })
@login_required(login_url='loginPage')
def estadisticas(request):
    datosF = MyUser.objects.filter(genero="Femenino").count()
    datosM = MyUser.objects.filter(genero="Masculino").count()

    informatica = MyUser.objects.filter(carrera="Informatica").count()
    tics = MyUser.objects.filter(carrera="Tics").count()
    agronomia = MyUser.objects.filter(carrera="Agronomia").count()
    biologia = MyUser.objects.filter(carrera="Biologia").count()
    administracion = MyUser.objects.filter(carrera="Administracion").count()
    gestion = MyUser.objects.filter(carrera="GestionEmpresarial").count()
    
    libros = Libro.objects.all().count()
    archivos = Residencia.objects.all().count()
    usuarios = MyUser.objects.all().count()
    osi = RevistaOsio.objects.all().count()
    cien = RevistaCientifica.objects.all().count()

    return render(request, 'Alumnos/estadisticas.html',{
        'usuarios':usuarios,
        'datosF':datosF,
        'datosM':datosM,
        'informatica':informatica,
        'tics':tics,
        'agronomia':agronomia,
        'biologia':biologia,
        'gestion':gestion,
        'administracion':administracion,
        'libros':libros,
        'archivos':archivos,
        'osi':osi,
        'cien':cien
    })
@login_required(login_url='loginPage')
#vista para la Actualizacion de datos de usuario en desarrollo
def actualizar(request):
    if request.method=='POST':
        user_form = UserChangeForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request,'Actualizado correctamente')
            return redirect('perfil')
        
        else:

            messages.success(request,'Error, Verifique que sus Datos sean Correctos')
            return redirect('actualizar')
        
    elif request.method == "GET":
        user_form = UserChangeForm(instance=request.user)

        return render(request, 'Alumnos/modificar.html',{'user_form':user_form})
@login_required(login_url='loginPage')
def desarrollador(request):

    return render(request,'Alumnos/desarrollador.html')

