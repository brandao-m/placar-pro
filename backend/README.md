# Backend — Placar Pro

API do projeto Placar Pro, desenvolvida com FastAPI.

## Tecnologias

- Python
- FastAPI
- SQLModel
- PostgreSQL
- HTTPX
- Pydantic Settings
- Uvicorn

## Como rodar o backend localmente

Crie o ambiente virtual:
```
python -m venv .venv
```
Ative o ambiente virtual:
```
.venv\Scripts\activate
```
Instale as dependências:
```
pip install -r requirements.txt
```
Execute o servidor:
```
uvicorn app.main:app --reload
```
Acesse:
```
http://127.0.0.1:8000
```
Documentação automática:
```
http://127.0.0.1:8000/docs
```
---