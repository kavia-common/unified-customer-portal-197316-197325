import os
from functools import lru_cache
from typing import Optional

from pydantic import BaseModel


class Settings(BaseModel):
    """
    Centralized application settings. Populated from environment variables.
    """
    API_PREFIX: str = "/api/v1"
    FRONTEND_ORIGIN: Optional[str] = None
    FEATURE_FLAGS: Optional[str] = None

    # Align with provided env names for this container
    REACT_APP_API_BASE: Optional[str] = None
    REACT_APP_BACKEND_URL: Optional[str] = None
    REACT_APP_FRONTEND_URL: Optional[str] = None
    REACT_APP_WS_URL: Optional[str] = None
    REACT_APP_NODE_ENV: Optional[str] = None
    REACT_APP_NEXT_TELEMETRY_DISABLED: Optional[str] = None
    REACT_APP_ENABLE_SOURCE_MAPS: Optional[str] = None
    REACT_APP_PORT: Optional[str] = None
    REACT_APP_TRUST_PROXY: Optional[str] = None
    REACT_APP_LOG_LEVEL: Optional[str] = None
    REACT_APP_HEALTHCHECK_PATH: Optional[str] = None
    REACT_APP_FEATURE_FLAGS: Optional[str] = None
    REACT_APP_EXPERIMENTS_ENABLED: Optional[str] = None

    @classmethod
    def from_env(cls) -> "Settings":
        # Map specific envs into settings
        api_prefix = os.getenv("API_PREFIX", "/api/v1")
        frontend_origin = os.getenv("FRONTEND_ORIGIN") or os.getenv("REACT_APP_FRONTEND_URL")
        feature_flags = os.getenv("FEATURE_FLAGS") or os.getenv("REACT_APP_FEATURE_FLAGS")
        kwargs = {
            "API_PREFIX": api_prefix,
            "FRONTEND_ORIGIN": frontend_origin,
            "FEATURE_FLAGS": feature_flags,
            "REACT_APP_API_BASE": os.getenv("REACT_APP_API_BASE"),
            "REACT_APP_BACKEND_URL": os.getenv("REACT_APP_BACKEND_URL"),
            "REACT_APP_FRONTEND_URL": os.getenv("REACT_APP_FRONTEND_URL"),
            "REACT_APP_WS_URL": os.getenv("REACT_APP_WS_URL"),
            "REACT_APP_NODE_ENV": os.getenv("REACT_APP_NODE_ENV"),
            "REACT_APP_NEXT_TELEMETRY_DISABLED": os.getenv("REACT_APP_NEXT_TELEMETRY_DISABLED"),
            "REACT_APP_ENABLE_SOURCE_MAPS": os.getenv("REACT_APP_ENABLE_SOURCE_MAPS"),
            "REACT_APP_PORT": os.getenv("REACT_APP_PORT"),
            "REACT_APP_TRUST_PROXY": os.getenv("REACT_APP_TRUST_PROXY"),
            "REACT_APP_LOG_LEVEL": os.getenv("REACT_APP_LOG_LEVEL"),
            "REACT_APP_HEALTHCHECK_PATH": os.getenv("REACT_APP_HEALTHCHECK_PATH"),
            "REACT_APP_FEATURE_FLAGS": os.getenv("REACT_APP_FEATURE_FLAGS"),
            "REACT_APP_EXPERIMENTS_ENABLED": os.getenv("REACT_APP_EXPERIMENTS_ENABLED"),
        }
        return cls(**kwargs)


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """
    Get cached application settings.

    Returns:
        Settings: The cached settings object built from environment variables.
    """
    return Settings.from_env()
