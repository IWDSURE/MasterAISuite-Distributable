# HRC_SEM_JOB_AUTO_SUG_VL

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemjobautosugvl-6421.html#hrcsemjobautosugvl-6421](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemjobautosugvl-6421.html#hrcsemjobautosugvl-6421)

## Columns

- LOV
- CREATION_DATE
- LAST_UPDATE_DATE
- OBJECT_VERSION_NUMBER

## Query

```sql
select REQUISITION_TITLE as LOV, CREATION_DATE, LAST_UPDATE_DATE, OBJECT_VERSION_NUMBER from HRC_SEM_JOBS where REQUISITION_TITLE is not null union select JOB_FAMILY_NAME as LOV, CREATION_DATE, LAST_UPDATE_DATE, OBJECT_VERSION_NUMBER from HRC_SEM_JOBS where JOB_FAMILY_NAME is not null union select LOCATION_FQN as LOV, CREATION_DATE, LAST_UPDATE_DATE, OBJECT_VERSION_NUMBER from HRC_SEM_JOBS where LOCATION_FQN is not null
```

---

[← Back to Index](../14_HCM_Common_Views_Index.md)
