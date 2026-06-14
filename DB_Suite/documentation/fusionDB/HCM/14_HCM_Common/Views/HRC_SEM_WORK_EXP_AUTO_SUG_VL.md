# HRC_SEM_WORK_EXP_AUTO_SUG_VL

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemworkexpautosugvl-5684.html#hrcsemworkexpautosugvl-5684](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemworkexpautosugvl-5684.html#hrcsemworkexpautosugvl-5684)

## Columns

- LOV
- CREATION_DATE
- LAST_UPDATE_DATE
- OBJECT_VERSION_NUMBER

## Query

```sql
select wok.JOB_TITLE as LOV, CREATION_DATE, LAST_UPDATE_DATE , OBJECT_VERSION_NUMBER from HRC_SEM_WORK_EXPERIENCES wok where wok.JOB_TITLE is not null union select wok.EMPLOYER_NAME as LOV, CREATION_DATE, LAST_UPDATE_DATE, OBJECT_VERSION_NUMBER from HRC_SEM_WORK_EXPERIENCES wok where wok.EMPLOYER_NAME is not null
```

---

[← Back to Index](../14_HCM_Common_Views_Index.md)
