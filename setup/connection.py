import psycopg2
from sqlalchemy import create_engine
from .config import env_config


class Connection:
    def __init__(self):
        self.conn = None
        self.engine = None

    def get_connect(self):
        try:
            self.conn = psycopg2.connect(
                host=env_config.POSTGRES_HOST,
                dbname=env_config.POSTGRES_DB,
                user=env_config.POSTGRES_USER,
                password=env_config.POSTGRES_PASSWORD,
            )
        except Exception as error:
            raise Exception(error)
        return self.conn

    def get_sqlalchemy_engine(self):
        self.engine = create_engine(
            f'postgresql://{env_config.POSTGRES_USER}'
            f':{env_config.POSTGRES_PASSWORD}@{env_config.POSTGRES_HOST}'
            f':{env_config.POSTGRES_PORT}/{env_config.POSTGRES_DB}'
        )
        return self.engine
