# HRY_SETUP_CONFIG_PROP_DTLS_VL

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrysetupconfigpropdtlsvl-7906.html#hrysetupconfigpropdtlsvl-7906](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrysetupconfigpropdtlsvl-7906.html#hrysetupconfigpropdtlsvl-7906)

## Columns

- PROPERTY_DETAIL_ID
- PROPERTY_ID
- BASE_PROPERTY_DETAILS_NAME
- PROPERTY_DETAIL_VALUE
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
- EDITABLE
- ENABLE
- PROPERTY_DETAILS_NAME
- PROPERTY_DETAILS_DESC
- LANGUAGE
- SOURCE_LANG

## Query

```sql
SELECT tab.PROPERTY_DETAIL_ID ,tab.PROPERTY_ID ,tab.BASE_PROPERTY_DETAILS_NAME ,tab.PROPERTY_DETAIL_VALUE ,tab.CREATED_BY ,tab.CREATION_DATE ,tab.LAST_UPDATED_BY ,tab.LAST_UPDATE_DATE ,tab.LAST_UPDATE_LOGIN ,tab.OBJECT_VERSION_NUMBER ,tab.MODULE_ID ,tab.SEED_DATA_SOURCE ,tab.ENTERPRISE_ID ,tab.SGUID ,tab.EDITABLE ,tab.ENABLE ,tl.PROPERTY_DETAILS_NAME ,tl.PROPERTY_DETAILS_DESC ,tl.LANGUAGE ,tl.SOURCE_LANG FROM hry_setup_config_prop_dtls_tl tl, hry_setup_config_prop_dtls tab WHERE tab.PROPERTY_DETAIL_ID = tl.PROPERTY_DETAIL_ID AND tl.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../12_Global_Payroll_Interface_Views_Index.md)
