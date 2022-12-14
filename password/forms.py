from django import forms


STATUS = (
    ('1', 'Letras'),
    ('2', 'Letras e numeros'),
    ('3', 'Letras, numeros e simbolos')
)


class PasswordForm(forms.Form):
    title = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Titulo', 'id': 'title'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usuario', 'id': 'usuario'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Senha - Se vazio sera gerado uma randomica'
        , 'id': 'password'}),  required=False)
    url = forms.CharField(widget=forms.URLInput(attrs={'value': 'https://wwww.', 'placeholder': 'Url', 'id': 'url'}), required=False)


class GenerateForm(forms.Form):
    length = forms.CharField(widget=forms.NumberInput(attrs={'value': '16', 'placeholder': 'Tamanho', 'id': 'length'}),
                             required=True)
    option = forms.ChoiceField(choices=STATUS, required=True)
