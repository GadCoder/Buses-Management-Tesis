import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

print(os.getenv("DATABASE_URL"))


class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./sql_app.db")


settings = Settings()
