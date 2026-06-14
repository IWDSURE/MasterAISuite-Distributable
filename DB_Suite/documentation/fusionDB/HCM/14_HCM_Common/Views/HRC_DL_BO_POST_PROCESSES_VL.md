# HRC_DL_BO_POST_PROCESSES_VL

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlbopostprocessesvl-5151.html#hrcdlbopostprocessesvl-5151](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlbopostprocessesvl-5151.html#hrcdlbopostprocessesvl-5151)

## Columns

- POST_PROC_ID
- POST_PROC_KEY
- POST_PROC_NAME
- POST_PROC_DESCRIPTION
- POST_PROC_TYPE
- POST_PROC_JOB_FQ_DEFN_NAME
- POST_PROC_JOB_FQ_CLASS_NAME
- POST_PROC_TASK_NAME
- BUSINESS_OBJECT_ID
- POST_PROCESS_SEQUENCE
- DEFAULT_VALUE
- OVERRIDE_ENABLED
- POST_PROC_ENABLED
- POST_PROC_CERTIFIED
- ENTERPRISE_ID
- MODULE_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- OBJECT_VERSION_NUMBER
- SGUID
- SEED_DATA_SOURCE
- ORA_SEED_SET1
- ORA_SEED_SET2

## Query

```sql
SELECT b.post_proc_id ,b.post_proc_key ,tl.post_proc_name ,tl.post_proc_description ,b.post_proc_type ,b.post_proc_job_fq_defn_name ,b.post_proc_job_fq_class_name ,b.post_proc_task_name ,b.business_object_id ,b.post_process_sequence ,b.default_value ,b.override_enabled ,b.post_proc_enabled ,b.post_proc_certified ,b.enterprise_id ,b.module_id ,b.created_by ,b.creation_date ,b.last_updated_by ,b.last_update_date ,b.last_update_login ,b.object_version_number ,b.sguid ,b.seed_data_source ,b.ora_seed_set1 ,b.ora_seed_set2 FROM hrc_dl_bo_post_processes_b b ,hrc_dl_bo_post_processes_tl tl WHERE b.post_proc_id = tl.post_proc_id AND userenv ('LANG') = tl.language
```

---

[← Back to Index](../14_HCM_Common_Views_Index.md)
