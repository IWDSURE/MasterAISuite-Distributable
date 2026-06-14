# PER_CHECKLIST_CATEGORIES_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistcategoriesv-8447.html#perchecklistcategoriesv-8447](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistcategoriesv-8447.html#perchecklistcategoriesv-8447)

## Columns

- LOOKUP_CODE
- MEANING
- DESCRIPTION
- ENABLED_FLAG
- TAG
- SUBJECT_TYPE_CODE
- SUB_CATEGORY_ALLOWED
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_LOGIN
- LAST_UPDATE_DATE

## Query

```sql
SELECT B.CATEGORY_CODE as LOOKUP_CODE, T.NAME as MEANING, T.DESCRIPTION, B.ENABLED_FLAG, B.TAG, B.SUBJECT_TYPE_CODE, B.SUB_CATEGORY_ALLOWED, T.CREATED_BY, T.CREATION_DATE, T.LAST_UPDATED_BY, T.LAST_UPDATE_LOGIN, T.LAST_UPDATE_DATE FROM PER_CHECKLIST_CATEGORIES_TL T, PER_CHECKLIST_CATEGORIES_B B WHERE T.CHECKLIST_CATEGORY_ID = B.CHECKLIST_CATEGORY_ID AND T.LANGUAGE = USERENV('LANG') AND B.CATEGORY_TYPE = 'CATEGORY'
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
