# PAY_ACTION_PARAMETERS_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactionparametersvl-3993.html#payactionparametersvl-3993](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactionparametersvl-3993.html#payactionparametersvl-3993)

## Columns

- PARAMETER_NAME
- PARAMETER_VALUE

## Query

```sql
SELECT PAPV.PARAMETER_NAME , PAPV.PARAMETER_VALUE FROM PAY_ACTION_PARAM_VALUES PAPV WHERE pay_core_utils.get_pap_group_id = PAPV.ACTION_PARAM_GROUP_ID OR (PAPV.ACTION_PARAM_GROUP_ID = (SELECT PAPG.ACTION_PARAM_GROUP_ID FROM PAY_ACTION_PARAM_GROUPS PAPG WHERE ACTION_PARAM_GROUP_NAME = 'DEFAULT GROUP') AND not exists (SELECT null FROM PAY_ACTION_PARAM_VALUES PAPV2 WHERE PAPV2.PARAMETER_NAME = PAPV.PARAMETER_NAME AND PAPV2.ACTION_PARAM_GROUP_ID = pay_core_utils.get_pap_group_id))
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
