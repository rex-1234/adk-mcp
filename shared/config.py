from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    aws_access_key_id: SecretStr | None = None
    aws_secret_access_key: SecretStr | None = None
    aws_region: str
    s3_bucket: str
    internal_service_token: SecretStr | None = None
    gemini_api_key: SecretStr | None = None
    storage_mcp_url: str
    document_mcp_url: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()
