#  API de Agenda de Contatos / Contacts REST API

Uma API simples para gerenciar uma agenda de contatos, desenvolvida com FastAPI e Python 3.10.11.  
A simple API to manage a contact agenda, developed with FastAPI and Python 3.10.11.

---

## 📦 Funcionalidades / Features

-  Criar contato / Create contact
-  Listar contatos / List all contacts
-  Buscar contato por ID / Get contact by ID

---

##  Como executar / How to run

### 1️⃣ Clonar o repositório / Clone the repository

```bash
git clone https://github.com/dieineb/contacts-rest-api.git
cd contacts-rest-api
````

### 2️⃣ Criar e ativar o ambiente virtual / Create and activate the virtual environment

```bash
python -m venv venv
```

* Ativar no Windows (CMD):

```bash
venv\Scripts\activate
```

* Ativar no PowerShell:

```bash
venv\Scripts\Activate.ps1
```

* Ativar no Linux/Mac:

```bash
source venv/bin/activate
```

### 3️⃣ Instalar as dependências / Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Executar a API / Run the API

```bash
uvicorn main:app --reload
```

### 5️⃣ Acessar a documentação interativa / Access interactive documentation

* Swagger UI: 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Redoc: 👉 [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Endpoints da API / API Endpoints

| Método/Method | Endpoint       | Descrição/Description                     |
| ------------- | -------------- | ----------------------------------------- |
| POST          | /contatos/     | Criar contato / Create contact            |
| GET           | /contatos/     | Listar contatos / List contacts           |
| GET           | /contatos/{id} | Buscar contato por ID / Get contact by ID |

---

## Teste / Testing

Execute o script de teste:

```bash
python test_api.py
```

---

## Tecnologias / Technologies

* Python 3.10.11
* FastAPI
* Uvicorn
* Requests

---

## Requisitos / Requirements

* Python >= 3.10.11

---

## Licença / License

Este projeto está sob a licença MIT.
This project is licensed under the MIT License.

```


