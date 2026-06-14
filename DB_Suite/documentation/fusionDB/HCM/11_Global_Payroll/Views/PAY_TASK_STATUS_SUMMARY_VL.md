# PAY_TASK_STATUS_SUMMARY_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytaskstatussummaryvl-5782.html#paytaskstatussummaryvl-5782](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytaskstatussummaryvl-5782.html#paytaskstatussummaryvl-5782)

## Columns

- HIGHLIGHT_NUM
- TILE_NUMBER
- TASK_TYPE
- SUMMARY_TYPE
- TOTAL
- OVERDUE
- TAKING_LONGER
- WITH_ERROR
- TILE_SIZE

## Query

```sql
select HIGHLIGHT_NUM , TILE_NUMBER, TASK_TYPE,SUMMARY_TYPE,TOTAL, OVERDUE, TAKING_LONGER, WITH_ERROR , sum(decode(HIGHLIGHT_NUM,1,1,2,1,3,1.5,4,2,2)) over (partition by summary_breakdown) tile_size from ( select ((CASE WHEN OVERDUE> 0 THEN 1 ELSE 0 END )+ (CASE WHEN TAKING_LONGER> 0 THEN 1 ELSE 0 END )+( CASE WHEN WITH_ERROR> 0 THEN 1 ELSE 0 END)) AS HIGHLIGHT_NUM , rownum TILE_NUMBER, TASK_TYPE,SUMMARY_TYPE,TOTAL, OVERDUE, TAKING_LONGER, WITH_ERROR,summary_breakdown from ( select summary_breakdown,TASK_TYPE,task_name SUMMARY_TYPE,count(*) as TOTAL, sum(decode(Due_Date,null,0,case when Due_Date<sysdate then 1 else 0 end)) OVERDUE, sum(decode(Expected_Time_Left,null,0,decode(Expected_Time_Left,'00:00:00',1,0))) TAKING_LONGER, sum(decode(Errors_and_Warnings,null,0,1)) WITH_ERROR from pay_task_status_vl where TASK_TYPE='AUTOMATIC' group by summary_breakdown,TASK_TYPE,task_name)) order by TILE_NUMBER
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
