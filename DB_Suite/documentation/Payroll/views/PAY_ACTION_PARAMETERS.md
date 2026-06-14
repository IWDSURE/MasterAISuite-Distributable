# PAY_ACTION_PARAMETERS

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactionparameters-6636.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactionparameters-6636.html)

## Columns

- PARAMETER_NAME
- PARAMETER_VALUE

## Query

```sql
SELECT PAPV.PARAMETER_NAME, PAPV.PARAMETER_VALUE FROM PAY_ACTION_PARAM_VALUES PAPV WHERE (PAPV.ACTION_PARAM_GROUP_ID = pay_core_utils.get_pap_group_id OR (PAPV.ACTION_PARAM_GROUP_ID = (SELECT PAPG.ACTION_PARAM_GROUP_ID FROM PAY_ACTION_PARAM_GROUPS PAPG WHERE ACTION_PARAM_GROUP_NAME = 'DEFAULT GROUP') AND not exists (SELECT null FROM PAY_ACTION_PARAM_VALUES PAPV2 WHERE PAPV2.PARAMETER_NAME = PAPV.PARAMETER_NAME AND PAPV2.ACTION_PARAM_GROUP_ID = pay_core_utils.get_pap_group_id ))) union select pftp.base_parameter_name PARAMETER_NAME, pftpv.flow_task_param_value PARAMETER_VALUE from pay_requests prq, pay_flow_task_parameters pftp, pay_flow_task_param_vals pftpv, hcm_lookups plk where prq.call_id = pay_core_utils.get_parent_ess_id and pay_core_utils.get_parent_ess_id is not null and pftpv.flow_task_param_value is not null and prq.call_type='FLOW_ESS' and prq.flow_task_instance_id = pftpv.flow_task_instance_id and pftpv.base_flow_task_param_id = pftp.flow_task_param_id and plk.lookup_type = 'PAY_ACTION_PARAMETER_TYPE' and plk.lookup_code = pftp.base_parameter_name and not exists (SELECT null FROM PAY_ACTION_PARAM_VALUES PAPV WHERE PAPV.PARAMETER_NAME = pftp.base_parameter_name AND (PAPV.ACTION_PARAM_GROUP_ID = pay_core_utils.get_pap_group_id OR (PAPV.ACTION_PARAM_GROUP_ID = (SELECT PAPG.ACTION_PARAM_GROUP_ID FROM PAY_ACTION_PARAM_GROUPS PAPG WHERE ACTION_PARAM_GROUP_NAME = 'DEFAULT GROUP') AND not exists (SELECT null FROM PAY_ACTION_PARAM_VALUES PAPV2 WHERE PAPV2.PARAMETER_NAME = PAPV.PARAMETER_NAME AND PAPV2.ACTION_PARAM_GROUP_ID = pay_core_utils.get_pap_group_id ))))
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
