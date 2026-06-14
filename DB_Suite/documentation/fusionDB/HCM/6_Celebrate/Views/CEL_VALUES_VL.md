# CEL_VALUES_VL

## Details

**Schema:** FUSION

**Object owner:** CEL

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celvaluesvl-5607.html#celvaluesvl-5607](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celvaluesvl-5607.html#celvaluesvl-5607)

## Columns

- VALUE_ID
- VALUE_NAME
- ENABLED_FLAG
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.VALUE_ID, T.VALUE_NAME, B.ENABLED_FLAG, B.OBJECT_VERSION_NUMBER, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM CEL_VALUES_B B, CEL_VALUES_TL T WHERE B.VALUE_ID = T.VALUE_ID AND T.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../6_Celebrate_Views_Index.md)
