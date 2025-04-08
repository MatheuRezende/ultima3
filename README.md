# Restaurante do Matheus

## Como rodar localmente

1. Clone o repositório
2. Copie `.env.example` para `.env` e configure os dados do banco (Railway)
3. Execute com Docker:

```
docker build -t restaurante .
docker run -p 5000:5000 --env-file .env restaurante
```

## Como subir no Render

1. Crie um novo Web Service
2. Escolha Docker e conecte este repositório
3. Configure variáveis de ambiente do banco (Railway)
4. Faça o deploy!

## Frontend

Abra `frontend/index.html` no navegador para testar a API.