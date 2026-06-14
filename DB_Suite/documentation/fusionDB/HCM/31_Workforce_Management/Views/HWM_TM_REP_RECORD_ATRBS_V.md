# HWM_TM_REP_RECORD_ATRBS_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmreprecordatrbsv-6788.html#hwmtmreprecordatrbsv-6788](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmreprecordatrbsv-6788.html#hwmtmreprecordatrbsv-6788)

## Columns

- ATTRIBUTE_ID
- ATTRIBUTE_NAME
- ATTRIBUTE_TYPE
- ATTRIBUTE_VALUE
- TM_REC_ID
- TM_REC_VERSION

## Query

```sql
SELECT FUNC.ATTRIBUTE_ID, FUNC.ATTRIBUTE_NAME, FUNC.ATTRIBUTE_TYPE, FUNC.ATTRIBUTE_VALUE, TR.TM_REC_ID TM_REC_ID, TR.TM_REC_VERSION TM_REC_VERSION FROM HWM_TM_REC TR, TABLE (HWM_TIME_REPOS_REST.GET_TM_ATRB_VALS(TR.TM_REC_ID , TR.TM_REC_VERSION)) FUNC WHERE TR.LATEST_VERSION = 'Y' AND NVL(TR.DELETE_FLAG, 'N') = 'N'
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
