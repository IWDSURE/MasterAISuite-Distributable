# HTS_SCHED_UNITS_AOR_SGP_V

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedunitsaorsgpv-4781.html#htsschedunitsaorsgpv-4781](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedunitsaorsgpv-4781.html#htsschedunitsaorsgpv-4781)

## Columns

- SCHED_UNIT_ID
- DEPARTMENT_ID
- LOCATION_ID
- SCHED_GEN_PROFILE_ID
- SCHED_PROFILE_MGR_ID
- PERSON_ID
- ENTERPRISE_ID
- OBJECT_VERSION_NUMBER

## Query

```sql
SELECT spu.sched_unit_id, spu.department_id, spu.location_id, sgp.sched_gen_profile_id, mgr.sched_profile_mgr_id, mgr.person_id, spu.enterprise_id, sgp.object_version_number FROM hts_schedule_gen_profiles_b sgp, ( SELECT sched_profile_unit_id, sched_gen_profile_id, sched_unit_id, department_id, location_id, enterprise_id FROM hts_sched_profile_units UNION SELECT sched_profile_float_id, sched_gen_profile_id, sched_unit_id, department_id, location_id, enterprise_id FROM hts_sched_profile_floats ) spu, hts_sched_profile_managers mgr WHERE sgp.sched_gen_profile_id = mgr.sched_gen_profile_id AND sgp.sched_gen_profile_id = spu.sched_gen_profile_id AND trunc(sysdate) BETWEEN nvl(mgr.start_date, TO_DATE('1901-01-01', 'yyyy-mm-dd')) AND nvl(mgr.end_date, TO_DATE('4712-12-31', 'yyyy-mm-dd')) AND EXISTS (SELECT 1 FROM per_asg_responsibilities res WHERE status = 'Active' AND trunc(sysdate) BETWEEN res.start_date AND nvl(res.end_date, trunc(sysdate)) AND res.person_id = mgr.person_id AND res.responsibility_type = ( SELECT nvl(value_text, 'ORA_PER_SCHEDULE_MANAGER') FROM hts_global_setups_b WHERE parameter_code = 'RESPONSIBILITY_TYPE' ) AND res.enterprise_id = spu.enterprise_id AND res.organization_id = spu.department_id AND ( (nvl(res.location_id, - 1) < 0) OR (nvl(spu.location_id, - 1) < 0) OR (nvl(res.location_id, - 1) = nvl(spu.location_id, - 1)) ) )
```

---

[← Back to Index](../35_Workforce_Scheduling_Views_Index.md)
