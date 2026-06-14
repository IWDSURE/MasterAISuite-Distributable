# HWR_SYNONYMS_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsynonymsvl-7804.html#hwrsynonymsvl-7804](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsynonymsvl-7804.html#hwrsynonymsvl-7804)

## Columns

- SYNONYM_ID
- SYNONYM_ATTR_1
- SYNONYM_ATTR_2
- DISPLAY_TEXT
- DESCRIPTION
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.SYNONYM_ID, B.SYNONYM_ATTR_1, B.SYNONYM_ATTR_2, T.DISPLAY_TEXT, T.DESCRIPTION, B.OBJECT_VERSION_NUMBER, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM HWR_SYNONYMS_B B, HWR_SYNONYMS_TL T WHERE B.SYNONYM_ID = T.SYNONYM_ID AND T.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
