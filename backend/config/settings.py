"""
Application settings and configuration management.
Loads ALL configuration from environment variables (.env file).
NO SECRETS ARE HARDCODED HERE - everything comes from .env!
"""
from typing import List, Optional
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings - ALL values loaded from .env file.
    Never hardcode passwords or secrets here!
    
    All fields WITHOUT defaults are REQUIRED in .env
    All fields WITH defaults are OPTIONAL in .env
    """
    
    # ============================================================================
    # Application
    # ============================================================================
    APP_NAME: str  # Required in .env
    DEBUG: bool = False  # Optional, defaults to False
    ENVIRONMENT: str  # Required in .env
    
    # ============================================================================
    # Database - Choose MySQL OR PostgreSQL
    # ============================================================================
    ## CHANGE START
    DB_TYPE: str  # Required: "mysql" or "postgresql" from .env
    DB_HOST: str  # Required: from .env
    DB_PORT: int  # Required: from .env
    DB_USER: str  # Required: from .env
    DB_PASSWORD: str  # Required: from .env - NEVER HARDCODE!
    DB_NAME: str  # Required: from .env
    ## CHANGE END
    
    @property
    def DATABASE_URL(self) -> str:
        """Build database URL based on DB_TYPE"""
        if self.DB_TYPE == "mysql":
            # MySQL async URL
            return f"mysql+aiomysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        elif self.DB_TYPE == "postgresql":
            # PostgreSQL async URL
            return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        else:
            raise ValueError(f"Unsupported DB_TYPE: {self.DB_TYPE}. Use 'mysql' or 'postgresql'")
    
    # ============================================================================
    # Security
    # ============================================================================
    SECRET_KEY: str  # Required: from .env - NEVER HARDCODE!
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # Optional: defaults to 30 minutes
    
    # ============================================================================
    # CORS
    # ============================================================================
    ALLOWED_ORIGINS: List[str]  # Required: from .env (comma-separated string)
    
    @field_validator("ALLOWED_ORIGINS", mode="before")
    @classmethod
    def parse_cors_origins(cls, v):
        """Parse comma-separated string into list"""
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v
    
    # ============================================================================
    # File Uploads
    # ============================================================================
    MAX_UPLOAD_SIZE: int = 10485760  # Optional: defaults to 10MB
    UPLOAD_DIR: str = "uploads"  # Optional: defaults to "uploads"
    
    # ============================================================================
    # Pydantic Config - Load from .env file
    # ============================================================================
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True
    )


# ============================================================================
# Global settings instance
# ============================================================================
settings = Settings()