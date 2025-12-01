# Dockerfile CORRIGIDO
FROM python:3.13-slim

WORKDIR /app

# Instala dependências
RUN apt-get update && apt-get install -y \
    gcc \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# Copia requirements
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia projeto
COPY . .

# COMENTE ou REMOVA esta linha ↓
# RUN python manage.py collectstatic --noinput

EXPOSE 8082

CMD ["python", "manage.py", "runserver", "0.0.0.0:8082"]