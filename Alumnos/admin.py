from django import forms
from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import MyUser, Libro, Residencia, Video, RevistaOsio, RevistaCientifica

# Register your models here.
class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    GENERO_CHOICES = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
    )
    CARRERA_CHOICES = (
        ('Informatica', 'Informatica'),
        ('Agronomia', 'Agronomia'),
        ('Biologia', 'Biologia'),
        ('Administracion', 'Administracion'),
        ('GestionEmpresarial', 'GestionEmpresarial'),
        ('Tics', 'Tics'),
    )
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Contraseña Confirmacion', widget=forms.PasswordInput)
    genero = forms.ChoiceField(label='genero', choices=GENERO_CHOICES)
    carrera = forms.ChoiceField(label='carrera', choices=CARRERA_CHOICES)

    class Meta:
        model = MyUser
        fields = ('email','matricula', 'nombre', 'apellido_paterno', 'apellido_materno', 'carrera', 'semestre', 'edad', 'genero')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password no son iguales")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    GENERO_CHOICES = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
    )
    CARRERA_CHOICES = (
        ('Informatica', 'Informatica'),
        ('Agronomia', 'Agronomia'),
        ('Biologia', 'Biologia'),
        ('Administracion', 'Administracion'),
        ('GestionEmpresarial', 'GestionEmpresarial'),
        ('Tics', 'Tics'),
    )
    password = None
    genero = forms.ChoiceField(label='genero', choices=GENERO_CHOICES)
    carrera = forms.ChoiceField(label='carrera', choices=CARRERA_CHOICES)

    class Meta:
        model = MyUser
        fields =  ('email', 'matricula', 'nombre', 'apellido_paterno', 'apellido_materno', 'carrera', 'semestre', 'edad', 'genero')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'matricula', 'nombre', 'apellido_paterno', 'apellido_materno', 'carrera', 'semestre', 'edad', 'genero', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('matricula', 'nombre', 'apellido_paterno', 'apellido_materno', 'carrera', 'semestre', 'edad', 'genero',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'matricula', 'nombre', 'apellido_paterno', 'apellido_materno', 'carrera', 'semestre', 'edad', 'genero', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class LibroResource(resources.ModelResource):
    class Meta:
        model = Libro

class LibroAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','autor','area','imagen','archivo',)
    resources_class = LibroResource

class ResidenciaResource(resources.ModelResource):
    class Meta:
        model = Residencia

class ResidenciaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['matricula']
    list_display = ('matricula', 'autores','carrera','nombre_doc','tipo_doc','fecha_elaboracion','fecha_ingreso','archivo',)
    resources_class = ResidenciaResource

# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
admin.site.register(Libro,LibroAdmin)
admin.site.register(Video)
admin.site.register(Residencia, ResidenciaAdmin)
admin.site.register(RevistaCientifica)
admin.site.register(RevistaOsio)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)

