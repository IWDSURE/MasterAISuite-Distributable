# HWR_EXPERIENCE_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrexperiencevl-5754.html#hwrexperiencevl-5754](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrexperiencevl-5754.html#hwrexperiencevl-5754)

## Columns

- EXPERIENCE_ID
- SOURCE_ID
- COMPANY
- DESCRIPTION
- END_DATE
- START_DATE
- TITLE
- EXPERIENCE_TYPE
- PRFL_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.EXPERIENCE_ID , B.SOURCE_ID , B.COMPANY , B.DESCRIPTION , B.END_DATE , B.START_DATE , B.TITLE , B.EXPERIENCE_TYPE , X.PRFL_ID , B.CREATED_BY , B.CREATION_DATE , B.LAST_UPDATED_BY , B.LAST_UPDATE_DATE , B.LAST_UPDATE_LOGIN FROM HWR_EXPERIENCE_B B LEFT JOIN HWR_EXPERIENCE_PRFL_X X ON (B.EXPERIENCE_ID = X.EXPERIENCE_ID AND B.SOURCE_ID = X.SOURCE_ID)
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
