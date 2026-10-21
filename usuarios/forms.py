from django import forms
class CadastroForms(forms.Form):
    matricula = forms.CharField(label='Matricula')
    nome = forms.EmailField(label='E-mail')
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
    confirmar_senha = forms.CharField(label='Confirmar senha', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('senha')

        if senha != confirmar_senha:
            raise forms.ValidationError('Senhas não coincidem')
        
        return cleaned_data
        