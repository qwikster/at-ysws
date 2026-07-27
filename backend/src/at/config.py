from pydantic_settings import BaseSettings, SettingsConfigDict

_config = None
_secret = None

class Config(BaseSettings):
    devmode: bool = False
    host: str = "0.0.0.0"
    port: int = 8000

    model_config = SettingsConfigDict(env_file = "app.config", env_file_encoding="utf-8")

class Secret(BaseSettings):
    db_url: str
    hca_id: str
    hca_secret: str

    airtable_key: str
    airtable_base_id: str

    model_config = SettingsConfigDict(env_file = ".env", env_file_encoding="utf-8")

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
