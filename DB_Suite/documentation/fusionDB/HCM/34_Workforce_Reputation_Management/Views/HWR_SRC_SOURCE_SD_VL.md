# HWR_SRC_SOURCE_SD_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrcsourcesdvl-4458.html#hwrsrcsourcesdvl-4458](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrcsourcesdvl-4458.html#hwrsrcsourcesdvl-4458)

## Columns

- SOURCE_ID
- SOURCE_TYPE_ID
- SOURCE_TYPE_VERSION_ID
- CONNECTION_SPEC
- IS_INTERNAL
- IS_RECRUITING
- SYNC_STATE_CLOB
- NAME
- DESCRIPTION
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.SOURCE_ID, B.SOURCE_TYPE_ID, B.SOURCE_TYPE_VERSION_ID, B.CONNECTION_SPEC, B.IS_INTERNAL, B.IS_RECRUITING, B.SYNC_STATE_CLOB, T.NAME, T.DESCRIPTION, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM HWR_SRC_SOURCE_B B, HWR_SRC_SOURCE_TL T WHERE B.SOURCE_ID = T.SOURCE_ID AND T.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
