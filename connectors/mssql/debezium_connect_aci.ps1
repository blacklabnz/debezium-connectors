$resourceGroup="resource-group-name"
$location="Australiaeast"
$vnetName="vnet-name"
$subnetName="container-subnet"
$containerName="debeziumnxu"
$image="debezium/connect:1.9"
$containerGroup="debeziumnxugroupprv"
$osType = "Linux"
$cpu = 2 
$memory = 4
$ehName="nxuevent"
$EH_CONNECTION_STRING="eventhub-connection-string"
$username = '$ConnectionString'


az container create `
    --resource-group $resourceGroup `
    --name $containerGroup `
    --image $image `
    --location $location `
    --cpu $cpu `
    --memory $memory `
    --os-type $osType `
    --ports 8083 `
    --environment-variables `
        LOG_LEVEL=DEBUG `
        BOOTSTRAP_SERVERS=$ehName.servicebus.windows.net:9093 `
        GROUP_ID=dbzium-group `
        CONFIG_STORAGE_TOPIC=debezium_configs `
        OFFSET_STORAGE_TOPIC=debezium_offsets `
        STATUS_STORAGE_TOPIC=debezium_status `
        CONNECT_KEY_CONVERTER_SCHEMAS_ENABLE=false `
        CONNECT_VALUE_CONVERTER_SCHEMAS_ENABLE=true `
        CONNECT_REQUEST_TIMEOUT_MS=60000 `
        CONNECT_SECURITY_PROTOCOL=SASL_SSL `
        CONNECT_SASL_MECHANISM=PLAIN `
        CONNECT_SASL_JAAS_CONFIG="org.apache.kafka.common.security.plain.PlainLoginModule required username=\""$username\"" password=\""$EH_CONNECTION_STRING\"";" `
        CONNECT_PRODUCER_SECURITY_PROTOCOL=SASL_SSL `
        CONNECT_PRODUCER_SASL_MECHANISM=PLAIN `
        CONNECT_PRODUCER_SASL_JAAS_CONFIG="org.apache.kafka.common.security.plain.PlainLoginModule required username=\""$username\"" password=\""$EH_CONNECTION_STRING\"";" `
        CONNECT_CONSUMER_SECURITY_PROTOCOL=SASL_SSL `
        CONNECT_CONSUMER_SASL_MECHANISM=PLAIN `
        CONNECT_CONSUMER_SASL_JAAS_CONFIG="org.apache.kafka.common.security.plain.PlainLoginModule required username=\""$username\"" password=\""$EH_CONNECTION_STRING\"";" `
    --vnet $vnetName `
    --subnet $subnetName `
        # --ip-address public `
