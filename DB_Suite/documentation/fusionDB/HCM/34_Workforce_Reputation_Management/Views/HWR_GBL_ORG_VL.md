# HWR_GBL_ORG_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrgblorgvl-3076.html#hwrgblorgvl-3076](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrgblorgvl-3076.html#hwrgblorgvl-3076)

## Columns

- GBL_PRFL_ID
- PRFL_ID
- SOURCE_ID
- HWR_ORG_ID
- PRFL_GBL_PRFL_ID

## Query

```sql
SELECT G.GBL_PRFL_ID AS GBL_PRFL_ID , O.PRFL_ID AS PRFL_ID , G.SOURCE_ID AS SOURCE_ID, O.HWR_ORG_ID AS HWR_ORG_ID , G2.GBL_PRFL_ID AS PRFL_GBL_PRFL_ID FROM HWR_PER_GBL_PRFL_PRFL_X G, HWR_PER_ORG_PRFL_XREF O, HWR_PER_GBL_PRFL_PRFL_X G2 WHERE G.PRFL_ID = O.HWR_ORG_ID AND G2.PRFL_ID = O.PRFL_ID
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
