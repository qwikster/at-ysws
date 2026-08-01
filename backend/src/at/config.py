from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

DIR = Path(__file__).resolve().parent.parent.parent

_config = None
_secret = None

class Config(BaseSettings):
    devmode: bool = False
    host: str = "0.0.0.0"
    port: int = 8000

    model_config = SettingsConfigDict(env_file = DIR / "app.config", env_file_encoding="utf-8")

class Secret(BaseSettings):
    db_url: str | None = None
    hca_id: str | None = None
    hca_secret: str | None = None

    airtable_key: str | None = None
    airtable_base_id: str | None = None

    model_config = SettingsConfigDict(env_file = DIR / ".env", env_file_encoding="utf-8")

def config() -> Config:
    global _config
    if _config is None:
        _config = Config()
    return _config

def secret() -> Secret:
    global _secret
    if _secret is None:
        _secret = Secret()
    return _secret
