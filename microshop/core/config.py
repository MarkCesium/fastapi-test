from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = "postgresql+asyncpg://postgres:12345@localhost/microshop"
    db_echo: bool = True


settings: Settings = Settings()
