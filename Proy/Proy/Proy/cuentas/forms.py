from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import usuarios, ctacte

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = usuarios
        fields = ('username', 'tipoUsr')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = usuarios
        fields = ('username', 'tipoUsr')
    def clean_password(self):
        password = self.cleaned_data.get('password')
        
        

class CuentaCorrienteForm(forms.ModelForm):
    def __init__(self,*arg,**kwargs):
        super(CuentaCorrienteForm, self).__init__(*arg, **kwargs)
        self.fields['inquilino'].queryset= usuarios.objects.filter(tipoUsr='I')
    
    class Meta:
        model= ctacte
        fields='__all__'
        