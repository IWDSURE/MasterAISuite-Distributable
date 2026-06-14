# HWR_FLW_FLOW_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrflwflowvl-3812.html#hwrflwflowvl-3812](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrflwflowvl-3812.html#hwrflwflowvl-3812)

## Columns

- FLOW_ID
- SOURCE_ID
- UUID
- NAME
- IS_SEEDED_DATA
- IS_INTERNAL
- DESCRIPTION
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- OBJECT_VERSION_NUMBER

## Query

```sql
SELECT B.FLOW_ID, B.SOURCE_ID, B.UUID, B.NAME, B.IS_SEEDED_DATA, B.IS_INTERNAL, T.DESCRIPTION, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN, B.OBJECT_VERSION_NUMBER FROM HWR_FLW_FLOW_B B, HWR_FLW_FLOW_TL T WHERE B.FLOW_ID = T.FLOW_ID AND T.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
