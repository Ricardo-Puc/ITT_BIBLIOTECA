from django import forms
from .models import Residencia


class ResidenciaForm(forms.ModelForm):
    class Meta:
        model = Residencia
        fields=[
            'matricula',
            'autores',
            'carrera',
            'tipo_doc',
            'nombre_doc',
            'fecha_elaboracion',
            'fecha_ingreso',
            'archivo',
        
        ]
