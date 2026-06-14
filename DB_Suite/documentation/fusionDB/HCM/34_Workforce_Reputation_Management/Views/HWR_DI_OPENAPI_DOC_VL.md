# HWR_DI_OPENAPI_DOC_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdiopenapidocvl-6391.html#hwrdiopenapidocvl-6391](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdiopenapidocvl-6391.html#hwrdiopenapidocvl-6391)

## Columns

- ID
- FILE_NAME
- CONTENT
- USR_PRFL_OPR
- USR_REVOKE_OPR
- CONNECTOR_TYPE
- NAME
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- OBJECT_VERSION_NUMBER

## Query

```sql
SELECT B.ID, B.FILE_NAME, B.CONTENT, B.USR_PRFL_OPR, B.USR_REVOKE_OPR, B.CONNECTOR_TYPE, T.NAME, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN, B.OBJECT_VERSION_NUMBER FROM HWR_DI_OPENAPI_DOC_B B, HWR_DI_OPENAPI_DOC_TL T WHERE B.ID = T.ID AND T.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
