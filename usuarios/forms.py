from django import forms
class CadastroForms(forms.Form):
    nome = forms.CharField(label='e-mail')
    matricula = forms.CharField(label='matricula')
    senha = forms.CharField(label='e-mail', widget=forms.PasswordInput)
    confirmar_senha = forms.CharField(label='e-mail', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('senha')

        if senha != confirmar_senha:
            raise forms.ValidationError('Senhas não coincidem')
        
        return cleaned_data
        