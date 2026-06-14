# CMP_MKT_COMPOSITE_CONFIG_VL

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktcompositeconfigvl-3724.html#cmpmktcompositeconfigvl-3724](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktcompositeconfigvl-3724.html#cmpmktcompositeconfigvl-3724)

## Columns

- COMPOSITE_CONFIG_ID
- COMP_TYPE_CONFIG_ID
- COMPOSITE_COLUMN_KEY
- DISPLAY_NAME
- DISPLAY_SEQUENCE
- ENABLE_FLAG
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.COMPOSITE_CONFIG_ID, B.COMP_TYPE_CONFIG_ID, B.COMPOSITE_COLUMN_KEY, TL.DISPLAY_NAME, B.DISPLAY_SEQUENCE, B.ENABLE_FLAG, B.OBJECT_VERSION_NUMBER, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM CMP_MKT_COMPOSITE_CONFIG_B B, CMP_MKT_COMPOSITE_CONFIG_TL TL WHERE B.COMPOSITE_CONFIG_ID = TL.COMPOSITE_CONFIG_ID AND TL.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../7_Compensation_Views_Index.md)
