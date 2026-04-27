from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
)


@app.get('/')
def root():
    return {
        'message': 'API do Placar Pro esta funcionando.'
    }


@app.get('/health')
def health_check():
    return {
        'status': 'ok',
        'app': settings.APP_NAME,
        'version': settings.APP_VERSION,
    }