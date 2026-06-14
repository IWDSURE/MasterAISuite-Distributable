# HWR_DI_ACC_ACCESS_POINT_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdiaccaccesspointvl-5220.html#hwrdiaccaccesspointvl-5220](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdiaccaccesspointvl-5220.html#hwrdiaccaccesspointvl-5220)

## Columns

- ACCESS_POINT_ID
- SOURCE_ID
- UUID
- CONNECTION_SPEC
- ACCESS_POINT_TYPE
- NAME
- DESCRIPTION
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- OBJECT_VERSION_NUMBER

## Query

```sql
SELECT B.ACCESS_POINT_ID, B.SOURCE_ID, B.UUID, B.CONNECTION_SPEC, B.ACCESS_POINT_TYPE, B.NAME, T.DESCRIPTION, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN, B.OBJECT_VERSION_NUMBER FROM HWR_DI_ACC_ACCESS_POINT_B B, HWR_DI_ACC_ACCESS_POINT_TL T WHERE B.ACCESS_POINT_ID = T.ACCESS_POINT_ID AND T.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
