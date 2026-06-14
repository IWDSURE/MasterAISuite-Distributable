# PAY_HISTORY_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payhistoryvl-3010.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payhistoryvl-3010.html)

## Columns

- FLOW_NAME
- FLOW_INSTANCE_ID
- SUBMITTED_ON
- NUMBER_OF_RECORDS
- TIME_TAKEN

## Query

```sql
select flow_name, flow_instance_id, sysdate submitted_on, 1000 number_of_records, '00:00:10' time_taken from PAY_FLOW_STATUS_VL
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
