# PAY_PROCESS_TASKS_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payprocesstasksv-5019.html#payprocesstasksv-5019](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payprocesstasksv-5019.html#payprocesstasksv-5019)

## Columns

- PAYROLL_ID
- LOOKUP_TYPE
- LOOKUP_CODE
- ACTION_TYPE
- STATUS
- LOOKUP_TYPE1
- LOOKUP_CODE1
- PAYROLL_NAME
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- PAYROLL_ACTION_ID
- PROCESSDATE
- DATE_EARNED
- STATUTORY_PERIOD_NAME
- STATUTORY_TIME_PERIOD_ID
- PERIOD_NUM
- EARNINGS_PERIOD_NAME
- EARNINGS_TIME_PERIOD_ID
- EARNINGS_PERIOD_NUM
- MEANING
- LEGISLATIVE_DATA_GROUP_ID
- PAYROLL_ID1
- TASK_NAME

## Query

```sql
SELECT PayrollActionPEO.PAYROLL_ID, HcmLookupPEO.LOOKUP_TYPE, HcmLookupPEO.LOOKUP_CODE, HcmLookupPEO1.MEANING AS ACTION_TYPE, HcmLookupPEO.MEANING AS STATUS, HcmLookupPEO1.LOOKUP_TYPE AS LOOKUP_TYPE1, HcmLookupPEO1.LOOKUP_CODE AS LOOKUP_CODE1, PayrollDPEO.PAYROLL_NAME, PayrollDPEO.EFFECTIVE_START_DATE, PayrollDPEO.EFFECTIVE_END_DATE, PayrollActionPEO.PAYROLL_ACTION_ID, PayrollActionPEO.EFFECTIVE_DATE as ProcessDate, PayrollActionPEO.DATE_EARNED, TimePeriodPEO.PERIOD_NAME AS STATUTORY_PERIOD_NAME, TimePeriodPEO.TIME_PERIOD_ID AS STATUTORY_TIME_PERIOD_ID, TimePeriodPEO.PERIOD_NUM AS PERIOD_NUM, TimePeriodPEOEarn.PERIOD_NAME AS EARNINGS_PERIOD_NAME, TimePeriodPEOEarn.TIME_PERIOD_ID AS EARNINGS_TIME_PERIOD_ID, TimePeriodPEOEarn.PERIOD_NUM AS EARNINGS_PERIOD_NUM, HcmLookupPEO.MEANING, ldg.legislative_data_group_id, PayrollDPEO.PAYROLL_ID AS PAYROLL_ID1, nvl(pt.task_name,HcmLookupPEO1.MEANING) as task_name FROM PAY_PAYROLL_ACTIONS PayrollActionPEO, PAY_ALL_PAYROLLS_F PayrollDPEO, HCM_LOOKUPS HcmLookupPEO, HCM_LOOKUPS HcmLookupPEO1, PAY_TIME_PERIODS TimePeriodPEO, PAY_TIME_PERIODS TimePeriodPEOEarn, pay_requests prq, fusion.pay_task_actions pta, fusion.pay_tasks_vl pt, fusion.per_legislative_data_groups ldg WHERE PayrollActionPEO.PAYROLL_ID = PayrollDPEO.PAYROLL_ID (+) AND PayrollActionPEO.EFFECTIVE_DATE BETWEEN PayrollDPEO.EFFECTIVE_START_DATE (+) AND PayrollDPEO.EFFECTIVE_END_DATE (+) AND HcmLookupPEO1.LOOKUP_TYPE = 'ACTION_TYPE' AND HcmLookupPEO1.LOOKUP_CODE = PayrollActionPEO.ACTION_TYPE AND HcmLookupPEO.LOOKUP_TYPE = 'PAY_ACTION_STATUS' AND HcmLookupPEO.LOOKUP_CODE = PayrollActionPEO.ACTION_STATUS AND PayrollActionPEO.dedn_time_period_id = TimePeriodPEO.TIME_PERIOD_ID (+) AND PayrollActionPEO.earn_time_period_id = TimePeriodPEOEarn.TIME_PERIOD_ID (+) AND prq.pay_request_id (+) = PayrollActionPEO.pay_request_id AND prq.pay_task_action_id = pta.task_action_id (+) AND pta.base_task_id = pt.task_id (+) and PayrollActionPEO.legislative_data_group_id = ldg.legislative_data_group_id (+) AND ((pt.legislative_data_group_id IS NOT NULL AND pt.legislation_code IS NULL AND pt.legislative_data_group_id = ldg.legislative_data_group_id) OR (pt.legislation_code is not null AND pt.legislative_data_group_id is null AND pt.legislation_code =ldg.legislation_code AND ( NOT EXISTS ( SELECT TASK_ID FROM fusion.PAY_TASK_ACTIONS_VL c1 WHERE pt.BASE_TASK_ID = c1.BASE_TASK_ID AND (c1.legislative_data_group_id is not null AND c1.legislation_code is null AND c1.legislative_data_group_id = ldg.legislative_data_group_id )))) or ( pt.legislative_data_group_id is null AND pt.legislation_code is null AND ( NOT EXISTS ( SELECT TASK_ID FROM fusion.PAY_TASK_ACTIONS_VL c2 WHERE pt.BASE_TASK_ID = c2.BASE_TASK_ID AND (( c2.legislative_data_group_id IS NOT NULL AND c2.legislation_code IS NULL AND c2.legislative_data_group_id = ldg.legislative_data_group_id) OR ( c2.legislation_code IS NOT NULL AND c2.legislative_data_group_id IS NULL AND c2.legislation_code = ldg.legislation_code ))))))
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
