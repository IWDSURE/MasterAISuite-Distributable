# HWR_DI_OBJ_DEF_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdiobjdefvl-7101.html#hwrdiobjdefvl-7101](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdiobjdefvl-7101.html#hwrdiobjdefvl-7101)

## Columns

- ID
- SOURCE_ID
- UUID
- NAME
- PHYSICAL_DEF
- LOGICAL_DEF
- OBJ_DEF_TYPE
- MAP_TYPE
- DEF_NAME
- REF_DEF_NAME
- PRODUCT
- DESCRIPTION
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- OBJECT_VERSION_NUMBER

## Query

```sql
SELECT B.ID, B.SOURCE_ID, B.UUID, B.NAME, B.PHYSICAL_DEF, B.LOGICAL_DEF, B.OBJ_DEF_TYPE, B.MAP_TYPE, B.DEF_NAME, B.REF_DEF_NAME, B.PRODUCT, T.DESCRIPTION, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN, B.OBJECT_VERSION_NUMBER FROM HWR_DI_OBJ_DEF_B B, HWR_DI_OBJ_DEF_TL T WHERE B.ID = T.ID AND T.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
