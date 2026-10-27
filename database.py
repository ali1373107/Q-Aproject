import os 
from sqlalchemy import URL, create_engine 
from dotenv import load_dotenv
load_dotenv()
database_url = URL.create(
    drivername = "postgresql+psycopg2",
    username = "qanda_app",
    password = os.environ["DB_PASSWORD"],
    host = "localhost",
    port = 5432, 
    database = "qanda_db",
)
engine = create_engine(database_url, pool_pre_ping=True)