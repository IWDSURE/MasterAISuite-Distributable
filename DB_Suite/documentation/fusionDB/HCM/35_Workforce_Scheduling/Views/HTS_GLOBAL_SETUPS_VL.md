# HTS_GLOBAL_SETUPS_VL

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsglobalsetupsvl-3354.html#htsglobalsetupsvl-3354](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsglobalsetupsvl-3354.html#htsglobalsetupsvl-3354)

## Columns

- SETUP_PARAM_ID
- OBJECT_VERSION_NUMBER
- ENTERPRISE_ID
- PARAMETER_CODE
- VALUE_TYPE
- VALUE_NUMBER
- VALUE_TEXT
- VALUE_DATE
- LIST_OF_VALUES_SRC
- LIST_OF_VALUES_NAME
- PARAMETER_CATEGORY
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- MODULE_ID
- SGUID
- PARAMETER_NAME
- PARAMETER_DESCRIPTION

## Query

```sql
SELECT gs.SETUP_PARAM_ID ,gs.OBJECT_VERSION_NUMBER ,gs.ENTERPRISE_ID ,gs.PARAMETER_CODE ,gs.VALUE_TYPE ,gs.VALUE_NUMBER ,gs.VALUE_TEXT ,gs.VALUE_DATE ,gs.LIST_OF_VALUES_SRC ,gs.LIST_OF_VALUES_NAME ,gs.PARAMETER_CATEGORY ,gs.CREATED_BY ,gs.CREATION_DATE ,gs.LAST_UPDATED_BY ,gs.LAST_UPDATE_DATE ,gs.LAST_UPDATE_LOGIN ,gs.MODULE_ID ,gs.SGUID ,tl.PARAMETER_NAME ,tl.PARAMETER_DESCRIPTION From hts_global_setups_b gs, hts_global_setups_tl tl WHERE gs.SETUP_PARAM_ID = tl.SETUP_PARAM_ID AND tl.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../35_Workforce_Scheduling_Views_Index.md)
