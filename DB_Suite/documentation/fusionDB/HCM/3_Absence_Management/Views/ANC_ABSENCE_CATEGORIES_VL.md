# ANC_ABSENCE_CATEGORIES_VL

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancabsencecategoriesvl-4555.html#ancabsencecategoriesvl-4555](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancabsencecategoriesvl-4555.html#ancabsencecategoriesvl-4555)

## Columns

- ABSENCE_CATEGORY_ID
- ANC_ABS_CATEGORY_F_ALTCD
- NAME
- EFFECTIVE_END_DATE
- EFFECTIVE_START_DATE
- STATUS
- LEGISLATION_CODE
- OBJECT_VERSION_NUMBER
- LAST_UPDATED_BY
- LAST_UPDATE_LOGIN
- LAST_UPDATE_DATE
- ENTERPRISE_ID
- DESCRIPTION
- LANGUAGE
- SGUID
- BASE_NAME
- MANAGEMENT_TYPE_CD

## Query

```sql
SELECT AbsenceCategoriesDEO.ABSENCE_CATEGORY_ID, AbsenceCategoriesDEO.ANC_ABS_CATEGORY_F_ALTCD, AbsenceCategoriesTranslation.NAME, AbsenceCategoriesDEO.EFFECTIVE_END_DATE, AbsenceCategoriesDEO.EFFECTIVE_START_DATE, AbsenceCategoriesDEO.STATUS, AbsenceCategoriesDEO.LEGISLATION_CODE, AbsenceCategoriesDEO.OBJECT_VERSION_NUMBER, AbsenceCategoriesDEO.LAST_UPDATED_BY, AbsenceCategoriesDEO.LAST_UPDATE_LOGIN, AbsenceCategoriesDEO.LAST_UPDATE_DATE, AbsenceCategoriesDEO.ENTERPRISE_ID, AbsenceCategoriesTranslation.DESCRIPTION, AbsenceCategoriesTranslation.LANGUAGE, AbsenceCategoriesDEO.SGUID SGUID, AbsenceCategoriesDEO.BASE_NAME, AbsenceCategoriesDEO.MANAGEMENT_TYPE_CD FROM ANC_ABSENCE_CATEGORIES_F AbsenceCategoriesDEO, ANC_ABSENCE_CATEGORIES_F_TL AbsenceCategoriesTranslation WHERE AbsenceCategoriesDEO.ABSENCE_CATEGORY_ID = AbsenceCategoriesTranslation.ABSENCE_CATEGORY_ID AND AbsenceCategoriesDEO.EFFECTIVE_END_DATE = AbsenceCategoriesTranslation.EFFECTIVE_END_DATE AND AbsenceCategoriesDEO.EFFECTIVE_START_DATE = AbsenceCategoriesTranslation.EFFECTIVE_START_DATE AND AbsenceCategoriesTranslation.LANGUAGE = SYS_CONTEXT('USERENV', 'LANG')
```

---

[← Back to Index](../3_Absence_Management_Views_Index.md)
