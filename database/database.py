import os
from peewee import PostgresqlDatabase
from dotenv import load_dotenv

load_dotenv()

database_uri = os.getenv('DATABASE_URI', '')
db = PostgresqlDatabase(database_uri)