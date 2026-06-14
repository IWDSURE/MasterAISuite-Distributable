# HR_ORG_INFORMATION_TYPES_VL

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrorginformationtypesvl-8444.html#hrorginformationtypesvl-8444](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrorginformationtypesvl-8444.html#hrorginformationtypesvl-8444)

## Columns

- row_id
- ORG_INFORMATION_TYPE
- BUSINESS_GROUP_ID
- MODULE_ID
- DESCRIPTION
- DISPLAYED_ORG_INFORMATION_TYPE
- DATE_EFFECTIVE_FLAG
- FND_APPLICATION_ID
- LEGISLATION_CODE
- NAVIGATION_METHOD
- OBJECT_VERSION_NUMBER
- LAST_UPDATE_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_LOGIN
- CREATED_BY
- CREATION_DATE

## Query

```sql
SELECT oit.ROWID row_id, oit.ORG_INFORMATION_TYPE, oit.BUSINESS_GROUP_ID, oit.MODULE_ID, tl.DESCRIPTION, tl.DISPLAYED_ORG_INFORMATION_TYPE, oit.DATE_EFFECTIVE_FLAG, oit.FND_APPLICATION_ID, oit.LEGISLATION_CODE, oit.NAVIGATION_METHOD, oit.OBJECT_VERSION_NUMBER, oit.LAST_UPDATE_DATE, oit.LAST_UPDATED_BY, oit.LAST_UPDATE_LOGIN, oit.CREATED_BY, oit.CREATION_DATE FROM HR_ORG_INFORMATION_TYPES_TL tl, HR_ORG_INFORMATION_TYPES oit WHERE tl.ORG_INFORMATION_TYPE = oit.ORG_INFORMATION_TYPE AND tl.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
