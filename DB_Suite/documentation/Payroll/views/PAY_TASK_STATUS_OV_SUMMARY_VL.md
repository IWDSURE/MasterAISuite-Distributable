# PAY_TASK_STATUS_OV_SUMMARY_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytaskstatusovsummaryvl-8528.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytaskstatusovsummaryvl-8528.html)

## Columns

- FLOW_INSTANCE_ID
- FLOW_NAME
- STATUS
- TASK_NUM

## Query

```sql
select FLOW_INSTANCE_ID, FLOW_NAME,DECODE(TASK_STATUS,'COMPLETE','Completed','COMPLETE_WITH_ISSUES','Completed','SKIPPED', 'Skipped','Pending') as status, COUNT(*) Task_Num from PAY_TASK_STATUS_VL GROUP BY FLOW_INSTANCE_ID,FLOW_NAME,DECODE(TASK_STATUS,'COMPLETE','Completed','COMPLETE_WITH_ISSUES','Completed','SKIPPED', 'Skipped','Pending')
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
