# PAY_VALUE_DEFS_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payvaluedefsv-7057.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payvaluedefsv-7057.html)

## Columns

- VALUE_DEFN_ID
- VBC_ID
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- BASE_NAME
- VALUE_GROUP_ID
- VBC_STRUCT_ID
- CALC_TYPE_ID
- DATABASE_ITEM_ID
- RANGE_DATABASE_ITEM_ID
- OVERRIDDEN_DB_ITEM_ID
- BASE_VALUE_DEFN_ID
- PARENT_VALUE_DEFN_ID
- DATE_MODE
- ENTERPRISE_ID
- LEGISLATION_CODE
- LEGISLATIVE_DATA_GROUP_ID
- MODULE_ID
- CURRENCY_CODE
- UOM
- PERIODICITY
- PERIODICITY_TYPE
- DEFAULT_CALC_TYPE_ID
- EXPRESSION
- SEQUENCE
- DEFAULT_FLAG
- VALUE_SET_CODE1
- VALUE_SET_CODE2
- VALUE_SET_CODE3
- VO_NAME1
- VO_NAME2
- VO_NAME3
- VALUE_IDENTIFIER
- GEOGRAPHY_TYPE_ID
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- LAST_UPDATED_BY
- SEED_STATUS
- SGUID

## Query

```sql
SELECT pvd.VALUE_DEFN_ID, pvd.VBC_ID VBC_ID, pvd.EFFECTIVE_START_DATE, pvd.EFFECTIVE_END_DATE, pvd.BASE_NAME, pvd.VALUE_GROUP_ID, pvd.vbc_struct_id, pvd.CALC_TYPE_ID, /* nvl(pvd.DATABASE_ITEM_ID, decode (pvd.vbc_struct_id, null, null, decode(pct.type, 'NO', (select CRITERIA_ID from pay_vbc_criteria_defs where VBC_CRITERIA_ID = pvd.vbc_struct_id), null) ) ) DATABASE_ITEM_ID, */ pvd.DATABASE_ITEM_ID, pvd.RANGE_DATABASE_ITEM_ID, pvd.OVERRIDDEN_DB_ITEM_ID, pvd.BASE_VALUE_DEFN_ID, pvd.PARENT_VALUE_DEFN_ID, nvl(pvd.DATE_MODE, decode (pvd.vbc_struct_id, null, null, decode(pct.type, 'VBC', null, 'NO', null, (select DATE_MODE from pay_vbc_value_idents where VBC_VALUE_IDENT_ID = pvd.vbc_struct_id)) ) ) DATE_MODE, pvd.ENTERPRISE_ID, pvd.LEGISLATION_CODE, pvd.LEGISLATIVE_DATA_GROUP_ID, pvd.MODULE_ID, nvl(pvd.CURRENCY_CODE, decode (pvd.vbc_struct_id, null, null, decode(pct.type, 'VBC', null, 'NO', null, (select CURRENCY_CODE from pay_vbc_value_idents where VBC_VALUE_IDENT_ID = pvd.vbc_struct_id)) ) ) CURRENCY_CODE, nvl(pvd.UOM, decode (pvd.vbc_struct_id, null, null, decode(pct.type, 'VBC', null, 'NO', null, (select UOM from pay_vbc_value_idents where VBC_VALUE_IDENT_ID = pvd.vbc_struct_id)) ) ) UOM, nvl(pvd.PERIODICITY, decode (pvd.vbc_struct_id, null, null, decode(pct.type, 'VBC', null, 'NO', null, (select PERIODICITY from pay_vbc_value_idents where VBC_VALUE_IDENT_ID = pvd.vbc_struct_id)) ) ) PERIODICITY, pvd.PERIODICITY_TYPE, nvl(pvd.DEFAULT_CALC_TYPE_ID, decode (pvd.vbc_struct_id, null, null, decode(pct.type, 'VBC', (select CALC_TYPE_ID from pay_vbc_definitions where VBC_DEFINITION_ID = pvd.vbc_struct_id), null) ) ) DEFAULT_CALC_TYPE_ID, nvl(pvd.EXPRESSION, decode (pvd.vbc_struct_id, null, null, decode(pct.type, 'NO', (select EXPRESSION from pay_vbc_criteria_defs where VBC_CRITERIA_ID = pvd.vbc_struct_id), null) ) ) EXPRESSION, pvd.SEQUENCE, pvd.DEFAULT_FLAG, nvl(pvd.VALUE_SET_CODE1, decode (pvd.vbc_struct_id, null, null, decode(pct.type, 'VBC', null, 'NO', (select VALUE_SET_CODE from pay_vbc_criteria_defs where VBC_CRITERIA_ID = pvd.vbc_struct_id), (select VALUE_SET_CODE from pay_vbc_value_idents where VBC_VALUE_IDENT_ID = pvd.vbc_struct_id)) ) ) VALUE_SET_CODE1, nvl(pvd.VALUE_SET_CODE2, decode (pvd.vbc_struct_id, null, null, decode(pct.type, 'VBC', null, 'NO', null, (select VALUE_SET_CODE2 from pay_vbc_value_idents where VBC_VALUE_IDENT_ID = pvd.vbc_struct_id)) ) ) VALUE_SET_CODE2, nvl(pvd.VALUE_SET_CODE3, decode (pvd.vbc_struct_id, null, null, decode(pct.type, 'VBC', null, 'NO', null, (select VALUE_SET_CODE3 from pay_vbc_value_idents where VBC_VALUE_IDENT_ID = pvd.vbc_struct_id)) ) ) VALUE_SET_CODE3, nvl(pvd.VO_NAME1, decode (pvd.vbc_struct_id, null, null, decode(pct.type, 'VBC', null, 'NO', (select VO_NAME from pay_vbc_criteria_defs where VBC_CRITERIA_ID = pvd.vbc_struct_id), (select VO_NAME from pay_vbc_value_idents where VBC_VALUE_IDENT_ID = pvd.vbc_struct_id)) ) ) VO_NAME1, nvl(pvd.VO_NAME2, decode (pvd.vbc_struct_id, null, null, decode(pct.type, 'VBC', null, 'NO', null, (select VO_NAME2 from pay_vbc_value_idents where VBC_VALUE_IDENT_ID = pvd.vbc_struct_id)) ) ) VO_NAME2, nvl(pvd.VO_NAME3, decode (pvd.vbc_struct_id, null, null, decode(pct.type, 'VBC', null, 'NO', null, (select VO_NAME3 from pay_vbc_value_idents where VBC_VALUE_IDENT_ID = pvd.vbc_struct_id)) ) ) VO_NAME3, nvl(pvd.VALUE_IDENTIFIER, decode (pvd.vbc_struct_id, null, null, decode(pct.type, 'VBC', null, 'NO', null, (select BASE_NAME from pay_vbc_value_idents where VBC_VALUE_IDENT_ID = pvd.vbc_struct_id)) ) ) VALUE_IDENTIFIER, pvd.GEOGRAPHY_TYPE_ID, pvd.OBJECT_VERSION_NUMBER, pvd.CREATED_BY, pvd.CREATION_DATE, pvd.LAST_UPDATE_DATE, pvd.LAST_UPDATE_LOGIN, pvd.LAST_UPDATED_BY, pvd.SEED_STATUS, pvd.SGUID FROM PAY_value_defs_f pvd, pay_calc_types pct WHERE pvd.CALC_TYPE_ID = pct.CALC_TYPE_ID
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
