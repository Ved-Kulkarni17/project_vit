import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    DEBUG = os.getenv("DEBUG", False)

settings = Settings()