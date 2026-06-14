# HWM_DATA_SOURCE_USAGES_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmdatasourceusagesv-3674.html#hwmdatasourceusagesv-3674](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmdatasourceusagesv-3674.html#hwmdatasourceusagesv-3674)

## Columns

- DATA_SOURCE_USAGE_ID
- TM_ATRB_FLD_ID
- DATA_SOURCE_ID
- ADMIN_DS_FLAG
- USER_DS_FLAG
- DEFAULT_FLAG
- DISPLAY_NAME
- DATA_SOURCE_CODE

## Query

```sql
SELECT DataSourceUsagePEO.DATA_SOURCE_USAGE_ID , DataSourceUsagePEO.TM_ATRB_FLD_ID, DataSourceUsagePEO.DATA_SOURCE_ID , CASE WHEN DataSourceUsagePEO.USAGE_TYPE like '%ADMIN%' THEN 'Y' ELSE 'N' END ADMIN_DS_FLAG, CASE WHEN DataSourceUsagePEO.USAGE_TYPE like '%USER%' THEN 'Y' ELSE 'N' END USER_DS_FLAG, DataSourceUsagePEO.DEFAULT_FLAG , DataSourcePEO.DISPLAY_NAME , DataSourcePEO.DATA_SOURCE_CODE FROM HWM_DATA_SOURCE_USAGES DataSourceUsagePEO, HWM_DATA_SOURCES_VL DataSourcePEO WHERE DataSourceUsagePEO.DATA_SOURCE_ID = DataSourcePEO.DATA_SOURCE_ID (+)
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
