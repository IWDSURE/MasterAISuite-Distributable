# FAI_SAM_TBS_PROCESSOUT_DATA_V

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamtbsprocessoutdatav-6831.html#faisamtbsprocessoutdatav-6831](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamtbsprocessoutdatav-6831.html#faisamtbsprocessoutdatav-6831)

## Columns

- SEQUENCE_ID
- RAW_PROCESSOUT_ID
- STATUS
- CONTEXT
- KEY
- VALUE
- DATE_DATA
- ANOMALY_LOOP
- SEQUENCE

## Query

```sql
select B.SEQUENCE_ID, A.RAW_PROCESSOUT_ID,A.STATUS,"CONTEXT", "KEY","VALUE","DATE_DATA", "ANOMALY_LOOP", B.SEQUENCE from FAI_SAM_RAW_PROCESSOUT A, FAI_SAM_SEQUENCE B, FAI_SAM_SEQUENCE_OBJECT C where A.RAW_PROCESSOUT_ID = C.RAW_PROCESSOUT_ID and C.SEQUENCE_ID = B.SEQUENCE_ID and a.last_update_date >= SYS_EXTRACT_UTC(SYSTIMESTAMP) - interval '2' hour
```

---

[← Back to Index](../2_AI_Views_Index.md)
