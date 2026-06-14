# HTS_LINE_MANAGER_SCHED_UNITS_V

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htslinemanagerschedunitsv-3563.html#htslinemanagerschedunitsv-3563](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htslinemanagerschedunitsv-3563.html#htslinemanagerschedunitsv-3563)

## Columns

- MANAGER_ID
- PERSON_ID
- MANAGER_LEVEL
- ASSIGNMENT_ID
- ORGANIZATION_ID
- LOCATION_ID
- SCHED_UNIT_ID
- TIMEZONE_CODE
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE

## Query

```sql
WITH sgp_units AS ( SELECT sgp.sched_gen_profile_id, unit.sched_unit_id, unit.department_id, unit.location_id, unit.timezone_code, sgp.active_start_date, coalesce(unit.active_end_date, sgp.active_end_date, DATE '4712-12-31') AS active_end_date FROM hts_schedule_gen_profiles_b sgp, hts_sched_profile_units unit WHERE sgp.sched_gen_profile_id = unit.sched_gen_profile_id ) SELECT mhd.manager_id, mhd.person_id, mhd.manager_level, asgns.assignment_id, asgns.organization_id, asgns.location_id, unit.sched_unit_id, unit.timezone_code, greatest(mhd.effective_start_date, asgns.effective_start_date, unit.active_start_date) effective_start_date, least(mhd.effective_end_date, asgns.effective_end_date, unit.active_end_date) effective_end_date FROM per_manager_hrchy_dn mhd, per_all_assignments_m asgns, sgp_units unit WHERE mhd.assignment_id = asgns.assignment_id AND mhd.person_id = asgns.person_id AND unit.department_id = asgns.organization_id AND ( unit.location_id IS NULL OR unit.location_id = asgns.location_id ) AND mhd.manager_type = 'LINE_MANAGER' AND mhd.manager_level <= 1 AND asgns.assignment_status_type = 'ACTIVE' AND mhd.effective_start_date <= asgns.effective_end_date AND mhd.effective_end_date >= asgns.effective_start_date AND unit.active_start_date <= mhd.effective_end_date AND unit.active_end_date >= mhd.effective_start_date AND unit.active_start_date <= asgns.effective_end_date AND unit.active_end_date >= asgns.effective_start_date
```

---

[← Back to Index](../35_Workforce_Scheduling_Views_Index.md)
