from django import forms
from .models import Contacto, Compra, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class RegistroForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Requerido. Máximo 30 caracteres.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Requerido. Máximo 30 caracteres.')
    email = forms.EmailField(max_length=254, required=True, help_text='Requerido. Ingrese una dirección de correo válida.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['metodo_pago', 'direccion_envio']
