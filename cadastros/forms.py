from django.contrib.auth import forms
from django.forms import CharField, PasswordInput

from cadastros.models import Usuario, UsuarioDjango
#from .models import Usuario

class LoginResumoForm(forms.AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginResumoForm, self).__init__(*args, **kwargs)
    
    model = Usuario
    
    class Meta(forms.AuthenticationForm):
        exclude = [
        'username',
        'usuário',
        ]



'''
class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Usuario
        
        fields = ['password', 'email', 'nivel',]
        
        exclude = ['id', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined',]

class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Usuario
        
        fields = ['password', 'email', 'nivel',]
        
        exclude = ['id', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined',]
'''