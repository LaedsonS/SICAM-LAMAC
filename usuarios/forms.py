from django import forms
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
            'autocomplete' : 'name',
            'autofocus' : True
        })
    )
    email = forms.EmailField(
        label='E-mail',
        widget = forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Informe seu email para contato',
            'autocomplete' : 'name',
            'autofocus' : True
        })
    )
    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Informe sua senha',
            'autocomplete' : 'name',
            'autofocus' : True
        })
    )
    confirmar_senha = forms.CharField(
        label='Confirmar senha', 
        widget=forms.PasswordInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Informe sua senha',
            'autocomplete' : 'name',
            'autofocus' : True
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('senha')

        if senha != confirmar_senha:
            raise forms.ValidationError('Senhas não coincidem')
        
        return cleaned_data

class LoginForms(forms.Form):
    matricula = forms.CharField(
        label='Matricula',
        widget= forms.NumberInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Informe sua matrícula',
            'autocomplete' : 'name',
            'autofocus' : True
        })
    )
    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={

        }))

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('senha')

        if senha != confirmar_senha:
            raise forms.ValidationError('Senhas não coincidem')
        
        return cleaned_data