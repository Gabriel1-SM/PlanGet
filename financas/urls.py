# financas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
    
    
    path('transacoes/', views.listar_transacoes, name='listar_transacoes'),
    path('transacoes/nova/', views.criar_transacao, name='criar_transacao'),
    path('transacoes/editar/<int:id>/', views.editar_transacao, name='editar_transacao'),
    path('transacoes/excluir/<int:id>/', views.excluir_transacao, name='excluir_transacao'),
    
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/nova/', views.criar_categoria, name='criar_categoria'),
    path('categorias/editar/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/excluir/<int:id>/', views.excluir_categoria, name='excluir_categoria'),
]