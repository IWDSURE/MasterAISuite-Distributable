# HTS_SKILLS_VL

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsskillsvl-4878.html#htsskillsvl-4878](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsskillsvl-4878.html#htsskillsvl-4878)

## Columns

- SCHED_SKILL_ID
- OBJECT_VERSION_NUMBER
- ENTERPRISE_ID
- SCHED_SKILL_CODE
- JOB_PROFILE_TYPE
- JOB_PROFILE_ID
- COMPETENCY_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- SKILL_NAME
- SKILL_DESCRIPTION
- SCHEDULING_GROUP_CODE

## Query

```sql
SELECT sklb.sched_skill_id, sklb.object_version_number, sklb.enterprise_id, sklb.sched_skill_code, sklb.job_Profile_type, sklb.job_Profile_id, sklb.competency_id, sklb.created_by, sklb.creation_date, sklb.last_updated_by, sklb.last_update_date, sklb.last_update_login, sklt.skill_name, sklt.skill_description, sklb.scheduling_group_code FROM hts_skills_b sklb, hts_skills_tl sklt WHERE sklb.sched_skill_id = sklt.sched_skill_id AND sklt.language = userenv('LANG')
```

---

[← Back to Index](../35_Workforce_Scheduling_Views_Index.md)
