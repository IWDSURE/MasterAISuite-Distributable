# HTS_STAFF_PLAN_DETAILS_V

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsstaffplandetailsv-5877.html#htsstaffplandetailsv-5877](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsstaffplandetailsv-5877.html#htsstaffplandetailsv-5877)

## Columns

- STAFFING_PLAN_ID
- STAFFING_PLAN_NAME
- SCHEDULE_UNIT_ID
- ACTIVE_START_DATE
- ACTIVE_END_DATE
- VOLUME_CAPACITY_MAX
- AVERAGE_DAILY_VOLUME
- DEPARTMENT_ID
- LOCATION_ID
- DEPARTMENT_NAME
- LOCATION_NAME
- STAFF_PLAN_STATUS_CODE
- STAFF_PLAN_STATUS_MEANING
- STAFF_PLAN_STATUS_CODE_ORIG
- GRID_ERROR
- PLAN_SCHEDULED
- STAFF_PLAN_TYPE_CODE
- ENTERPRISE_ID

## Query

```sql
SELECT staffing_plan_id, staffing_plan_name, schedule_unit_id, active_start_date, active_end_date, volume_capacity_max, average_daily_volume, department_id, location_id, department_name, location_name, ( CASE WHEN nvl(grid_error, 'x') = 'Y' THEN 'ORA_HTS_STAFFING_PLAN_ERROR' WHEN nvl(staff_plan_status_code_orig, 'x') = 'ORA_HTS_STAFFING_PLAN_AVAIL' AND nvl(plan_scheduled, 'x') = 'Y' THEN 'ORA_HTS_STAFFING_SCHEDULING' ELSE staff_plan_status_code_orig END ) staff_plan_status_code, ( SELECT lu1.meaning FROM fnd_lookup_values_vl lu1 WHERE lu1.lookup_type = 'ORA_HTS_STAFFING_PLAN_STATUS' AND lu1.lookup_code = ( CASE WHEN nvl(grid_error, 'x') = 'Y' THEN 'ORA_HTS_STAFFING_PLAN_ERROR' WHEN nvl(staff_plan_status_code_orig, 'x') = 'ORA_HTS_STAFFING_PLAN_AVAIL' AND nvl(plan_scheduled, 'x') = 'Y' THEN 'ORA_HTS_STAFFING_SCHEDULING' ELSE staff_plan_status_code_orig END ) ) staff_plan_status_meaning, staff_plan_status_code_orig, grid_error, plan_scheduled, staff_plan_type_code, enterprise_id FROM ( SELECT pln.staff_plan_id staffing_plan_id, pln.plan_name staffing_plan_name, pln.sched_unit_id schedule_unit_id, pln.active_start_date, pln.active_end_date, pln.volume_capacity_max, pln.average_daily_volume, dept.organization_id department_id, location.location_id, dept.name department_name, location.location_name, pln.staff_plan_status_code staff_plan_status_code_orig, ( SELECT DISTINCT 'Y' FROM hts_staff_plan_grids spg, hts_staff_grids grd WHERE spg.staff_grid_id = grd.staff_grid_id AND spg.staff_plan_id = pln.staff_plan_id AND staff_grid_status_code = 'ORA_HTS_STAFFING_GRID_ERROR' ) grid_error, ( SELECT DISTINCT 'Y' FROM ( SELECT DISTINCT schedule_unit_id FROM hts_schedules x WHERE x.schedule_unit_id = pln.sched_unit_id AND ( x.start_date BETWEEN pln.active_start_date AND pln.active_end_date OR x.end_date BETWEEN pln.active_start_date AND pln.active_end_date ) ) sch WHERE sch.schedule_unit_id = pln.sched_unit_id ) plan_scheduled, staff_plan_type_code, pln.enterprise_id FROM hts_staff_plans pln, hts_sched_units_department_v su, per_departments dept, per_location_details_f_vl location WHERE pln.sched_unit_id = su.sched_unit_id AND su.member_id = dept.organization_id AND pln.enterprise_id = su.enterprise_id AND su.enterprise_id = dept.business_group_id AND ( trunc(sysdate) BETWEEN dept.effective_start_date AND dept.effective_end_date ) AND nvl(su.location_id, 0) = location.location_id (+) AND ( trunc(sysdate) BETWEEN location.effective_start_date (+) AND location.effective_end_date (+) ) )
```

---

[← Back to Index](../35_Workforce_Scheduling_Views_Index.md)
