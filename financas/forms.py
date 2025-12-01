# financas/forms.py
from django import forms
from .models import Transacao, Categoria

class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ['descricao', 'valor', 'data', 'categoria']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descrição da transação'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '0.00'}),
            'categoria': forms.Select(attrs={'class': 'form-control'})
        }
    
    def __init__(self, user, *args, **kwargs):
        super(TransacaoForm, self).__init__(*args, **kwargs)
        # Filtra categorias apenas do usuário logado
        self.fields['categoria'].queryset = Categoria.objects.filter(usuario=user)

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'tipo', 'cor']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da categoria'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'cor': forms.TextInput(attrs={'type': 'color', 'class': 'form-control form-control-color'})
        }