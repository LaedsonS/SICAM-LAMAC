from django import forms
from .models import Usuario
from django.contrib.auth.hashers import check_password

class CadastroForms(forms.Form):
    nome = forms.CharField(
        label='Nome',
        widget = forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Informe seu nome',
            'autocomplete' : 'name',
            'autofocus' : True
        })
    )
    matricula = forms.CharField(
        label='Matricula',
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Informe sua matrícula',
            'autocomplete' : 'username',
        })
    )
    email = forms.EmailField(
        label='E-mail',
        widget = forms.EmailInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Informe seu email para contato',
            'autocomplete' : 'email',
        })
    )
    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Informe sua senha',
            'autocomplete' : 'new-password',
        })
    )
    confirmar_senha = forms.CharField(
        label='Confirmar senha', 
        widget=forms.PasswordInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Informe sua senha',
            'autocomplete' : 'new-password',
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('confirmar_senha')

        if senha != confirmar_senha:
            raise forms.ValidationError('Senhas não coincidem')
        
        return cleaned_data
    
    def clean_matricula(self):
        matricula = self.cleaned_data['matricula']
        if Usuario.objects.filter(matricula=matricula).exists():
            raise forms.ValidationError('Essa matrícula já está cadastrada')
        return matricula

class LoginForms(forms.Form):
    matricula = forms.CharField(
        label='Matricula',
        widget= forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Informe sua matrícula',
            'autocomplete':'username',
            'autofocus':True,
            'inputmode': 'numeric'
        })
    )
    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'Informe sua senha',
            'autocomplete':'current-password'
        })
    )

    def clean(self):
        self.cleaned_data = super().clean()
        self.matricula = self.cleaned_data.get('matricula')
        self.senha = self.cleaned_data.get('senha')

        if self.matricula and self.senha:
            try:
                usuario = Usuario.objects.get(matricula=self.matricula) 
            except Usuario.DoesNotExist:
                usuario = None

            if usuario is None or not check_password(self.senha, usuario.senha):
                raise forms.ValidationError('Matrícula ou senha inválidas')

            self.cleaned_data['usuario'] = usuario

        return self.cleaned_data