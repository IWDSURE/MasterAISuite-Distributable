# HWR_VLTR_VOL_MET_VL

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrvolmetvl-8765.html#hwrvltrvolmetvl-8765](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrvolmetvl-8765.html#hwrvltrvolmetvl-8765)

## Columns

- HCM_PERSON_ID
- TOTAL_PROJECT_SUBS
- TOTAL_HOURS_SPENT

## Query

```sql
SELECT A.HCM_PERSON_ID HCM_PERSON_ID, COUNT(A.PROJECT_ID) TOTAL_PROJECT_SUBS, SUM(B.NO_OF_HOURS) TOTAL_HOURS_SPENT FROM HWR_VLTR_VOL_PROJ_REL_VL A, HWR_VLTR_ACTIVITY_VL B WHERE A.HCM_PERSON_ID = B.HCM_PERSON_ID(+) AND A.PROJECT_ID = B.PROJECT_ID(+) GROUP BY A.HCM_PERSON_ID
```

---

[← Back to Index](../8_Corporate_Social_Responsibility_Views_Index.md)
