import requests

# URL base da API local
base_url = "http://127.0.0.1:8000"

# 🔸 Criar um contato
contato = {
    "nome": "Morgana Freitas",
    "telefones": [
        {"numero": "51999994465", "tipo": "movel"},
        {"numero": "5133331299", "tipo": "fixo"}
    ],
    "categoria": "pessoal"
}

response = requests.post(f"{base_url}/contatos/", json=contato)
print("✅ Criar contato:", response.status_code, response.json())

# 🔸 Listar todos os contatos
response = requests.get(f"{base_url}/contatos/")
print("✅ Listar contatos:", response.status_code, response.json())

# 🔸 Buscar contato por ID (ID = 1)
response = requests.get(f"{base_url}/contatos/1")
print("✅ Buscar contato ID 1:", response.status_code, response.json())
