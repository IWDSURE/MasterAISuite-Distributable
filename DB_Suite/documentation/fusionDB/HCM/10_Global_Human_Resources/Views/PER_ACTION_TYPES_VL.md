# PER_ACTION_TYPES_VL

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peractiontypesvl-5853.html#peractiontypesvl-5853](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peractiontypesvl-5853.html#peractiontypesvl-5853)

## Columns

- ACTION_TYPE_ID
- ACTION_TYPE_CODE
- MEANING
- BUSINESS_GROUP_ID
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- LAST_UPDATED_BY
- MODULE_ID
- SGUID
- CHANGE_ASG_VISIBLE_FLAG
- DEFAULT_ASG_STATUS
- SUPPORT_ASG_STATUS_DFLT
- INCLUDE_CLE_FUT

## Query

```sql
SELECT b.ACTION_TYPE_ID, b.ACTION_TYPE_CODE, t.MEANING, b.BUSINESS_GROUP_ID, b.OBJECT_VERSION_NUMBER, b.CREATED_BY, b.CREATION_DATE, b.LAST_UPDATE_DATE, b.LAST_UPDATE_LOGIN, b.LAST_UPDATED_BY, b.MODULE_ID, b.SGUID SGUID, b.CHANGE_ASG_VISIBLE_FLAG, b.DEFAULT_ASG_STATUS, b.SUPPORT_ASG_STATUS_DFLT, b.INCLUDE_CLE_FUT FROM PER_ACTION_TYPES_B b, PER_ACTION_TYPES_TL t WHERE b.ACTION_TYPE_ID = t.ACTION_TYPE_ID AND t.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
