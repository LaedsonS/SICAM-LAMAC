from django import forms

class CadastroSolicitacao(forms.Form):
    proprietario = forms.CharField(
        label='Proprietário a máquina',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Informe o proprietário da máquina',
            'autocomplete':'name',
            'autofocus':True
        })
    )
    modelo_maquina = forms.CharField(
        label='Modelo ou Marca',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Informe o modelo/marca da máquina',
            'autocomplete':'name',
            'autofocus':True
        })
    )
    problema = forms.CharField(
        label='Problema',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Informe o problema da máquina',
            'autocomplete':'name',
            'autofocus':True
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class CadastroMaquinaForm(forms.Form):
    proprietario = forms.CharField(
        label='Proprietário da máquina',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Informe o proprietário da máquina',
            'autocomplete':'name',
            'autofocus':True
        })
    )
    modelo_maquina = forms.CharField(
        label='Modelo da máquina',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Informe o modelo/marca da máquina',
            'autocomplete':'name',
            'autofocus':True
        })
    )
    modelo_processador = forms.CharField(
        label='Modelo do processador',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Informe o modelo/marca do processador',
            'autocomplete':'name',
            'autofocus':True
        })
    )
    problema = forms.CharField(
        label='Problema',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Informe o problema da máquina',
            'autocomplete':'name',
            'autofocus':True
        })
    )

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