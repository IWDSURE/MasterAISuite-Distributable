# PER_ROLES_DN_VL

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perrolesdnvl-6625.html#perrolesdnvl-6625](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perrolesdnvl-6625.html#perrolesdnvl-6625)

## Columns

- ROLE_ID
- ROLE_GUID
- ROLE_NAME
- DESCRIPTION
- BUSINESS_GROUP_ID
- ABSTRACT_ROLE
- JOB_ROLE
- DATA_ROLE
- ACTIVE_FLAG
- ROLE_COMMON_NAME
- MULTITENANCY_COMMON_NAME
- ROLE_DISTINGUISHED_NAME
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- DELEGATION_ALLOWED
- EXTERNAL_ID
- EXTERNAL_ROLE
- DUTY_ROLE

## Query

```sql
SELECT pr_base.ROLE_ID, pr_base.ROLE_GUID, prtl.ROLE_NAME, prtl.DESCRIPTION, pr_base.BUSINESS_GROUP_ID, pr_base.ABSTRACT_ROLE, pr_base.JOB_ROLE, pr_base.DATA_ROLE, pr_base.ACTIVE_FLAG, pr_base.ROLE_COMMON_NAME, pr_base.MULTITENANCY_COMMON_NAME, pr_base.ROLE_DISTINGUISHED_NAME, pr_base.OBJECT_VERSION_NUMBER, pr_base.CREATED_BY, pr_base.CREATION_DATE, pr_base.LAST_UPDATED_BY, pr_base.LAST_UPDATE_DATE, pr_base.LAST_UPDATE_LOGIN, pr_base.DELEGATION_ALLOWED, pr_base.EXTERNAL_ID, pr_base.EXTERNAL_ROLE, pr_base.DUTY_ROLE FROM PER_ROLES_DN pr_base, PER_ROLES_DN_TL prtl WHERE prtl.ROLE_ID = pr_base.ROLE_ID AND prtl.LANGUAGE = 'US'
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
