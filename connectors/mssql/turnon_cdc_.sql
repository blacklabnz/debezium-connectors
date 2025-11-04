-- USE nxuevent;
-- EXEC sys.sp_cdc_enable_table @source_schema = 'dbo', @source_name = 'events_clone', @role_name = NULL;

SELECT name, is_cdc_enabled FROM sys.databases;

SELECT * FROM cdc.change_tables;

EXEC sys.sp_cdc_enable_table @source_schema = 'dbo', @source_name = 'events', @role_name = NULL, @supports_net_changes = 0, @capture_instance = 'dbo_events_v2';
GO

EXEC sys.sp_cdc_disable_table @source_schema = 'dbo', @source_name = 'events', @capture_instance = 'dbo_events';
GO

SELECT capture_instance, source_object_id, object_name(source_object_id) AS source_table_name
FROM cdc.change_tables;