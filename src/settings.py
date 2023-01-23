from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    rollbar_key: str = Field(..., env='ROLLBAR_KEY')
    region: str = Field(..., env='REGION')

settings = Settings()