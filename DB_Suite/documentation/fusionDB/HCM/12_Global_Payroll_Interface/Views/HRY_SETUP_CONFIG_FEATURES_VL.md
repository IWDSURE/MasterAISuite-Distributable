# HRY_SETUP_CONFIG_FEATURES_VL

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrysetupconfigfeaturesvl-6320.html#hrysetupconfigfeaturesvl-6320](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrysetupconfigfeaturesvl-6320.html#hrysetupconfigfeaturesvl-6320)

## Columns

- FEATURE_ID
- BASE_FEATURE_NAME
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
- FEATURE_NAME
- FEATURE_DESCRIPTION
- LANGUAGE
- SOURCE_LANG

## Query

```sql
SELECT tab.FEATURE_ID ,tab.BASE_FEATURE_NAME ,tab.CREATED_BY ,tab.CREATION_DATE ,tab.LAST_UPDATED_BY ,tab.LAST_UPDATE_DATE ,tab.LAST_UPDATE_LOGIN ,tab.OBJECT_VERSION_NUMBER ,tab.MODULE_ID ,tab.SEED_DATA_SOURCE ,tab.ENTERPRISE_ID ,tab.SGUID ,tl.FEATURE_NAME ,tl.FEATURE_DESCRIPTION ,tl.LANGUAGE ,tl.SOURCE_LANG FROM hry_setup_config_features_tl tl, hry_setup_config_features tab WHERE tab.FEATURE_ID = tl.FEATURE_ID AND tl.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../12_Global_Payroll_Interface_Views_Index.md)
