# HTS_SCHEDULES_ATRBS_VIEW

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedulesatrbsview-8762.html#htsschedulesatrbsview-8762](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedulesatrbsview-8762.html#htsschedulesatrbsview-8762)

## Columns

- TM_REP_ATRB_ID
- USAGES_SOURCE_ID
- USAGES_SOURCE_VERSION
- LATEST_VERSION
- SHIFT_ID
- SHIFT_NAME
- SHIFT_SHORT_NAME
- SHORT_TXT
- SHIFT_TYPE_CODE
- SHIFT_COLOUR
- LANGUAGE
- TIME_NOT_WORKED

## Query

```sql
SELECT Atrbs.tm_rep_atrb_id, AtrbUsg.usages_source_id, AtrbUsg.usages_source_version, AtrbUsg.latest_version, ShiftVL.shift_id, ShiftVL.shift_name, ShiftVL.shift_short_name, ShiftVL.short_txt, ShiftVL.shift_type_code, ShiftVL.shift_colour, USERENV('LANG'), NVL(Atrbs.ATTRIBUTE_NUMBER7/60, ShiftVL.TIME_NOT_WORKED/3600000) as time_not_worked FROM HWM_TM_REP_ATRBS Atrbs, HWM_TM_REP_ATRB_USAGES AtrbUsg, HTS_SCHEDULES_SHIFT_TYPES_VL ShiftVL WHERE AtrbUsg.TM_REP_ATRB_ID = Atrbs.TM_REP_ATRB_ID AND Atrbs.ATTRIBUTE_CATEGORY = 'Schedules' AND Atrbs.ATTRIBUTE_NUMBER6 = ShiftVL.SHIFT_ID AND (ShiftVL.deleted_flag IS NULL OR ShiftVL.deleted_flag = 'N') UNION SELECT Atrbs.tm_rep_atrb_id, AtrbUsg.usages_source_id, AtrbUsg.usages_source_version, atrbusg.latest_version, NULL shift_id, 'Normal Working Hours' shift_name, 'NWH' shift_short_name, 'NWH' short_txt, 'TIME' shift_type_code, '#50925A' shift_colour, NULL LANGUAGE, Atrbs.ATTRIBUTE_NUMBER7/60 as time_not_worked FROM hwm_tm_rep_atrbs atrbs, hwm_tm_rep_atrb_usages atrbusg, hwm_tm_rec timerecordpeo WHERE AtrbUsg.TM_REP_ATRB_ID = Atrbs.TM_REP_ATRB_ID AND atrbs.attribute_category = 'Schedules' AND atrbs.attribute_varchar7 IN ('ASSIGNMENT_HOURS', 'STANDARD_HOURS', 'DEFAULT_HOURS') AND TimeRecordPEO.TM_REC_ID = atrbusg.USAGES_SOURCE_ID (+) AND timerecordpeo.tm_rec_version = atrbusg.usages_source_version (+) AND timerecordpeo.latest_version = atrbusg.latest_version (+) AND Atrbs.ATTRIBUTE_NUMBER6 is null UNION SELECT Atrbs.tm_rep_atrb_id, AtrbUsg.usages_source_id, AtrbUsg.usages_source_version, atrbusg.latest_version, NULL shift_id, 'Absence' shift_name, 'ABS' shift_short_name, 'ABS' short_txt, CASE timerecordpeo.tm_rec_type WHEN 'RANGE' THEN 'TIME' WHEN 'MEASURE' THEN 'ELAPSED' ELSE 'TIME' END shift_type_code, '#F8C682' shift_colour, NULL LANGUAGE, NULL time_not_worked FROM hwm_tm_rep_atrbs atrbs, hwm_tm_rep_atrb_usages atrbusg, hwm_tm_rec timerecordpeo WHERE AtrbUsg.TM_REP_ATRB_ID = Atrbs.TM_REP_ATRB_ID AND atrbs.attribute_category = 'Schedules' AND atrbs.attribute_varchar7 = 'ABSENCES' AND TimeRecordPEO.TM_REC_ID = atrbusg.USAGES_SOURCE_ID (+) AND timerecordpeo.tm_rec_version = atrbusg.usages_source_version (+) AND timerecordpeo.latest_version = atrbusg.latest_version (+)
```

---

[← Back to Index](../35_Workforce_Scheduling_Views_Index.md)
