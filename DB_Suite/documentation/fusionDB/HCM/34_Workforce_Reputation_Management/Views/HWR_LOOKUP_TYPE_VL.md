# HWR_LOOKUP_TYPE_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrlookuptypevl-4981.html#hwrlookuptypevl-4981](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrlookuptypevl-4981.html#hwrlookuptypevl-4981)

## Columns

- LOOKUP_TYPE_ID
- LOOKUP_TYPE_CODE
- IS_SEEDED_DATA
- DISPLAY_TEXT
- DESCRIPTION
- CREATED_BY
- CREATION_DATE
- LAST_UPDATE_LOGIN
- LAST_UPDATED_BY
- LAST_UPDATE_DATE

## Query

```sql
SELECT B.LOOKUP_TYPE_ID, B.LOOKUP_TYPE_CODE, B.IS_SEEDED_DATA, B.DISPLAY_TEXT, B.DESCRIPTION, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATE_LOGIN, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE FROM HWR_LOOKUP_TYPE_B B
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
