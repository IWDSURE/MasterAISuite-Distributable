# HRC_DL_BO_POST_PROC_PARAMS_VL

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlbopostprocparamsvl-6486.html#hrcdlbopostprocparamsvl-6486](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlbopostprocparamsvl-6486.html#hrcdlbopostprocparamsvl-6486)

## Columns

- POST_PROC_PARAM_ID
- POST_PROC_ID
- POST_PROC_PARAM_KEY
- POST_PROC_PARAM_NAME
- POST_PROC_PARAM_DESCRIPTION
- PARAM_DEFAULT_VALUE
- PARAM_VALUE_LOOKUP_TYPE
- OVERRIDE_ENABLED
- POST_PROC_PARAM_ENABLED
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
SELECT b.post_proc_param_id ,b.post_proc_id ,b.post_proc_param_key ,tl.post_proc_param_name ,tl.post_proc_param_description ,b.param_default_value ,b.param_value_lookup_type ,b.override_enabled ,b.post_proc_param_enabled ,b.enterprise_id ,b.module_id ,b.created_by ,b.creation_date ,b.last_updated_by ,b.last_update_date ,b.last_update_login ,b.object_version_number ,b.sguid ,b.seed_data_source ,b.ora_seed_set1 ,b.ora_seed_set2 FROM hrc_dl_bo_post_proc_params_b b ,hrc_dl_bo_post_proc_params_tl tl WHERE b.post_proc_param_id = tl.post_proc_param_id AND userenv ('LANG') = tl.language
```

---

[← Back to Index](../14_HCM_Common_Views_Index.md)
