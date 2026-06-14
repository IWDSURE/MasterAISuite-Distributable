# HRT_PROFILE_SECTIONS_VL

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilesectionsvl-7495.html#hrtprofilesectionsvl-7495](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilesectionsvl-7495.html#hrtprofilesectionsvl-7495)

## Columns

- PROFILE_SECTION_ID
- BUSINESS_GROUP_ID
- PROFILE_ID
- SECTION_ID
- CONTENT_TYPE_ID
- DESCRIPTION
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.PROFILE_SECTION_ID, B.BUSINESS_GROUP_ID, B.PROFILE_ID, B.SECTION_ID, B.CONTENT_TYPE_ID, TL.DESCRIPTION, B.OBJECT_VERSION_NUMBER, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM HRT_PROFILE_SECTIONS_B B, HRT_PROFILE_SECTIONS_TL TL WHERE B.PROFILE_SECTION_ID = TL.PROFILE_SECTION_ID AND B.BUSINESS_GROUP_ID = TL.BUSINESS_GROUP_ID AND TL.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../20_Profile_Management_Views_Index.md)
