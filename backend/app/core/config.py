from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = 'Placar Pro API'
    APP_DESCRIPTION: str = 'API para acompanhamento de resultados de futebol.'
    APP_VERSION: str = '0.1.0'

    DATABASE_URL: str = 'postgresql://postgres:postgres@localhost:5432/placar_pro'

    FOOTBALL_API_KEY: str = ''
    FOOTBALL_API_BASE_URL: str = 'https://v3.football.api-sports.io'

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )


settings = Settings()