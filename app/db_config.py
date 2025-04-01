from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine("postgresql+psycopg2://postgres:root@127.0.0.1:5432/mydb")

def app():
    with engine.connect() as conn:
        stmt = text("select * from pg_database")
        print(conn.execute(stmt).fetchall())










