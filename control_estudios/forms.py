from django import forms


class CursoFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64) 
    comision = forms.IntegerField(required=True, max_value=50000)

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64) 
    apellido = forms.CharField(required=True, max_length=64)
    dni = forms.CharField(required=True, max_length=64)
    email = forms.CharField(required=True, max_length=256)
    bio = forms.CharField(required=True, max_length=256)
    profesion = forms.CharField(required=True, max_length=128) 


class EntregableFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64) 
    fecha_entrega = forms.DateTimeField()
    esta_aprobado = forms.BooleanField(required=True, initial=False)