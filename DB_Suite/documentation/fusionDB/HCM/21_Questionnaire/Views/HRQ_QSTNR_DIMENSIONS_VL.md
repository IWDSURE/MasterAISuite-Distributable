# HRQ_QSTNR_DIMENSIONS_VL

## Details

**Schema:** FUSION

**Object owner:** HRQ

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrdimensionsvl-5481.html#hrqqstnrdimensionsvl-5481](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrdimensionsvl-5481.html#hrqqstnrdimensionsvl-5481)

## Columns

- BUSINESS_GROUP_ID
- QSTNR_DIMENSION_ID
- NAME
- QUESTIONNAIRE_ID
- QSTNR_VERSION_NUM
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.BUSINESS_GROUP_ID, B.QSTNR_DIMENSION_ID, L.NAME, B.QUESTIONNAIRE_ID, B.QSTNR_VERSION_NUM, B.OBJECT_VERSION_NUMBER, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM HRQ_QSTNR_DIMENSIONS_B B, HRQ_QSTNR_DIMENSIONS_TL L WHERE B.BUSINESS_GROUP_ID = L.BUSINESS_GROUP_ID AND B.QSTNR_DIMENSION_ID = L.QSTNR_DIMENSION_ID AND L.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../21_Questionnaire_Views_Index.md)
