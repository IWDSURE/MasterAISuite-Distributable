# FAI_SAM_TBS_OCTO_METRIC_V

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamtbsoctometricv-5101.html#faisamtbsoctometricv-5101](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamtbsoctometricv-5101.html#faisamtbsoctometricv-5101)

## Columns

- METRIC_ID
- KEY
- VALUE
- TYPE
- DESCRIPTION
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- ENTERPRISE_ID
- OBJECT_VERSION_NUMBER

## Query

```sql
select "METRIC_ID","KEY","VALUE","TYPE","DESCRIPTION","CREATED_BY","CREATION_DATE","LAST_UPDATED_BY","LAST_UPDATE_DATE","LAST_UPDATE_LOGIN","ENTERPRISE_ID","OBJECT_VERSION_NUMBER" from FAI_SAM_METRIC where last_update_date >= SYS_EXTRACT_UTC(SYSTIMESTAMP) - interval '1' day
```

---

[← Back to Index](../2_AI_Views_Index.md)
