import pandas as pd
from setup.connection import Connection
from datetime import datetime


class TransferData:
    def __init__(self, tb_name: str = "amazon", columns: list[str] = None, limit: int = 1000000):
        if columns is None:
            columns = ["book_id", "user_id", "review_score", "review_time"]
        # self.pg_conn = Connection().get_sqlalchemy_engine()
        self.pg_conn = Connection().get_connect()
        self.tb_name = tb_name
        self.columns = columns
        self.limit = limit
        self._data = None
        self.get_data()

    def get_data(self):
        self._data = pd.read_sql(
            f"select {','.join(self.columns)} from {self.tb_name} limit {self.limit}",
            self.pg_conn
        )
        print(self._data)

    def preparation(self):
        self._data = self._data.rename(
            columns={
                "review_score": "score",
                "review_time": "time"
            }
        )

    def save_dataset(self):
        self.preparation()
        self._data.to_csv(f'data/amazon_book.csv')
