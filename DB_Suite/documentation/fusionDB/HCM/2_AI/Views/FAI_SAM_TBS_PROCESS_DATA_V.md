# FAI_SAM_TBS_PROCESS_DATA_V

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamtbsprocessdatav-4951.html#faisamtbsprocessdatav-4951](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamtbsprocessdatav-4951.html#faisamtbsprocessdatav-4951)

## Columns

- SEQUENCE_ID
- PROCESS_PRODUCT
- OBJECT_ID
- OBJECT_KEY
- PROCESS_TYPE
- PROCESS_NAME
- ID_METRIC
- PARENT_ID_METRIC
- PROCESS_STATUS
- LOAD
- LOAD_SUCCESS
- LOAD_ERROR
- PROCESSING_TIME
- THREAD_COUNT
- DAY
- START_TIME
- STOP_TIME
- PRODUCT
- PARAMETER
- PARAMETER_COMBINE
- RAW_DATA_ID
- ANOMALY_LOOP

## Query

```sql
select -1 sequence_id,product process_product, one_view_process_id object_id, object_key, process_type, process_name , id_metric, parent_id_metric, process_status, load, load_success, load_error, processing_time, thread_count, day, start_time, stop_time, product, parameter, parameter_combine, raw_data_id, anomaly_loop from fai_sam_one_view_process a where one_view_process_id not in (select one_view_process_id from fai_sam_sequence_object) and last_update_date >= SYS_EXTRACT_UTC(SYSTIMESTAMP) - interval '2' hour UNION ALL select b.sequence_id, c.product process_product , c.one_view_process_id object_id, c.object_key, c.process_type, c.process_name , c.id_metric, c.parent_id_metric, c.process_status, c.load, c.load_success, c.load_error, c.processing_time, c.thread_count, c.day, c.start_time, c.stop_time, c.product, c.parameter, c.parameter_combine, raw_data_id, anomaly_loop from fai_sam_sequence a, fai_sam_sequence_object b, fai_sam_one_view_process c where a.parent_sequence_id is not null and a.sequence_id = b.sequence_id and b.one_view_process_id = c.one_view_process_id and c.last_update_date >= SYS_EXTRACT_UTC(SYSTIMESTAMP) - interval '2' hour
```

---

[← Back to Index](../2_AI_Views_Index.md)
