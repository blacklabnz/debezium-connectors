from dotenv import load_dotenv, dotenv_values
import requests

connector_name = "pg_connector_3_1_2"
load_dotenv(dotenv_path="../../.env")
env = dotenv_values()

body= f"""
{{
  "name": "{connector_name}",
  "config": {{
    "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
    "snapshot.mode": "always",
    "slot.name": "pg_slot",
    "plugin.name": "pgoutput",
    "topic.prefix": "pg",
    "database.dbname": "{env['pg_database']}",
    "database.hostname": "{env['pg_server_hostname']}",
    "database.port": 5432,
    "database.user": "{env['pg_username']}",
    "database.password": "{env['pg_password']}",
    "tombstones.on.delete": false
  }}
}}
"""

existing_connector = requests.get(
    url=f"http://{env['kafka_connect_host']}:8083/connectors/{connector_name}",
    headers={'Accept': 'application/json', 'Content-type': 'application/json'}
)

if existing_connector:
    status = requests.get(
        url=f"http://{env['kafka_connect_host']}:8083/connectors/{connector_name}/status",
        headers={'Accept': 'application/json', 'Content-type': 'application/json'}
    )
    print(status.json())
else:
    connector = requests.post(
        url=f"http://{env['kafka_connect_host']}:8083/connectors/", 
        headers={'Accept': 'application/json', 'Content-type': 'application/json'}, 
        data=body)
    print(connector.json())