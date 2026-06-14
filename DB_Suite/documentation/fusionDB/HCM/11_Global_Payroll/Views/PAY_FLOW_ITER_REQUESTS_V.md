# PAY_FLOW_ITER_REQUESTS_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowiterrequestsv-3339.html#payflowiterrequestsv-3339](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowiterrequestsv-3339.html#payflowiterrequestsv-3339)

## Columns

- FLOW_TASK_INSTANCE_ID
- PAY_REQUEST_ID
- COUNTER
- BASE_TASK_PARAMETER_ID
- BASE_TASK_PARAMETER_VALUE

## Query

```sql
SELECT a.flow_task_instance_id, b.value_1 PAY_REQUEST_ID, b.value_2 COUNTER, b.value_3 BASE_TASK_PARAMETER_ID, b.value_4 BASE_TASK_PARAMETER_VALUE FROM pay_flow_task_instances a , table(pay_process_flow_utils.get_tab_pay_requests_tf(flow_task_instance_id)) b
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
