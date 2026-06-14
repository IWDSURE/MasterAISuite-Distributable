# CMP_MKT_SURVEY_BATCH_B_V

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktsurveybatchbv-6009.html#cmpmktsurveybatchbv-6009](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktsurveybatchbv-6009.html#cmpmktsurveybatchbv-6009)

## Columns

- BATCH_ID
- VENDOR_ID
- VENDOR_SURVEY_ID
- DATA_EFFECTIVE_START_DATE
- DATA_EFFECTIVE_END_DATE
- STATUS
- OBJECT_VERSION_NUMBER
- BUSINESS_GROUP_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT BATCH_ID, VENDOR_ID, VENDOR_SURVEY_ID, TRUNC(DATA_EFFECTIVE_START_DATE) AS DATA_EFFECTIVE_START_DATE, TRUNC(DATA_EFFECTIVE_END_DATE) AS DATA_EFFECTIVE_END_DATE, STATUS, OBJECT_VERSION_NUMBER, BUSINESS_GROUP_ID, CREATED_BY, CREATION_DATE, LAST_UPDATED_BY, LAST_UPDATE_DATE, LAST_UPDATE_LOGIN FROM CMP_MKT_SURVEY_BATCH_B
```

---

[← Back to Index](../7_Compensation_Views_Index.md)
