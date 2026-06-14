# HWR_ACCOMPLISH_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwraccomplishvl-8011.html#hwraccomplishvl-8011](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwraccomplishvl-8011.html#hwraccomplishvl-8011)

## Columns

- ACCOMPLISHMENT_ID
- SOURCE_ID
- DESCRIPTION
- COMMENTS
- START_DATE
- END_DATE
- COMPLETION_DATE
- PRFL_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.ACCOMPLISHMENT_ID , B.SOURCE_ID , B.DESCRIPTION , B.COMMENTS , B.START_DATE , B.END_DATE , B.COMPLETION_DATE , X.PRFL_ID , B.CREATED_BY , B.CREATION_DATE , B.LAST_UPDATED_BY , B.LAST_UPDATE_DATE , B.LAST_UPDATE_LOGIN FROM HWR_ACCOMPLISH_B B LEFT JOIN HWR_ACCOMPLISH_PRFL_X X ON (B.ACCOMPLISHMENT_ID = X.ACCOMPLISHMENT_ID AND B.SOURCE_ID = X.SOURCE_ID)
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
