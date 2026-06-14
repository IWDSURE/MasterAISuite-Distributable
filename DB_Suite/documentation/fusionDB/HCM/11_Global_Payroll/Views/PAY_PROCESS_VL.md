# PAY_PROCESS_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payprocessvl-5805.html#payprocessvl-5805](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payprocessvl-5805.html#payprocessvl-5805)

## Columns

- FLOW_INSTANCE_ID
- FLOW_NAME
- CHECKLIST_NAME
- TASK_INSTANCE_ID
- PROCESS_ID
- NAME
- STATUS
- SCHEDULED_TIME
- START_TIME
- FINISH_TIME
- LOG_FLAG
- ELAPSED_TIME
- WAIT_TIME
- PARENTREQUESTID
- LOG_URL

## Query

```sql
SELECT FLOW_INSTANCE_ID,FLOW_NAME,CHECKLIST_NAME , TASK_INSTANCE_ID,PROCESS_ID, NAME, STATUS, SCHEDULED_TIME, START_TIME, FINISH_TIME, LOG_FLAG, ELAPSED_TIME, WAIT_TIME, PARENTREQUESTID,LOG_URL FROM ( SELECT null as flow_instance_id,null as flow_name,null as CHECKLIST_NAME ,null as task_instance_id, null AS Process_Id, null AS Name, null AS Status, null AS Scheduled_Time, null AS Start_Time, null AS Finish_Time, null as log_flag, null AS Elapsed_Time, null AS Wait_Time, null as parentrequestid, null log_url from hr_lookups where rownum=1 ) ORDER BY PROCESS_ID asc
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
