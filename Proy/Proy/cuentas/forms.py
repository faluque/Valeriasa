from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from .models import usuarios, ctacte


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=usuarios
        fields=('username','first_name', 'tipoUsr', 'nro_inquilino')


class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(label= ("Contraseña"),
                help_text= ("Para cambiar la contraseña utiliza <a href=\"/password/\">este formulario</a>."))
                   
    class Meta:
        model = usuarios
        fields = ('username', 'tipoUsr')

    def clean_password(self):
        password = self.cleaned_data.get('password')

        
        

class CuentaCorrienteForm(forms.ModelForm):
    def __init__(self,*arg,**kwargs):
        super(CuentaCorrienteForm, self).__init__(*arg, **kwargs)
        inq= usuarios.objects.filter(tipoUsr='I')
        self.fields['nro_inquilino'].queryset=inq
    class Meta:
        model= ctacte
        fields='__all__'
        