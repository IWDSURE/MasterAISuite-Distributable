# HWR_WLNS_DI_SOURCE_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsdisourcevl-3765.html#hwrwlnsdisourcevl-3765](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsdisourcevl-3765.html#hwrwlnsdisourcevl-3765)

## Columns

- ID
- SOURCE_NAME
- SOURCE_TYPE_ID
- SOURCE_ID
- META_DATA
- SOURCE_CATEGORY
- SETUP_STATUS
- IS_ACTIVE
- NAME
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.ID, B.SOURCE_NAME, B.SOURCE_TYPE_ID, B.SOURCE_ID, B.META_DATA, B.SOURCE_CATEGORY, B.SETUP_STATUS, B.IS_ACTIVE, T.NAME, B.OBJECT_VERSION_NUMBER, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM HWR_WLNS_DI_SOURCE_B B, HWR_WLNS_DI_SOURCE_TL T WHERE B.ID = T.ID AND T.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
