# HWR_REP_CONTROL_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrrepcontrolvl-4510.html#hwrrepcontrolvl-4510](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrrepcontrolvl-4510.html#hwrrepcontrolvl-4510)

## Columns

- REPUTATION_CONTROL_ID
- REPUTATION_CONTROL_KEY
- FILE_PATH
- PERCENT
- NAME
- DESCRIPTION
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.REPUTATION_CONTROL_ID, B.REPUTATION_CONTROL_KEY, B.FILE_PATH, B.PERCENT, B.NAME, B.DESCRIPTION, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM HWR_REP_CONTROL_B B
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
