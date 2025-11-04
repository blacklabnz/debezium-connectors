$resourceGroup="resource-group-name"
$location="Australiaeast"
$vnetName="vnet-name"
$subnetName="container-subnet"
$containerName="debeziumnxu"
$image="debezium/connect:1.9"
$containerGroup="debeziumnxugrouppub"
$osType = "Linux"
$cpu = 2 
$memory = 4
$ehName="nameofeventhub"
$EH_CONNECTION_STRING="connectionstringofeventhub"
$username = '$ConnectionString'
$bootstrap_servers="$ehName.servicebus.windows.net:9093"
# $bootstrap_servers="esehsyjmsgh7v10ppgq0re.servicebus.windows.net:9093"


docker run -it --name connect -p 8083:8083 `
    -e GROUP_ID=cdc-group `
    -e LOG_LEVEL=DEBUG `
    -e BOOTSTRAP_SERVERS=$bootstrap_servers `
    -e CONFIG_STORAGE_TOPIC=debezium_configs `
    -e OFFSET_STORAGE_TOPIC=debezium_offsets `
    -e STATUS_STORAGE_TOPIC=debezium_status `
    -e CONFIG_STORAGE_REPLICATION_FACTOR=1 `
    -e OFFSET_STORAGE_REPLICATION_FACTOR=1 `
    -e STATUS_STORAGE_REPLICATION_FACTOR=1 `
    -e CONNECT_KEY_CONVERTER_SCHEMAS_ENABLE=false `
    -e CONNECT_VALUE_CONVERTER_SCHEMAS_ENABLE=false `
    -e CONNECT_REQUEST_TIMEOUT_MS=60000 `
    -e CONNECT_SECURITY_PROTOCOL=SASL_SSL `
    -e CONNECT_SASL_MECHANISM=PLAIN `
    -e CONNECT_SASL_JAAS_CONFIG="org.apache.kafka.common.security.plain.PlainLoginModule required username=\""$username\"" password=\""$EH_CONNECTION_STRING\"";" `
    -e CONNECT_PRODUCER_SECURITY_PROTOCOL=SASL_SSL `
    -e CONNECT_PRODUCER_SASL_MECHANISM=PLAIN `
    -e CONNECT_PRODUCER_SASL_JAAS_CONFIG="org.apache.kafka.common.security.plain.PlainLoginModule required username=\""$username\"" password=\""$EH_CONNECTION_STRING\"";" `
    -e CONNECT_CONSUMER_SECURITY_PROTOCOL=SASL_SSL `
    -e CONNECT_CONSUMER_SASL_MECHANISM=PLAIN `
    -e CONNECT_CONSUMER_SASL_JAAS_CONFIG="org.apache.kafka.common.security.plain.PlainLoginModule required username=\""$username\"" password=\""$EH_CONNECTION_STRING\"";" `
$image
