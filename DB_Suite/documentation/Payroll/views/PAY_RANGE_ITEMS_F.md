# PAY_RANGE_ITEMS_F

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrangeitemsf-6347.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrangeitemsf-6347.html)

## Columns

- RANGE_ITEM_ID
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- VALUE_DEFN_ID
- LOW_VALUE
- LOW_VALUE_TEXT
- HIGH_VALUE
- HIGH_VALUE_TEXT
- CALC_TYPE_ID
- VALUE1
- VALUE2
- VALUE3
- SOURCE_TYPE
- SOURCE_ID
- ENTERPRISE_ID
- LEGISLATION_CODE
- LEGISLATIVE_DATA_GROUP_ID
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- LAST_UPDATED_BY
- MODULE_ID
- SEED_STATUS
- SGUID

## Query

```sql
SELECT pay_range_defs_v.RANGE_ITEM_ID RANGE_ITEM_ID, pay_range_defs_v.EFFECTIVE_START_DATE EFFECTIVE_START_DATE, pay_range_defs_v.EFFECTIVE_END_DATE EFFECTIVE_END_DATE, pay_range_defs_v.VALUE_DEFN_ID VALUE_DEFN_ID, pay_range_defs_v.LOW_VALUE LOW_VALUE, pay_range_defs_v.LOW_VALUE_TEXT LOW_VALUE_TEXT, pay_range_defs_v.HIGH_VALUE HIGH_VALUE, pay_range_defs_v.HIGH_VALUE_TEXT HIGH_VALUE_TEXT, pay_range_defs_v.CALC_TYPE_ID CALC_TYPE_ID, pay_range_defs_v.VALUE1 VALUE1, pay_range_defs_v.VALUE2 VALUE2, pay_range_defs_v.VALUE3 VALUE3, pay_range_defs_v.SOURCE_TYPE SOURCE_TYPE, pay_range_defs_v.SOURCE_ID SOURCE_ID, pay_range_defs_v.ENTERPRISE_ID ENTERPRISE_ID, pay_range_defs_v.LEGISLATION_CODE LEGISLATION_CODE, pay_range_defs_v.LEGISLATIVE_DATA_GROUP_ID LEGISLATIVE_DATA_GROUP_ID, pay_range_defs_v.OBJECT_VERSION_NUMBER OBJECT_VERSION_NUMBER, pay_range_defs_v.CREATED_BY CREATED_BY, pay_range_defs_v.CREATION_DATE CREATION_DATE, pay_range_defs_v.LAST_UPDATE_DATE LAST_UPDATE_DATE, pay_range_defs_v.LAST_UPDATE_LOGIN LAST_UPDATE_LOGIN, pay_range_defs_v.LAST_UPDATED_BY LAST_UPDATED_BY, pay_range_defs_v.MODULE_ID MODULE_ID, pay_range_defs_v.SEED_STATUS SEED_STATUS, pay_range_defs_v.SGUID SGUID FROM pay_range_defs_v union all SELECT pay_range_inst_v.RANGE_ITEM_ID RANGE_ITEM_ID, pay_range_inst_v.EFFECTIVE_START_DATE EFFECTIVE_START_DATE, pay_range_inst_v.EFFECTIVE_END_DATE EFFECTIVE_END_DATE, pay_range_inst_v.VALUE_DEFN_ID VALUE_DEFN_ID, pay_range_inst_v.LOW_VALUE LOW_VALUE, pay_range_inst_v.LOW_VALUE_TEXT LOW_VALUE_TEXT, pay_range_inst_v.HIGH_VALUE HIGH_VALUE, pay_range_inst_v.HIGH_VALUE_TEXT HIGH_VALUE_TEXT, pay_range_inst_v.CALC_TYPE_ID CALC_TYPE_ID, pay_range_inst_v.VALUE1 VALUE1, pay_range_inst_v.VALUE2 VALUE2, pay_range_inst_v.VALUE3 VALUE3, pay_range_inst_v.SOURCE_TYPE SOURCE_TYPE, pay_range_inst_v.SOURCE_ID SOURCE_ID, pay_range_inst_v.ENTERPRISE_ID ENTERPRISE_ID, pay_range_inst_v.LEGISLATION_CODE LEGISLATION_CODE, pay_range_inst_v.LEGISLATIVE_DATA_GROUP_ID LEGISLATIVE_DATA_GROUP_ID, pay_range_inst_v.OBJECT_VERSION_NUMBER OBJECT_VERSION_NUMBER, pay_range_inst_v.CREATED_BY CREATED_BY, pay_range_inst_v.CREATION_DATE CREATION_DATE, pay_range_inst_v.LAST_UPDATE_DATE LAST_UPDATE_DATE, pay_range_inst_v.LAST_UPDATE_LOGIN LAST_UPDATE_LOGIN, pay_range_inst_v.LAST_UPDATED_BY LAST_UPDATED_BY, null MODULE_ID, null SEED_STATUS, null SGUID FROM pay_range_inst_v
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
