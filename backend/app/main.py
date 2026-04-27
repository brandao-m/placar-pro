from fastapi import FastAPI

app = FastAPI(
    title='Placar Pro API',
    description='API para acompanhamento de resultados de futebol.',
    version='0.1.0',
)


@app.get('/')
def root():
    return {
        'message': 'API do Placar Pro esta funcionando.'
    }


@app.get('/health')
def health_check():
    return {
        'status': 'ok'
    }