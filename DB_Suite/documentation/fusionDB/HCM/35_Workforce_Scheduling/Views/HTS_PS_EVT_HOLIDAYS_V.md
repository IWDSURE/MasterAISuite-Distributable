# HTS_PS_EVT_HOLIDAYS_V

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htspsevtholidaysv-8589.html#htspsevtholidaysv-8589](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htspsevtholidaysv-8589.html#htspsevtholidaysv-8589)

## Columns

- PERSON_ID
- ASSIGNMENT_ID
- EVENT_YEAR
- EVENT_DATE
- EVENT_DAYS
- EVENT_TITLE
- EVENT_DETAILS
- LINK_TEXT

## Query

```sql
SELECT paaf.person_id person_id, paaf.assignment_id assignment_id, EXTRACT(YEAR FROM avail.start_date_time) event_year, trunc(avail.start_date_time) event_date, ( ( trunc(avail.end_date_time) - trunc(avail.start_date_time) ) + 1 ) event_days, cal_evt_lookup.meaning event_title, avail.object_name event_details, '?pPersonId=' || paaf.person_id link_text FROM per_all_assignments_f paaf, TABLE ( per_availability_details.get_schedule_details(p_resource_id => paaf.assignment_id, p_period_start => add_months(sysdate, -12), p_period_end => add_months(sysdate, 12)) ) avail, fnd_lookup_values_tl cal_evt_lookup WHERE avail.object_type = 'CAL' AND avail.resource_id = paaf.assignment_id AND trunc(sysdate) BETWEEN paaf.effective_start_date AND paaf.effective_end_date AND cal_evt_lookup.lookup_type = 'PER_CAL_EVENT_CATEGORY' AND cal_evt_lookup.LANGUAGE = USERENV('LANG') AND cal_evt_lookup.lookup_code = avail.object_category
```

---

[← Back to Index](../35_Workforce_Scheduling_Views_Index.md)
