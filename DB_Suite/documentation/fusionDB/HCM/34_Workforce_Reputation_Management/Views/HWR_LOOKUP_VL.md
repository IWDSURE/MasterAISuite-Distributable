# HWR_LOOKUP_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrlookupvl-5274.html#hwrlookupvl-5274](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrlookupvl-5274.html#hwrlookupvl-5274)

## Columns

- LOOKUP_ID
- LOOKUP_TYPE_ID
- LOOKUP_TYPE
- LOOKUP_CODE
- IS_SEEDED_DATA
- DISPLAY_TEXT
- TRANS_ID
- DESCRIPTION
- CREATED_BY
- CREATION_DATE
- LAST_UPDATE_LOGIN
- LAST_UPDATED_BY
- LAST_UPDATE_DATE

## Query

```sql
SELECT B.LOOKUP_ID, B.LOOKUP_TYPE_ID, LTB.LOOKUP_TYPE_CODE as LOOKUP_TYPE, B.LOOKUP_CODE, B.IS_SEEDED_DATA, B.DISPLAY_TEXT, B.TRANS_ID, B.DESCRIPTION, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATE_LOGIN, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE FROM HWR_LOOKUP_B B, HWR_LOOKUP_TYPE_B LTB WHERE LTB.LOOKUP_TYPE_ID = B.LOOKUP_TYPE_ID
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
