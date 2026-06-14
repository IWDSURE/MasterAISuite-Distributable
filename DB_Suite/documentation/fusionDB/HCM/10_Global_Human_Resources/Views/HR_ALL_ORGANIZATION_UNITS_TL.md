# HR_ALL_ORGANIZATION_UNITS_TL

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrallorganizationunitstl-3551.html#hrallorganizationunitstl-3551](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrallorganizationunitstl-3551.html#hrallorganizationunitstl-3551)

## Columns

- ORGANIZATION_ID
- LANGUAGE
- SOURCE_LANG
- NAME
- TITLE
- LAST_UPDATE_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_LOGIN
- CREATED_BY
- CREATION_DATE
- OBJECT_VERSION_NUMBER

## Query

```sql
SELECT organization_id ,language ,source_lang ,name ,title ,last_update_date ,last_updated_by ,last_update_login ,created_by ,creation_date ,object_version_number FROM hr_organization_units_f_tl WHERE trunc(sysdate) between effective_start_date and effective_end_date
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
