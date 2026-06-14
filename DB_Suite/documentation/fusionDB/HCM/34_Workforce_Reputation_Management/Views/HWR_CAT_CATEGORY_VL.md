# HWR_CAT_CATEGORY_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcatcategoryvl-5886.html#hwrcatcategoryvl-5886](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcatcategoryvl-5886.html#hwrcatcategoryvl-5886)

## Columns

- CATEGORY_ID
- CATEGORY_KEY
- CATEGORY_TYPE
- IS_SEEDED_DATA
- IS_ACTIVE
- DISPLAY_TEXT
- DESCRIPTION
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.CATEGORY_ID, B.CATEGORY_KEY, B.CATEGORY_TYPE, B.IS_SEEDED_DATA, B.IS_ACTIVE, T.DISPLAY_TEXT, T.DESCRIPTION, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM HWR_CAT_CATEGORY_B B, HWR_CAT_CATEGORY_TL T WHERE B.CATEGORY_ID = T.CATEGORY_ID AND T.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
