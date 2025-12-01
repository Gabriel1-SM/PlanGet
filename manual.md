📘 PlanGet — Documentação Oficial

Sistema de Controle Financeiro Pessoal
Tecnologia: Django (Python)
Autor: Gabriel Morais

📑 Sumário

Introdução

Objetivo do Sistema

Arquitetura do Projeto

Estrutura de Pastas

Funcionalidades

Modelos de Dados

Fluxo de Funcionamento

Tecnologias Utilizadas

Como Executar o Projeto

Possíveis Melhorias Futuras

🧭 Introdução

O PlanGet é um sistema web desenvolvido em Django com o objetivo de permitir que o usuário organize suas finanças pessoais.
O sistema possibilita o cadastro de categorias, transações e a visualização desses dados através de um dashboard simples e funcional.

Este projeto foi criado para fins educacionais na faculdade, mas possui estrutura modular e pode ser ampliado facilmente.

🎯 Objetivo do Sistema

O PlanGet tem como foco principal:

Facilitar o registro de entradas e saídas financeiras.

Permitir a organização por categorias.

Proporcionar uma interface simples, clara e funcional para o usuário.

Servir como base de estudo para Django (Models, Views, URLs, Templates).

🧱 Arquitetura do Projeto

O projeto segue o padrão MVC (Model–View–Template) utilizado pelo Django:

Projeto principal (PlanGet/)
Contém configurações globais, rotas principais e inicialização do sistema.

Aplicação financas/
Módulo onde está toda a lógica:

modelos de dados

formulários

rotas

views

templates

migrações

regras de negócio

Banco SQLite3
Usado para persistência dos dados das transações e categorias.

📂 Estrutura de Pastas
PlanGet/
│── manage.py
│── db.sqlite3
│── manual.md
│
│── PlanGet/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
│── financas/
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    │
    ├── migrations/
    │   ├── __init__.py
    │   └── 0001_initial.py
    │
    └── templates/
        └── financas/
            ├── base.html
            ├── index.html
            ├── login.html
            ├── dashboard.html
            ├── cadastro.html
            ├── categorias_list.html
            ├── categoria_form.html
            ├── transacoes_list.html
            └── transacao_form.html

⚙️ Funcionalidades

O sistema implementa:

✅ Autenticação

Tela de login

Restrição de páginas para usuários autenticados

✅ Categorias

Criar categorias

Listar categorias

Editar categorias (se implementado)

Excluir categorias (se implementado)

✅ Transações

Criar transações (entrada ou saída)

Relacionar transações com categorias

Listar transações

Somatórios básicos

✅ Dashboard

Exibe resumo financeiro

Exibe total de entradas e saídas

Pode incluir gráficos futuramente

🛢️ Modelos de Dados
Categoria
Campo	Tipo	Descrição
nome	CharField	Nome da categoria
descricao	TextField	Detalhes opcionais da categoria
Transacao
Campo	Tipo	Descrição
nome	CharField	Nome da transação
valor	DecimalField	Valor da transação
tipo	CharField	Tipo: entrada ou saída
categoria	ForeignKey	Relacionamento com Categoria
data	DateField	Data em que ocorreu
🔄 Fluxo de Funcionamento

Usuário acessa o login

Após autenticação, é redirecionado ao dashboard

No menu, pode escolher:

Categorias

Transações

Em Categorias:

Criar nova categoria

Listar categorias existentes

Em Transações:

Registrar entrada ou saída

Escolher categoria

Ver lista completa

Dashboard mostra o resumo geral.

🛠️ Tecnologias Utilizadas

Python 3

Django

SQLite3

HTML5 + CSS3 (templates)

Bootstrap (se você utilizou)

▶️ Como Executar o Projeto
1️⃣ Clonar o repositório
git clone https://github.com/usuario/PlanGet.git
cd PlanGet

2️⃣ Criar ambiente virtual
python -m venv venv
venv/Scripts/activate  # Windows

3️⃣ Instalar dependências
pip install -r requirements.txt

4️⃣ Rodar migrações
python manage.py migrate

5️⃣ Rodar servidor
python manage.py runserver


O sistema estará disponível em:

http://127.0.0.1:8000/

## Como rodar com docker

```bash
    # 1. Construa a imagem
    docker build -t planget .

    # Roda em background (-d) com nome (--name)
    docker run --rm -d --name planget-app -p 8082:8082 planget

    # Verificar container rodando
    docker ps

    # Verificar todos os container
    docker ps -a

    # Verificar logs
    docker logs (id do container ou name)

    # Excluir do container
    docker rm -f (id do container ou name)
```