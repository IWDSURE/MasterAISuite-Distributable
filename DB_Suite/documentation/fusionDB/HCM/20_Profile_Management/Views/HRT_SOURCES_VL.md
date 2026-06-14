# HRT_SOURCES_VL

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtsourcesvl-3761.html#hrtsourcesvl-3761](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtsourcesvl-3761.html#hrtsourcesvl-3761)

## Columns

- SOURCE_ID
- BUSINESS_GROUP_ID
- SOURCE_CODE
- SOURCE_DESCRIPTION
- MODULE_ID
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATE_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT S.SOURCE_ID, S.BUSINESS_GROUP_ID, S.SOURCE_CODE, STL.SOURCE_DESCRIPTION, S.MODULE_ID, S.OBJECT_VERSION_NUMBER, S.CREATED_BY, S.CREATION_DATE, S.LAST_UPDATE_DATE, S.LAST_UPDATED_BY, S.LAST_UPDATE_LOGIN FROM HRT_SOURCES_B S, HRT_SOURCES_TL STL WHERE S.SOURCE_ID = STL.SOURCE_ID AND S.BUSINESS_GROUP_ID = STL.BUSINESS_GROUP_ID AND STL.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../20_Profile_Management_Views_Index.md)
