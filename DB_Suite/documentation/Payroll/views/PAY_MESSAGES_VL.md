# PAY_MESSAGES_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paymessagesvl-7125.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paymessagesvl-7125.html)

## Columns

- MODULE_NAME
- FLOW_NAME
- FLOW_INSTANCE_ID
- STATUS
- TOTAL
- MESSAGE_TEXT
- TASK_INSTANCE_ID
- PROCESS
- MESSAGE_TEXT_CODE

## Query

```sql
select aaa.module_name, aaa.flow_name,aaa.flow_instance_id, MESSAGE_LEVEL as status,COUNT(*) total, nvl(bbb.message_text,nvl((select max(message_text) from FND_MESSAGES_VL fnm where fnm.MESSAGE_NAME=bbb.MESSAGE),MESSAGE)) as message_text, aaa.task_instance_id,PROCESS, MESSAGE message_text_code from PAY_task_STATUS_VL aaa, PAY_PAY_MSG_RESULTS_VL bbb where bbb.flow_id= aaa.flow_instance_id and bbb.task_instance_id=aaa.task_instance_id and bbb.MESSAGE_LEVEL in ('F','E','W') group by aaa.module_name, aaa.flow_name,aaa.flow_instance_id, MESSAGE_LEVEL , MESSAGE_TEXT ,aaa.task_instance_id,PROCESS, MESSAGE
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
