# PAY_CMP_BAL_DIM_USAGES_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycmpbaldimusagesv-3347.html#paycmpbaldimusagesv-3347](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycmpbaldimusagesv-3347.html#paycmpbaldimusagesv-3347)

## Columns

- DEFINED_BALANCE_ID
- BALANCE_DIMENSION_ID
- DIMENSION_NAME
- BASE_DB_ITEM_SUFFIX
- LEGISLATIVE_DATA_GROUP_ID
- LEGISLATION_CODE
- BALANCE_TYPE_ID
- CURRENCY_CODE
- BALANCE_NAME

## Query

```sql
SELECT pdb.defined_balance_id, pbd.balance_dimension_id, pdu.dimension_name, pbd.base_db_item_suffix, pdu.legislative_data_group_id, pdu.legislation_code, pbt.balance_type_id, pbt.currency_code, pbt.balance_name FROM pay_defined_balances pdb, pay_balance_types_vl pbt, pay_balance_dimensions pbd, pay_dimension_usages_vl pdu WHERE pdb.balance_dimension_id = pbd.balance_dimension_id and pbd.balance_dimension_id = pdu.balance_dimension_id and pdb.balance_type_id = pbt.balance_type_id and pbd.base_db_item_suffix in ('_CORE_REL_YTD', '_CORE_REL_PTD', '_CORE_TRM_YTD', '_CORE_TRM_PTD', '_CORE_ASG_YTD', '_CORE_ASG_PTD')
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
