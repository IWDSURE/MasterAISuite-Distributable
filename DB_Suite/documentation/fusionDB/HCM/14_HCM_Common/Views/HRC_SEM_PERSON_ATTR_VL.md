# HRC_SEM_PERSON_ATTR_VL

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsempersonattrvl-6036.html#hrcsempersonattrvl-6036](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsempersonattrvl-6036.html#hrcsempersonattrvl-6036)

## Columns

- PERSON_ID
- URI
- FULL_NAME
- IS_INTERNAL
- FIRST_NAME
- LAST_NAME
- LOCATION_COUNTRY_ID
- LOCATION_STATE_ID
- LOCATION_CITY_ID
- LOCATION_LATITUDE
- LOCATION_LONGITUDE
- LOCATION_FQN
- OBJECT_VERSION_NUMBER
- PER_LAST_UPDATE_DATE
- EMAIL
- JOB_TITLE
- EMPLOYER_NAME
- YEARS_EXPERIENCE
- DEPARTMENT
- WORK_START_DATE
- WORK_END_DATE
- ACHIEVEMENT_TEXT
- DEGREE_LEVEL
- INSTITUTION_NAME
- FIELD_OF_STUDY
- ATTACH_LAST_MOD_DATE

## Query

```sql
SELECT distinct per.PERSON_ID, per.URI, per.FULL_NAME, per.IS_INTERNAL, per.first_name, per.last_name, per.LOCATION_COUNTRY_ID , per.LOCATION_STATE_ID, per.LOCATION_CITY_ID, per.LOCATION_LATITUDE, per.LOCATION_LONGITUDE, per.LOCATION_FQN, per.OBJECT_VERSION_NUMBER, per.LAST_UPDATE_DATE as PER_LAST_UPDATE_DATE, con.EMAIL, wor.JOB_TITLE, wor.EMPLOYER_NAME, wor.YEARS_EXPERIENCE, wor.DEPARTMENT, wor.START_DATE as WORK_START_DATE, wor.END_DATE as WORK_END_DATE, achi.ACHIEVEMENT_TEXT, edu.DEGREE_LEVEL, edu.INSTITUTION_NAME, edu.FIELD_OF_STUDY, att.LAST_MODIFIED_DATE as ATTACH_LAST_MOD_DATE from HRC_SEM_PERSONS per left outer join HRC_SEM_CONTACT_INFO con on per.person_id = con.person_id left outer join HRC_SEM_WORK_EXPERIENCES wor on per.person_id = wor.person_id left outer join HRC_SEM_ACHIEVEMENTS achi on wor.work_experience_id = achi.work_experience_id left outer join HRC_SEM_EDUCATIONS edu on per.person_id = edu.person_id left outer join HRC_SEM_ATTACHMENTS att on per.person_id = att.person_id
```

---

[← Back to Index](../14_HCM_Common_Views_Index.md)
