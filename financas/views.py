# financas/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from datetime import datetime
from .models import Transacao, Categoria
from .forms import TransacaoForm, CategoriaForm

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # LOGIN AUTOMÁTICO APÓS CADASTRO
            
            #8 CATEGORIAS PADRÃO AUTOMATICAMENTE
            categorias_padrao = [
                {'nome': 'Salário', 'tipo': 'receita', 'cor': '#28a745'},
                {'nome': 'Freelance', 'tipo': 'receita', 'cor': '#20c997'},
                {'nome': 'Investimentos', 'tipo': 'receita', 'cor': '#17a2b8'},
                {'nome': 'Alimentação', 'tipo': 'despesa', 'cor': '#dc3545'},
                {'nome': 'Transporte', 'tipo': 'despesa', 'cor': '#fd7e14'},
                {'nome': 'Moradia', 'tipo': 'despesa', 'cor': '#6f42c1'},
                {'nome': 'Lazer', 'tipo': 'despesa', 'cor': '#e83e8c'},
                {'nome': 'Saúde', 'tipo': 'despesa', 'cor': '#6c757d'},
            ]
            
            for cat_data in categorias_padrao:
                Categoria.objects.create(usuario=user, **cat_data)
            # FIM DA FEATURE ESPECIAL
            
            messages.success(request, 'Cadastro realizado com sucesso! Categorias padrão criadas.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Erro no cadastro. Verifique os dados.')
    else:
        form = UserCreationForm()
    
    return render(request, 'cadastro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user) # cria a sessão, sessionid no navegador
            messages.success(request, f'Bem-vindo, {user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    
    return render(request, 'login.html')

# DESTAQUE: DASHBOARD COM CÁLCULOS AUTOMÁTICOS
@login_required  # SÓ USUÁRIOS LOGADOS PODEM ACESSAR
def dashboard(request):
    # Busca transações
    transacoes = Transacao.objects.filter(usuario=request.user).order_by('-data')[:10]
    categorias = Categoria.objects.filter(usuario=request.user)
    
    # CÁLCULO
    total_receitas = Transacao.objects.filter(
        usuario=request.user, 
        categoria__tipo='receita'  # FILTRA SÓ RECEITAS
    ).aggregate(Sum('valor'))['valor__sum'] or 0  # SOMA OS VALORES aggregate(Sum()) DO DJANGO
    
    total_despesas = Transacao.objects.filter(
        usuario=request.user, 
        categoria__tipo='despesa'  # FILTRA SÓ DESPESAS
    ).aggregate(Sum('valor'))['valor__sum'] or 0
    
    saldo = total_receitas - total_despesas  # SALDO CALCULADO AUTOMATICAMENTE
    
    context = {
        'transacoes': transacoes,
        'total_receitas': total_receitas,
        'total_despesas': total_despesas,
        'saldo': saldo,
        'categorias': categorias,
    }
    
    return render(request, 'dashboard.html', context)

@login_required
def listar_transacoes(request):
    transacoes = Transacao.objects.filter(usuario=request.user).order_by('-data')
    return render(request, 'financas/transacoes_list.html', {'transacoes': transacoes})

@login_required
def criar_transacao(request):
    if request.method == 'POST':
        form = TransacaoForm(request.user, request.POST)
        if form.is_valid():
            transacao = form.save(commit=False)
            transacao.usuario = request.user  # ASSOCIA AO USUÁRIO LOGADO
            transacao.save()
            messages.success(request, 'Transação criada com sucesso!')
            return redirect('listar_transacoes')
    else:
        form = TransacaoForm(request.user)
    
    return render(request, 'financas/transacao_form.html', {'form': form})

# DESTAQUE: EDIÇÃO COM DUPLA SEGURANÇA
@login_required
def editar_transacao(request, id):
    # 1ª SEGURANÇA: @login_required (só logados)
    # 2ª SEGURANÇA: get_object_or_404 com usuario=request.user
    transacao = get_object_or_404(Transacao, id=id, usuario=request.user)
    # ^ IMPEDE QUE UM USUÁRIO EDITE TRANSAÇÕES DE OUTRO
    
    if request.method == 'POST':
        form = TransacaoForm(request.user, request.POST, instance=transacao)
        if form.is_valid():
            form.save()
            messages.success(request, 'Transação atualizada com sucesso!')
            return redirect('listar_transacoes')
    else:
        form = TransacaoForm(request.user, instance=transacao)
    
    return render(request, 'financas/transacao_form.html', {'form': form, 'editar': True})

@login_required
def excluir_transacao(request, id):
    transacao = get_object_or_404(Transacao, id=id, usuario=request.user)
    
    if request.method == 'POST':  # SÓ EXCLUI APÓS CONFIRMAÇÃO (POST)
        transacao.delete()
        messages.success(request, 'Transação excluída com sucesso!')
        return redirect('listar_transacoes')
    
    return render(request, 'financas/transacao_confirm_delete.html', {'transacao': transacao})

@login_required
def listar_categorias(request):
    categorias = Categoria.objects.filter(usuario=request.user)
    return render(request, 'financas/categorias_list.html', {'categorias': categorias})

@login_required
def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.usuario = request.user
            categoria.save()
            messages.success(request, 'Categoria criada com sucesso!')
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    
    return render(request, 'financas/categoria_form.html', {'form': form})

@login_required
def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id, usuario=request.user)
    
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria atualizada com sucesso!')
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    
    return render(request, 'financas/categoria_form.html', {'form': form, 'editar': True})

@login_required
def excluir_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id, usuario=request.user)
    
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoria excluída com sucesso!')
        return redirect('listar_categorias')
    
    return render(request, 'financas/categoria_confirm_delete.html', {'categoria': categoria})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('index')