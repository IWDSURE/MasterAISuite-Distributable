# HRC_DL_REM_TEMPLATES_VL

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlremtemplatesvl-6275.html#hrcdlremtemplatesvl-6275](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlremtemplatesvl-6275.html#hrcdlremtemplatesvl-6275)

## Columns

- TEMPLATE_ID
- TEMPLATE_CODE
- CATEGORY
- STATUS
- ENTERPRISE_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- OBJECT_VERSION_NUMBER
- TEMPLATE_NAME
- TEMPLATE_DESCRIPTION

## Query

```sql
SELECT b.template_id ,b.template_code ,b.category ,b.status ,b.enterprise_id ,b.created_by ,b.creation_date ,b.last_updated_by ,b.last_update_date ,b.last_update_login ,b.object_version_number ,tl.template_name ,tl.template_description FROM hrc_dl_rem_templates_b b ,hrc_dl_rem_templates_tl tl WHERE b.template_id = tl.template_id AND tl.language = userenv ('LANG')
```

---

[← Back to Index](../14_HCM_Common_Views_Index.md)
