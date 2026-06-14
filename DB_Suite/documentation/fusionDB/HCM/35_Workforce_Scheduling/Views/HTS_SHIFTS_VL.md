# HTS_SHIFTS_VL

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsshiftsvl-7798.html#htsshiftsvl-7798](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsshiftsvl-7798.html#htsshiftsvl-7798)

## Columns

- SHIFT_ID
- OBJECT_VERSION_NUMBER
- ENTERPRISE_ID
- SHIFT_CODE
- START_TIME_OFFSET
- END_TIME_OFFSET
- WORK_DURATION
- BREAK_DURATION
- SHIFT_CATEGORY
- END_PLUS_DAYS
- ACTIVE_FLAG
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- SHIFT_NAME

## Query

```sql
SELECT shb.shift_id, shb.object_version_number, shb.enterprise_id, shb.shift_code, shb.start_time_offset , shb.end_time_offset , shb.work_duration, shb.break_duration, shb.shift_category, shb.end_plus_days, shb.active_flag, shb.created_by, shb.creation_date, shb.last_updated_by, shb.last_update_date, shb.last_update_login, sht.shift_name FROM hts_shifts_b shb, hts_shifts_tl sht WHERE shb.shift_id = sht.shift_id AND sht.language = userenv('LANG')
```

---

[← Back to Index](../35_Workforce_Scheduling_Views_Index.md)
