# modulo de python para exterdel la clase formularios de las clases
from django.forms import ModelForm 
from django import forms
#importando el modelo de tarea
#from .models import Task
from junta.models import *

class PersonaForm(forms.Form):
    cedula = forms.CharField(max_length=13, label='Cedula/Ruc')
    nombres = forms.CharField(max_length=60, label='Nombres/Apellidos')
    direccion = forms.CharField(max_length=60, label='Dirección')    
    estado = forms.BooleanField(required=True)

class CreaPersonaForm(forms.ModelForm):
    class Meta:
        model = Personas
        fields = ['cedula', 'nombres', 'direccion', 'estado']
        widgets = {
            'cedula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la cedula'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombres y apellidos'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Direccion'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),
        }



#class TaskForm(forms.ModelForm):
 #   class Meta:  # crear el modelo en la cual va estar basada el formulario
  #      model = Task
   #     fields = ['title', 'description', 'important']
    #    widgets = {
     #        'title': forms.TextInput(attrs={'class': 'form-control'}),
      #       'description': forms.Textarea(attrs={'class': 'form-control'}),
       #      'important': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        #}
