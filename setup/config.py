from pathlib import Path
from pydantic import BaseSettings

__all__ = ["env_config"]


class Config(BaseSettings):
    # postgres host
    POSTGRES_USER = "postgres"
    POSTGRES_PASSWORD = "1234"
    POSTGRES_DB = "adin_mlops"
    POSTGRES_HOST = "127.0.0.1"
    POSTGRES_PORT = 5432
    POSTGRES_TABLE_NAME = 'amazon'
    POSTGRES_DB_SCHEMA = 'public'

    # MINIO
    MINIO_ENDPOINT = 'http://192.168.10.121:9000'
    MINIO_BUCKET_NAME = 'dvc'
    AWS_ACCESS_KEY_ID = 'minio'
    AWS_SECRET_ACCESS_KEY = 'minio123'
    MINIO_REGISTRY_PATH = ''

    # feast
    FEAST_S3_ENDPOINT_URL = 'http://192.168.10.121:9000'
    FEAST_PROJECT_NAME = 'amazon_book'
    FEAST_PROVIDER = 'local'

    class Config:
        case_sensitive = False
        BASE_DIR = Path(__file__).resolve().parent.parent
        env_file = (str(BASE_DIR) + "/.env").replace("//", "/")
        env_file_encoding = "utf-8"


env_config = Config()
