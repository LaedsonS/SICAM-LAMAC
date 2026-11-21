from django import forms

class CadastroSolicitacao(forms.Form):
    nome_proprietario = forms.CharField(
        label='Nome do proprietário da máquina',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Informe o nome do proprietário da máquina',
            'autocomplete':'name',
            'autofocus':True
        })
    )
    marca = forms.CharField(
        label='Modelo ou Marca',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Informe o modelo/marca da máquina',
            'autocomplete':'name',
        })
    )
    problema = forms.CharField(
        label='Problema',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Informe o problema da máquina',
            'autocomplete':'name',
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class CadastroMaquinaForm(forms.Form):
    proprietario = forms.CharField(
        label='Nome do proprietário da máquina',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Informe o nome do proprietário da máquina',
            'autocomplete':'name',
            'autofocus':True
        })
    )
    modelo_maquina = forms.CharField(
        label='Modelo/marca da máquina',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Informe o modelo/marca da máquina',
            'autocomplete':'name',
        })
    )
    modelo_processador = forms.CharField(
        label='Modelo do processador',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Informe o modelo do processador',
            'autocomplete':'name',
        })
    )
    defeito = forms.CharField(
        label='Defeito',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Informe o defeito da máquina',
            'autocomplete':'name',
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class AtulizacaoMaquinaForm(forms.Form):
    proprietario = forms.CharField(
        label='Proprietário a máquina',
        widget = forms.TelInput(attrs={
            'class':'form-control',
            'placeholder':'Informe o nome do proprietário da máquina',
            'autocomplete':'name',
            'autofocus':True
        }))
    modelo_maquina = forms.CharField(
        label='Modelo/marca da máquina',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Informe o modelo/marca da máquina',
            'autocomplete':'name',
        })
    )
    modelo_processador = forms.CharField(
        label='Modelo do processador',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Informe o modelo do processador',
            'autocomplete':'name',
        })
    )
    defeito = forms.CharField(
        label='defeito',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Informe o defeito da máquina',
            'autocomplete':'name',
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class RegistrarManutencao(forms.Form):
    procedimento = forms.CharField(
        label='Procedimento realizado',
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Informe o procedimento realizado',
            'autocomplete':'name',
            'autofocus':True
        })
    )
    maquina = forms.CharField(
        label='Máquina',
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Informe a máquina em que a manutenção foi feita',
            'autocomplete':'name',
        })
    )
    tecnico = forms.CharField(
        label='Técnico',
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Informe o técnico que fez manutenção',
            'autocomplete':'name',
        })
    )
    data = forms.DateField(
        label='Data da realização da manutenção',
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Informe a data em que a manutenção foi feita',
            'autocomplete':'name',
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data