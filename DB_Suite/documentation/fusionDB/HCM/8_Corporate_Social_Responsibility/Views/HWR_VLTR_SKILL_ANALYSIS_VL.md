# HWR_VLTR_SKILL_ANALYSIS_VL

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrskillanalysisvl-6704.html#hwrvltrskillanalysisvl-6704](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrskillanalysisvl-6704.html#hwrvltrskillanalysisvl-6704)

## Columns

- PROJECT_ID
- PROJECT_DESCRIPTION
- HCM_PERSON_ID
- LAST_UPDATE_DATE

## Query

```sql
SELECT PROJECT.PROJECT_ID, PROJECT.PROJECT_DESCRIPTION, PROFILE.HCM_PERSON_ID, PROJECT.LAST_UPDATE_DATE FROM HWR_VLTR_PROJECT_VL PROJECT INNER JOIN HWR_VLTR_VOL_PROJ_REL_VL PROFILE ON PROJECT.PROJECT_ID = PROFILE.PROJECT_ID AND PROJECT.STATE = 'ORA_COMPLETED' AND PROFILE.STATUS='VOLUNTEERED'
```

---

[← Back to Index](../8_Corporate_Social_Responsibility_Views_Index.md)
