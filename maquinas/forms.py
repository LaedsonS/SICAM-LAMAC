from django import forms

class CadastroSolicitacao(forms.Form):
    proprietario = forms.CharField(label='Proprietário a máquina')
    modelo_maquina = forms.CharField(label='Modelo ou Marca')
    problema = forms.CharField(label='Problema')

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    
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

class RegistrarManutencao(forms.Form):
    procedimento = forms.CharField(label='Procedimento realizado')
    maquina = forms.CharField(label='Máquina')
    tecnico = forms.CharField(label='Técnico')
    data = forms.DateField(label='Data da realização da manutenção')

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data