$resourceGroup="resource-group-name"
$location="Australiaeast"
$vnetName="vnet-name"
$subnetName="container-subnet"
$containerName="debeziumnxu"
$image="debezium/connect:3.0.0.Final"
$containerGroup="debeziumnxugrouppub"
$osType = "Linux"
$cpu = 2 
$memory = 4
$ehName="nxuevent"
$EH_CONNECTION_STRING="connectionstringofeventhub"
$username = '$ConnectionString'
$bootstrap_servers="$ehName.servicebus.windows.net:9093"
# $bootstrap_servers="esehsyjmsgh7v10ppgq0re.servicebus.windows.net:9093"


docker run -it --name connect -p 8083:8083 `
    -e GROUP_ID=cdc-group `
    -e LOG_LEVEL=INFO `
    -e BOOTSTRAP_SERVERS=$bootstrap_servers `
    -e CONFIG_STORAGE_TOPIC=debezium_configs `
    -e OFFSET_STORAGE_TOPIC=debezium_offsets `
    -e STATUS_STORAGE_TOPIC=debezium_status `
    -e KEY_CONVERTER_SCHEMAS_ENABLE=false `
    -e VALUE_CONVERTER_SCHEMAS_ENABLE=false `
    -e REQUEST_TIMEOUT_MS=60000 `
    -e SECURITY_PROTOCOL=SASL_SSL `
    -e SASL_MECHANISM=PLAIN `
    -e SASL_JAAS_CONFIG="org.apache.kafka.common.security.plain.PlainLoginModule required username=\""$username\"" password=\""$EH_CONNECTION_STRING\"";" `
    -e PRODUCER_SECURITY_PROTOCOL=SASL_SSL `
    -e PRODUCER_SASL_MECHANISM=PLAIN `
    -e PRODUCER_SASL_JAAS_CONFIG="org.apache.kafka.common.security.plain.PlainLoginModule required username=\""$username\"" password=\""$EH_CONNECTION_STRING\"";" `
    -e CONSUMER_SECURITY_PROTOCOL=SASL_SSL `
    -e CONSUMER_SASL_MECHANISM=PLAIN `
    -e CONSUMER_SASL_JAAS_CONFIG="org.apache.kafka.common.security.plain.PlainLoginModule required username=\""$username\"" password=\""$EH_CONNECTION_STRING\"";" `
$image