from dotenv import load_dotenv, dotenv_values
import requests

connector_name = "mssql_connector_3_1_2"
load_dotenv(dotenv_path="../../.env")
env = dotenv_values()
recreate = False

body= f"""
{{
  "name": "{connector_name}",
  "config": {{
    "connector.class": "io.debezium.connector.sqlserver.SqlServerConnector",
    "tasks.max": "1",
    "topic.prefix": "nxu",
    "snapshot.mode": "initial",
    "database.hostname": "{env['mssql_server_hostname']}",
    "database.port": "1433",
    "database.user": "{env['mssql_username']}",
    "database.password": "{env['mssql_password']}",
    "database.names": "{env['mssql_database']}",
    "database.server.name": "{env['mssql_server_name']}",
    "table.include.list": "dbo.events,dbo.events_clone",
    "schema.history.internal.kafka.bootstrap.servers": "{env['eh_hostname']}:9093",
    "schema.history.internal.kafka.topic": "schemahistory",
    "schema.history.internal.consumer.security.protocol": "SASL_SSL",
    "schema.history.internal.consumer.sasl.mechanism": "PLAIN",
    "schema.history.internal.consumer.sasl.jaas.config": "org.apache.kafka.common.security.plain.PlainLoginModule required username=\\"{env['eh_username']}\\" password=\\"{env['eh_constr']}\\";",
    "schema.history.internal.producer.security.protocol": "SASL_SSL",
    "schema.history.internal.producer.sasl.mechanism": "PLAIN",
    "schema.history.internal.producer.sasl.jaas.config": "org.apache.kafka.common.security.plain.PlainLoginModule required username=\\"{env['eh_username']}\\" password=\\"{env['eh_constr']}\\";"
  }}
}}
"""
print(body)

existing_connector = requests.get(
    url=f"http://{env['kafka_connect_host']}:8083/connectors/{connector_name}",
    headers={'Accept': 'application/json', 'Content-type': 'application/json'}
)

if existing_connector:
    if recreate:
        del_connector = requests.delete(
            url=f"http://{env['kafka_connect_host']}:8083/connectors/{connector_name}",
            headers={'Accept': 'application/json', 'Content-type': 'application/json'}
        )
        print(del_connector)
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
