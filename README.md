# Placar Pro

Placar Pro é uma aplicação full-stack para acompanhamento de resultados de futebol, desenvolvida com FastAPI, PostgreSQL, React, Vite e Tailwind CSS.

## Objetivo

O objetivo do projeto é criar uma plataforma inspirada em sistemas de live score, permitindo visualizar partidas de futebol por data, acompanhar placares, status dos jogos, campeonatos e detalhes básicos das partidas.

## Funcionalidades previstas

- Listagem de partidas por data
- Visualização de placares
- Status da partida
- Informações dos times
- Informações dos campeonatos
- Página de detalhes da partida
- Filtros por data e campeonato
- Integração com API externa de futebol
- Cache de dados para reduzir chamadas externas

## Tecnologias

### Backend

- Python
- FastAPI
- SQLModel
- PostgreSQL
- Alembic
- HTTPX
- Pydantic Settings

### Frontend

- React
- Vite
- TypeScript
- Tailwind CSS
- React Router
- Axios
- TanStack Query

## Estrutura prevista

```
placar-pro/
│
├── backend/
│   ├── app/
│   ├── alembic/
│   ├── requirements.txt
│   └── README.md
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── README.md
│
├── README.md
└── .gitignore
```

## Status do projeto

Em desenvolvimento.

Roadmap
Fase 1 — Fundação
- Criar estrutura inicial do projeto
- Configurar backend com FastAPI
- Configurar frontend com React, Vite e Tailwind
- Criar documentação inicial

Fase 2 — Backend
- Configurar banco PostgreSQL
- Criar modelos iniciais
- Criar endpoints de partidas
- Integrar com API externa de futebol

Fase 3 — Frontend
- Criar layout principal
- Criar cards de partidas
- Criar filtro por data
- Criar página de detalhes da partida

Fase 4 — Polimento
- Melhorar responsividade
- Adicionar loading states
- Adicionar tratamento de erros
- Atualizar README com prints
- Preparar deploy
