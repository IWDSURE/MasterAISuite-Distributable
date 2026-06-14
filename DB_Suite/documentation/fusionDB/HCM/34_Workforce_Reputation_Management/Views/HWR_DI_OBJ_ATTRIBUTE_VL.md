# HWR_DI_OBJ_ATTRIBUTE_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdiobjattributevl-3902.html#hwrdiobjattributevl-3902](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdiobjattributevl-3902.html#hwrdiobjattributevl-3902)

## Columns

- ID
- REF_ID
- SOURCE_ID
- ATTRIBUTE_ID
- LABEL
- DESCRIPTION
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.ID, B.REF_ID, B.SOURCE_ID, B.ATTRIBUTE_ID, T.LABEL, T.DESCRIPTION, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM HWR_DI_OBJ_ATTRIBUTE_B B, HWR_DI_OBJ_ATTRIBUTE_TL T WHERE B.ID = T.ID AND T.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
