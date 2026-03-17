# GNUVet Modern

Sistema de gerenciamento para clínicas veterinárias desenvolvido com **FastAPI, SQLAlchemy, PostgreSQL, Docker e Angular**.

O projeto segue uma arquitetura moderna baseada em **camadas (routes → services → repository → models)** com suporte a **testes automatizados, autenticação JWT e deploy em cloud**.

---

# Arquitetura

Backend construído com **FastAPI + SQLAlchemy**.

```
Angular
   ↓
FastAPI (routes)
   ↓
Service Layer
   ↓
Repository Layer
   ↓
PostgreSQL
```

---

# Tecnologias

## Backend

* FastAPI
* SQLAlchemy 2.0
* PostgreSQL
* Alembic
* Pytest
* JWT (python-jose)
* Docker
* Mangum (AWS Lambda)

## Frontend

* Angular
* Angular CLI
* HttpClient

## Infraestrutura

* Docker
* PostgreSQL container
* AWS Lambda
* AWS S3
* AWS API Gateway

---

# Estrutura do Projeto

```
gnuvet-modern
│
├ backend
│
│ ├ app
│ │
│ │ ├ core
│ │ │ ├ config.py
│ │ │ └ security.py
│ │ │
│ │ ├ database
│ │ │ ├ base.py
│ │ │ ├ session.py
│ │ │ └ models.py
│ │ │
│ │ ├ models
│ │ │ ├ client.py
│ │ │ ├ pet.py
│ │ │ ├ clinic.py
│ │ │ ├ appointment.py
│ │ │ ├ medical_record.py
│ │ │ ├ vaccine.py
│ │ │ ├ payment.py
│ │ │ └ product.py
│ │ │
│ │ ├ schemas
│ │ │ ├ client_schema.py
│ │ │ ├ pet_schema.py
│ │ │ ├ appointment_schema.py
│ │ │ └ user_schema.py
│ │ │
│ │ ├ repository
│ │ │ └ client_repository.py
│ │ │
│ │ ├ services
│ │ │ ├ client_service.py
│ │ │ └ pet_service.py
│ │ │
│ │ ├ routes
│ │ │ ├ client_routes.py
│ │ │ ├ pet_routes.py
│ │ │ └ auth_routes.py
│ │ │
│ │ └ main.py
│ │
│ ├ tests
│ │ ├ conftest.py
│ │ ├ test_clients.py
│ │ ├ test_pets.py
│ │ └ test_health.py
│ │
│ ├ alembic
│ ├ requirements.txt
│ └ docker-compose.yml
│
└ frontend
```

---

# Executando o projeto

## 1. Clonar o projeto

```
git clone https://github.com/deivid-afonso/gnuvet-modern.git
cd gnuvet-modern
```

---

# Backend

## Criar ambiente virtual

```
python -m venv venv
```

Ativar

Windows

```
venv\Scripts\activate
```

Linux/Mac

```
source venv/bin/activate
```

---

## Instalar dependências

Dentro da pasta backend

```
pip install -r requirements.txt
```

---

# Banco de dados

O projeto usa **PostgreSQL via Docker**.

Arquivo:

```
backend/docker-compose.yml
```

```
services:

  postgres:
    image: postgres:15
    container_name: gnuvet-db
    restart: always

    environment:
      POSTGRES_USER: gnuvet
      POSTGRES_PASSWORD: gnuvet
      POSTGRES_DB: gnuvet

    ports:
      - "5433:5432"

    volumes:
      - postgres_data:/var/lib/postgresql/data

    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U gnuvet"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  postgres_data:
```

Subir banco

```
docker compose up -d
```

---

# Variáveis de ambiente

Arquivo:

```
backend/.env
```

```
DATABASE_URL=postgresql://gnuvet:gnuvet@localhost:5433/gnuvet
SECRET_KEY=supersecretkey
```

---

# Executar API

Dentro de backend

```
uvicorn app.main:app --reload
```

Abrir documentação:

```
http://localhost:8000/docs
```

---

# Testes

Rodar testes automatizados

```
pytest -v
```

Resultado esperado

```
test_clients PASSED
test_pets PASSED
test_health PASSED
```

---

# Endpoints disponíveis

## Clients

```
GET /clients
POST /clients
```

## Pets

```
GET /pets
POST /pets
```

## Auth

```
POST /auth/register
POST /auth/login
```

## Healthcheck

```
GET /health
```

---

# Frontend Angular

Criar projeto

```
npm install -g @angular/cli
ng new gnuvet-frontend
```

Rodar

```
ng serve
```

---

# Deploy AWS

Arquitetura utilizada

```
Angular
   ↓
S3
   ↓
CloudFront
   ↓
API Gateway
   ↓
AWS Lambda (FastAPI via Mangum)
   ↓
PostgreSQL (RDS)
```

---

# Próximas funcionalidades

* agenda de consultas
* prontuário veterinário
* controle de vacinas
* controle financeiro
* estoque de medicamentos
* dashboard administrativo

---

# Autor

Deivid da Silva Afonso
