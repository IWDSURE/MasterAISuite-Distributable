# HTS_SCHED_UNITS_MANAGERS_SGP_V

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedunitsmanagerssgpv-6332.html#htsschedunitsmanagerssgpv-6332](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedunitsmanagerssgpv-6332.html#htsschedunitsmanagerssgpv-6332)

## Columns

- SCHED_UNIT_ID
- OBJECT_VERSION_NUMBER
- ENTERPRISE_ID
- SCHED_UNIT_CODE
- MEMBER_TYPE
- MEMBER_ID
- LOCATION_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- TIMEZONE_CODE

## Query

```sql
SELECT sched_unit_id, object_version_number, enterprise_id, sched_unit_code, member_type, member_id, location_id, created_by, creation_date, last_updated_by, last_update_date, last_update_login, timezone_code FROM hts_sched_units hsu WHERE hsu.sched_unit_id IN ( SELECT spu.sched_unit_id FROM hts_schedule_gen_profiles_b sgp, hts_sched_profile_managers mgr, hts_sched_profile_units spu WHERE sgp.sched_gen_profile_id = mgr.sched_gen_profile_id AND sgp.sched_gen_profile_id = spu.sched_gen_profile_id AND nvl(sgp.is_draft, 'N') = 'N' AND trunc(sysdate) BETWEEN nvl(mgr.start_date, TO_DATE('1901-01-01', 'yyyy-mm-dd')) AND nvl(mgr.end_date, TO_DATE('4712-12-31', 'yyyy-mm-dd')) AND mgr.person_id = nvl(hrc_session_util.get_user_personid, -1) )
```

---

[← Back to Index](../35_Workforce_Scheduling_Views_Index.md)
