from dotenv import load_dotenv, dotenv_values
import requests

connector_name = "mssql_connector_1_9"
load_dotenv(dotenv_path="../../.env")
env = dotenv_values()

body= f"""
{{
  "name": "{connector_name}",
  "config": {{
    "snapshot.mode": "schema_only",
    "connector.class": "io.debezium.connector.sqlserver.SqlServerConnector",
    "database.hostname": "{env['mssql_server_hostname']}",
    "database.port": 1433,
    "database.user": "{env['mssql_username']}",
    "database.password": "{env['mssql_password']}",
    "database.dbname": "{env['mssql_database']}",
    "database.server.name": "{env['mssql_server_name']}",
    "table.include.list": "dbo.events",
    "decimal.handling.mode": "string",
    "tombstones.on.delete": false,
    "database.history.kafka.bootstrap.servers": "{env['eh_hostname']}:9093",
    "database.history.kafka.topic": "dbhistory",
    "database.history.consumer.security.protocol": "SASL_SSL",
    "database.history.consumer.sasl.mechanism": "PLAIN",
    "database.history.consumer.sasl.jaas.config": "org.apache.kafka.common.security.plain.PlainLoginModule required username=\\"{env['eh_username']}\\" password=\\"{env['eh_constr']}\\";",
    "database.history.producer.security.protocol": "SASL_SSL",
    "database.history.producer.sasl.mechanism": "PLAIN",
    "database.history.producer.sasl.jaas.config": "org.apache.kafka.common.security.plain.PlainLoginModule required username=\\"{env['eh_username']}\\" password=\\"{env['eh_constr']}\\";"
  }}
}}
"""
print(body)

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


# "transforms": "Reroute",
# "transforms.Reroute.type": "io.debezium.transforms.ByLogicalTableRouter",
# "transforms.Reroute.topic.regex": "(.*)",
# "transforms.Reroute.topic.replacement": "events",