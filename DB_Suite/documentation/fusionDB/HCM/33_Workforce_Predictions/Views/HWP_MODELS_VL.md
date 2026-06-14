# HWP_MODELS_VL

## Details

**Schema:** FUSION

**Object owner:** HWP

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpmodelsvl-5334.html#hwpmodelsvl-5334](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpmodelsvl-5334.html#hwpmodelsvl-5334)

## Columns

- ENTERPRISE_ID
- MODEL_ID
- MODEL_CODE
- MODEL_NAME
- MODEL_DESCRIPTION
- MINING_FUNCTION
- TABLE_NAME
- CASE_ID_COLUMN
- TARGET_ID_COLUMN
- CORRECTION_VALUE
- MODULE_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- OBJECT_VERSION_NUMBER
- SGUID

## Query

```sql
SELECT hm.ENTERPRISE_ID, hm.MODEL_ID, hm.MODEL_CODE, hmt.MODEL_NAME, hmt.MODEL_DESCRIPTION, hm.MINING_FUNCTION, hm.TABLE_NAME, hm.CASE_ID_COLUMN, hm.TARGET_ID_COLUMN, hm.CORRECTION_VALUE, hm.MODULE_ID, hm.CREATED_BY, hm.CREATION_DATE, hm.LAST_UPDATED_BY, hm.LAST_UPDATE_DATE, hm.LAST_UPDATE_LOGIN, hm.OBJECT_VERSION_NUMBER, hm.SGUID SGUID FROM HWP_MODELS_B hm, HWP_MODELS_TL hmt WHERE hm.MODEL_ID = hmt.MODEL_ID AND hmt.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../33_Workforce_Predictions_Views_Index.md)
