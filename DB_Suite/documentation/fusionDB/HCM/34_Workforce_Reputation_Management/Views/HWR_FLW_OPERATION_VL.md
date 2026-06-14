# HWR_FLW_OPERATION_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrflwoperationvl-4497.html#hwrflwoperationvl-4497](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrflwoperationvl-4497.html#hwrflwoperationvl-4497)

## Columns

- OPERATION_ID
- SOURCE_ID
- UUID
- REST_ID
- REQUEST_OD
- RESPONSE_OD
- NAME
- DESCRIPTION
- OPERATION_TYPE
- CONNECTION_SPEC
- IS_SEEDED_DATA
- IS_INTERNAL
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- OBJECT_VERSION_NUMBER

## Query

```sql
SELECT B.OPERATION_ID, B.SOURCE_ID, B.UUID, B.REST_ID, B.REQUEST_OD, B.RESPONSE_OD, B.NAME, T.DESCRIPTION, B.OPERATION_TYPE, B.CONNECTION_SPEC, B.IS_SEEDED_DATA, B.IS_INTERNAL, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN, B.OBJECT_VERSION_NUMBER FROM HWR_FLW_OPERATION_B B, HWR_FLW_OPERATION_TL T WHERE B.OPERATION_ID = T.OPERATION_ID AND T.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
