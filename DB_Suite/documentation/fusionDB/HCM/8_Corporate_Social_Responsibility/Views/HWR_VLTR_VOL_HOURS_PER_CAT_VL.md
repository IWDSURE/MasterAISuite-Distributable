# HWR_VLTR_VOL_HOURS_PER_CAT_VL

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrvolhourspercatvl-7064.html#hwrvltrvolhourspercatvl-7064](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrvolhourspercatvl-7064.html#hwrvltrvolhourspercatvl-7064)

## Columns

- VOL_ID
- PROJ_ID
- NO_OF_HOURS
- AREAS_OF_INTEREST

## Query

```sql
SELECT A.HCM_PERSON_ID VOL_ID , A.PROJECT_ID PROJ_ID , SUM(A.NO_OF_HOURS) NO_OF_HOURS , B.AREAS_OF_INTEREST AREAS_OF_INTEREST FROM HWR_VLTR_ACTIVITY_VL A, HWR_VLTR_PROJECT_B B WHERE A.PROJECT_ID = B.PROJECT_ID AND A.STATE = 'ACCEPTED' GROUP BY A.HCM_PERSON_ID, A.PROJECT_ID, B.AREAS_OF_INTEREST ORDER BY A.HCM_PERSON_ID, A.PROJECT_ID
```

---

[← Back to Index](../8_Corporate_Social_Responsibility_Views_Index.md)
