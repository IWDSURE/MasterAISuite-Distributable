# PAY_RANGE_DEFS_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrangedefsv-8171.html#payrangedefsv-8171](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrangedefsv-8171.html#payrangedefsv-8171)

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
select prd.RANGE_DEF_ID RANGE_ITEM_ID, prd.EFFECTIVE_START_DATE, prd.EFFECTIVE_END_DATE, prd.VALUE_DEFN_ID, prd.LOW_VALUE, prd.VBC_VALUE_TEXT LOW_VALUE_TEXT, prd.HIGH_VALUE, prd.VBC_VALUE_TEXT HIGH_VALUE_TEXT, prd.CALC_TYPE_ID, prd.VALUE1, prd.VALUE2, prd.VALUE3, null SOURCE_TYPE, null SOURCE_ID, prd.ENTERPRISE_ID, prd.LEGISLATION_CODE, prd.LEGISLATIVE_DATA_GROUP_ID, prd.OBJECT_VERSION_NUMBER, prd.CREATED_BY, prd.CREATION_DATE, prd.LAST_UPDATE_DATE, prd.LAST_UPDATE_LOGIN, prd.LAST_UPDATED_BY, prd.MODULE_ID, prd.SEED_STATUS, prd.SGUID from pay_range_defs_f prd where not exists (select '' from pay_value_defs_f pvd where pvd.value_defn_id = prd.value_defn_id and prd.effective_start_date between pvd.effective_start_date and pvd.effective_end_date and pvd.value1 is not null) union all select pvd.VALUE_DEFN_ID RANGE_ITEM_ID, pvd.EFFECTIVE_START_DATE, pvd.EFFECTIVE_END_DATE, pvd.VALUE_DEFN_ID, -999999999999 LOW_VALUE, decode(pct.type, 'NO', pvd.VALUE1, null) LOW_VALUE_TEXT, 999999999999 HIGH_VALUE, decode(pct.type, 'NO', pvd.VALUE1, null) HIGH_VALUE_TEXT, pvd.CALC_TYPE_ID, pvd.VALUE1, pvd.VALUE2, pvd.VALUE3, null SOURCE_TYPE, null SOURCE_ID, pvd.ENTERPRISE_ID, pvd.LEGISLATION_CODE, pvd.LEGISLATIVE_DATA_GROUP_ID, pvd.OBJECT_VERSION_NUMBER, pvd.CREATED_BY, pvd.CREATION_DATE, pvd.LAST_UPDATE_DATE, pvd.LAST_UPDATE_LOGIN, pvd.LAST_UPDATED_BY, pvd.MODULE_ID, pvd.SEED_STATUS, pvd.SGUID from pay_value_defs_f pvd, pay_calc_types pct where pvd.value1 is not null and pct.calc_type_id = pvd.calc_type_id
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
