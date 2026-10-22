from django import forms

class CadastroMaquinaForm(forms.Form):
    proprietario = forms.CharField(label='Proprietário a máquina')
    modelo_maquina = forms.CharField(label='Modelo da máquina')
    modelo_processador = forms.CharField(label='Modelo do processador')
    problema = forms.CharField(label='Problema')

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class AtulizacaoMaquinaForm(forms.Form):
    proprietario = forms.CharField(label='Proprietário a máquina')
    modelo_maquina = forms.CharField(label='Modelo da máquina')
    modelo_processador = forms.CharField(label='Modelo do processador')
    problema = forms.CharField(label='Problema')

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data