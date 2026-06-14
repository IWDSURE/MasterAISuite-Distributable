# HRT_BOOKMARKS_VL

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtbookmarksvl-4839.html#hrtbookmarksvl-4839](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtbookmarksvl-4839.html#hrtbookmarksvl-4839)

## Columns

- BOOKMARK_ID
- ENTERPRISE_ID
- PROFILE_ID
- URL
- DESCRIPTION
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT BM.BOOKMARK_ID, BM.ENTERPRISE_ID, BM.PROFILE_ID, BM.URL, BMT.DESCRIPTION, BM.OBJECT_VERSION_NUMBER, BM.CREATED_BY, BM.CREATION_DATE, BM.LAST_UPDATED_BY, BM.LAST_UPDATE_DATE, BM.LAST_UPDATE_LOGIN FROM HRT_BOOKMARKS_B BM, HRT_BOOKMARKS_TL BMT WHERE BM.BOOKMARK_ID = BMT.BOOKMARK_ID AND BMT.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../20_Profile_Management_Views_Index.md)
