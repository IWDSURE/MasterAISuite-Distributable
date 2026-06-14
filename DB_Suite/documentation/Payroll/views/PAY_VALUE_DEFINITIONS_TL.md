# PAY_VALUE_DEFINITIONS_TL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payvaluedefinitionstl-4573.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payvaluedefinitionstl-4573.html)

## Columns

- VALUE_DEFN_ID
- LANGUAGE
- SOURCE_LANG
- NAME
- DISPLAY_TAG
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- ENTERPRISE_ID

## Query

```sql
SELECT potl.VALUE_DEFN_ID VALUE_DEFN_ID, potl.LANGUAGE LANGUAGE, potl.SOURCE_LANG SOURCE_LANG, potl.NAME NAME, potl.DISPLAY_TAG DISPLAY_TAG, potl.CREATED_BY CREATED_BY, potl.CREATION_DATE CREATION_DATE, potl.LAST_UPDATED_BY LAST_UPDATED_BY, potl.LAST_UPDATE_DATE LAST_UPDATE_DATE, potl.LAST_UPDATE_LOGIN LAST_UPDATE_LOGIN, potl.ENTERPRISE_ID ENTERPRISE_ID FROM pay_old_value_defns_tl potl where exists (select '' from pay_value_instances_v pvi where pvi.value_defn_id = potl.value_defn_id) union all SELECT pntl.VALUE_DEFN_ID VALUE_DEFN_ID, pntl.LANGUAGE LANGUAGE, pntl.SOURCE_LANG SOURCE_LANG, pntl.NAME NAME, pntl.DISPLAY_TAG DISPLAY_TAG, pntl.CREATED_BY CREATED_BY, pntl.CREATION_DATE CREATION_DATE, pntl.LAST_UPDATED_BY LAST_UPDATED_BY, pntl.LAST_UPDATE_DATE LAST_UPDATE_DATE, pntl.LAST_UPDATE_LOGIN LAST_UPDATE_LOGIN, pntl.ENTERPRISE_ID ENTERPRISE_ID FROM pay_value_defs_tl pntl
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
