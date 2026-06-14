# HWR_VLTR_TOTAL_WORKFORCE_VL

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrtotalworkforcevl-5814.html#hwrvltrtotalworkforcevl-5814](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrtotalworkforcevl-5814.html#hwrvltrtotalworkforcevl-5814)

## Columns

- TOTALWORKFORCE

## Query

```sql
select count (unique pps.person_id) TotalWorkforce from per_periods_of_service pps, per_all_assignments_f paa where period_type in ('E') and pps.person_id = paa.person_id and pps.legal_entity_id = paa.legal_entity_id and paa.primary_flag = 'Y' and paa.primary_assignment_flag = 'Y' and pps.period_of_service_id = paa.period_of_service_id and pps.date_start = paa.effective_start_date and pps.business_group_id = paa.business_group_id
```

---

[← Back to Index](../8_Corporate_Social_Responsibility_Views_Index.md)
