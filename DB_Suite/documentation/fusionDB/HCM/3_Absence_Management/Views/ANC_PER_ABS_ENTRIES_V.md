# ANC_PER_ABS_ENTRIES_V

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabsentriesv-3741.html#ancperabsentriesv-3741](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabsentriesv-3741.html#ancperabsentriesv-3741)

## Columns

- PER_ABSENCE_ENTRY_ID
- PERSON_ID
- START_DATE
- START_DATETIME
- END_DATETIME
- END_DATE
- START_TIME
- END_TIME
- APPROVAL_STATUS_CD
- DURATION
- UOM

## Query

```sql
SELECT abs.PER_ABSENCE_ENTRY_ID, abs.PERSON_ID, abs.START_DATE , abs.START_DATETIME, abs.END_DATETIME, abs.END_DATE, abs.START_TIME, abs.END_TIME, abs.APPROVAL_STATUS_CD, abs.DURATION, abs.UOM FROM ANC_PER_ABS_ENTRIES abs
```

---

[← Back to Index](../3_Absence_Management_Views_Index.md)
