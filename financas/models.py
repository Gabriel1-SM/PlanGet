# financas/models.py
from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    TIPO_CHOICES = [
        ('receita', 'Receita'),
        ('despesa', 'Despesa'),
    ]
    
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    cor = models.CharField(max_length=7, default='#4361ee')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nome} ({self.tipo})"

class Transacao(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"