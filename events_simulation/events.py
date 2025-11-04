import time
import urllib
import models 
import funkybob
import random
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import TIMESTAMP
from datetime import datetime
from zoneinfo import ZoneInfo
from dotenv import load_dotenv, dotenv_values

load_dotenv(dotenv_path="../../.env")
env = dotenv_values()

odbc_str = f'DRIVER={env["mssql_driver"]};SERVER={env["mssql_server_hostname"]};PORT=1433;UID={env["mssql_username"]};DATABASE={env["mssql_database"]};PWD={env["mssql_password"]}'
connect_str = 'mssql+pyodbc:///?odbc_connect=' + urllib.parse.quote_plus(odbc_str)

# connect_str = f"postgresql://{env['pg_username']}:{env['pg_password']}@{env['pg_server']}/{env['pg_database']}"

engine = create_engine(connect_str)

# Create all defined tables in the engine
models.Base.metadata.create_all(engine, checkfirst=True)

# Create a session factory
Session = sessionmaker(bind=engine)
session = Session()

now_aware_local = datetime.now(ZoneInfo("Pacific/Auckland"))
unique_name = funkybob.UniqueRandomNameGenerator()
it = iter(unique_name)

i = 0
while i < 2:
    name=next(it)
    event = models.Events(user_name=name, timestamp=now_aware_local, email=f"{name.lower()}@{random.choice(["example", "sample", "mock"])}.com")
    time.sleep(5)
    name=next(it)
    session.add(event)
    event_clone = models.Events_Clone(user_name=name, timestamp=now_aware_local)
    session.add(event_clone)
    session.commit()
    time.sleep(5)
    i += 1