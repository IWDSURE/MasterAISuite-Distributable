# HRY_SETUP_CONFIG_PROPERTIES_VL

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrysetupconfigpropertiesvl-4041.html#hrysetupconfigpropertiesvl-4041](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrysetupconfigpropertiesvl-4041.html#hrysetupconfigpropertiesvl-4041)

## Columns

- PROPERTY_ID
- FEATURE_ID
- BASE_PROPERTY_NAME
- LEVELS
- PROPERTY_TYPE
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- OBJECT_VERSION_NUMBER
- MODULE_ID
- SEED_DATA_SOURCE
- ENTERPRISE_ID
- SGUID
- MULTI_ROW
- REQ_USER_INPUT
- PROPERTY_NAME
- PROPERTY_DESCRIPTION
- LANGUAGE
- SOURCE_LANG

## Query

```sql
SELECT tab.PROPERTY_ID ,tab.FEATURE_ID ,tab.BASE_PROPERTY_NAME ,tab.LEVELS ,tab.PROPERTY_TYPE ,tab.CREATED_BY ,tab.CREATION_DATE ,tab.LAST_UPDATED_BY ,tab.LAST_UPDATE_DATE ,tab.LAST_UPDATE_LOGIN ,tab.OBJECT_VERSION_NUMBER ,tab.MODULE_ID ,tab.SEED_DATA_SOURCE ,tab.ENTERPRISE_ID ,tab.SGUID ,tab.MULTI_ROW ,tab.REQ_USER_INPUT ,tl.PROPERTY_NAME ,tl.PROPERTY_DESCRIPTION ,tl.LANGUAGE ,tl.SOURCE_LANG FROM hry_setup_config_properties_tl tl, hry_setup_config_properties tab WHERE tab.PROPERTY_ID = tl.PROPERTY_ID AND tl.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../12_Global_Payroll_Interface_Views_Index.md)
