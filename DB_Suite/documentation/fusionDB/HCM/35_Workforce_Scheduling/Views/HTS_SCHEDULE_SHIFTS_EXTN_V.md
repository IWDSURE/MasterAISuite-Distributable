# HTS_SCHEDULE_SHIFTS_EXTN_V

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsscheduleshiftsextnv-4451.html#htsscheduleshiftsextnv-4451](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsscheduleshiftsextnv-4451.html#htsscheduleshiftsextnv-4451)

## Columns

- SCHEDULE_SHIFT_ID
- PERSON_ID
- PERSON_NUMBER
- DISPLAY_NAME
- FULL_NAME
- ASSIGNMENT_ID
- ASSIGNMENT_NUMBER
- ASSIGNMENT_TYPE
- ASSIGNMENT_STATUS
- PRIMARY_FLAG
- DEPARTMENT_ID
- DEPARTMENT_NAME
- LOCATION_ID
- LOCATION_NAME
- LOCATION_CODE
- SCHEDULE_UNIT_ID
- SCHEDULE_ID
- STATUS_CODE
- JOB_PROFILE_TYPE
- JOB_ID
- JOB_CODE
- JOB_NAME
- POSITION_ID
- POSITION_CODE
- POSITION_NAME
- JOB_FAMILY_NAME
- SCHEDULE_GROUP_CODE
- SCHEDULE_GROUP_CODE_MEANING
- QUALIFICATION_TYPE_ID
- QUALIFICATION_TYPE
- QUALIFICATION_ID
- QUALIFICATION_CODE
- QUALIFICATON_NAME
- SHIFT_TYPE
- SHIFT_TYPE_ID
- SHIFT_TYPE_LOOKUP_CODE
- SHIFT_TYPE_NAME
- PRODUCTIVITY
- SHIFT_ID
- SHIFT_NAME
- SHIFT_CATEGORY
- SHIFT_CATEGORY_CODE
- START_DATE_TIME
- END_DATE_TIME
- START_TIME_TZ_OFFSET
- END_TIME_TZ_OFFSET
- CALENDAR_DATE
- REF_DATE
- UNPAID_BREAK_DURATION
- PAID_BREAK_DURATION
- WORK_DURATION
- SOURCE
- ASSIGNMENT_MODE
- COMMENTS
- PREMIUM_SHIFT_CODE
- PREMIUM_SHIFT_CODE_MEANING
- SHIFT_INCENTIVE
- OTHER_DEPARTMENT_FLAG
- APPROVAL_REQ_TO_CLAIM_FLAG
- ALLOW_OVERTIME_FLAG
- CREATION_DATE
- CREATED_BY
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT sh.schedule_shift_id, sh.person_id, ppf.person_number, personnamedpeo.display_name, personnamedpeo.full_name, sh.assignment_id, assignment_info.assignment_number, assignment_info.assignment_type, (CASE WHEN period_service.actual_termination_date IS NOT NULL AND sh.ref_date > period_service.actual_termination_date THEN 'TERMINATED' ELSE status.per_system_status END ) assignment_status, assignment_info.primary_flag, sh_unit.member_id department_id, org.name department_name, sh_unit.location_id, lot.location_name, loa.internal_location_code location_code, sh.schedule_unit_id, sh.schedule_id, sh_hdr.status_code, skill_dtls.job_profile_type job_profile_type, skill_dtls.job_id, skill_dtls.job_code, skill_dtls.job_name job_name, skill_dtls.position_id, skill_dtls.position_code, skill_dtls.position_name position_name, skill_dtls.job_family_name, skill_dtls.scheduling_group_code schedule_group_code, skill_dtls.scheduling_group_code_meaning schedule_group_code_meaning, skill_dtls.qualification_type_id, skill_dtls.qualification_type, skill_dtls.qualification_id, skill_dtls.qualification_code, skill_dtls.qualificaton_name, sh.shift_type shift_type, sh.shift_type_id shift_type_id, extlookupcode.lookup_code shift_type_lookup_code, extlookupcode.extended_lookup_code_name shift_type_name, extlookupcode.information_number1 productivity, sh.shift_id, sh_lib.shift_name, shitcategorylkup.meaning shift_category, nvl(sh.shift_category, sh_lib.shift_category) shift_category_code, sh.start_date_time, sh.end_date_time, sh.start_time_tz_offset, sh.end_time_tz_offset, trunc(sh.start_date_time) calendar_date, sh.ref_date, nvl(sh.break_duration, sh_lib.break_duration) unpaid_break_duration, sh.paid_break_duration, sh.work_duration, sh.source, sh.assignment_mode, sh.comments, sh.premium_shift_code, premshiftcodelkup.meaning premium_shift_code_meaning, sh.shift_incentive, sh.avail_to_other_dept_flag other_department_flag, sh.approval_req_to_claim_flag, sh.allow_overtime_flag, sh.creation_date, sh.created_by, sh.last_updated_by, sh.last_update_date, sh.last_update_login FROM fusion.hts_schedule_shifts sh, fusion.hts_schedules sh_hdr, fusion.hts_sched_units sh_unit, fusion.hr_organization_units_f_tl org, fusion.per_locations loa, fusion.per_location_details_f loc, fusion.per_location_details_f_tl lot, fusion.hcm_extended_lookup_codes_vl extlookupcode, fusion.fnd_lookup_values_vl premshiftcodelkup, fusion.fnd_lookup_values_vl shitcategorylkup, fusion.hts_shifts_vl sh_lib, fusion.per_person_names_f_v personnamedpeo, fusion.per_all_people_f ppf, fusion.per_all_assignments_m assignment_info, per_assignment_status_types_vl status, per_periods_of_service period_service, ( SELECT sk.sched_skill_id, sk.sched_skill_code, sk.job_profile_type, jobdpeo.job_id, jobdpeo.job_code, job_tl.name job_name, jobdpeo.effective_start_date job_effective_start_date, jobdpeo.effective_end_date job_effective_end_date, pos.position_id, pos.position_code, pos_tl.name position_name, pos.effective_start_date pos_effective_start_date, pos.effective_end_date pos_effective_end_date, jobfam.job_family_name, jobfam.effective_start_date job_fam_effective_start_date, jobfam.effective_end_date job_fam_effective_end_date, lookup_vals.lookup_code scheduling_group_code, lookup_vals.meaning scheduling_group_code_meaning, competency.content_item_id qualification_id, competency.content_item_code qualification_code, competency_tl.name qualificaton_name, competency.content_type_id qualification_type_id, contenttype.content_type_name qualification_type FROM fusion.hts_skills_b SK, fusion.per_jobs_f jobdpeo, fusion.per_jobs_f_tl job_tl, fusion.hr_all_positions_f pos, fusion.hr_all_positions_f_tl pos_tl, fusion.per_job_family_f_tl jobfam, fusion.fnd_lookup_values_tl lookup_vals, fusion.hrt_content_items_tl competency_tl, fusion.hrt_content_items_b competency, fusion.hrt_content_types_tl contenttype WHERE sk.job_profile_id = jobdpeo.job_id(+) AND jobdpeo.job_id = job_tl.job_id(+) AND job_tl.LANGUAGE(+) = userenv('LANG') AND sk.job_profile_id = pos.position_id(+) AND pos.position_id = pos_tl.position_id(+) AND pos_tl.LANGUAGE(+) = USERENV('LANG') AND sk.job_profile_id = jobfam.job_family_id(+) AND jobfam.LANGUAGE(+) = USERENV('LANG') AND lookup_vals.lookup_type(+) = 'ORA_PER_SCHEDULING_GROUP' AND lookup_vals.LANGUAGE(+) = userenv('LANG') AND sk.scheduling_group_code = lookup_vals.lookup_code(+) AND sk.competency_id = competency_tl.content_item_id(+) AND sk.enterprise_id = competency_tl.business_group_id(+) AND competency_tl.LANGUAGE(+) = USERENV('LANG') AND sk.competency_id = competency.content_item_id(+) AND sk.enterprise_id = competency.business_group_id(+) AND competency.content_type_id = contenttype.content_type_id(+) AND sk.enterprise_id = contenttype.business_group_id(+) AND contenttype.LANGUAGE(+) = USERENV('LANG') ) skill_dtls WHERE sh.schedule_unit_id = sh_unit.sched_unit_id AND sh.schedule_id = sh_hdr.schedule_id AND sh_unit.member_id = org.organization_id AND org.LANGUAGE = userenv('LANG') AND sh_unit.location_id = loc.location_id(+) AND loc.location_details_id = lot.location_details_id(+) AND loc.effective_start_date = lot.effective_start_date(+) AND loc.effective_end_date = lot.effective_end_date(+) AND lot.LANGUAGE(+) = userenv('LANG') AND loc.location_id = loa.location_id(+) AND sh.skill_id = skill_dtls.sched_skill_id AND sh.shift_type_id = extlookupcode.extended_lookup_code_id (+) AND extlookupcode.lookup_type(+) = 'ORA_HTS_WORKFORCE_SHIFT_TYPE' AND sh.shift_id = sh_lib.shift_id(+) AND premshiftcodelkup.lookup_type(+) = 'ORA_HWM_PREMIUM_SHIFT_CODE' AND sh.premium_shift_code = premshiftcodelkup.lookup_code (+) AND shitcategorylkup.lookup_type (+) = 'ORA_HTS_ENT_SHIFTS_CATEGORY' AND shitcategorylkup.lookup_code (+) = nvl(sh.shift_category, sh_lib.shift_category) AND sh.person_id = ppf.person_id (+) AND TRUNC(sysdate) BETWEEN ppf.effective_start_date (+) AND ppf.effective_end_date (+) AND assignment_info.assignment_type(+) IN ( 'E', 'C') AND assignment_info.effective_latest_change(+) = 'Y' AND sh.assignment_id = assignment_info.assignment_id(+) AND assignment_info.assignment_status_type_id = status.assignment_status_type_id (+) AND assignment_info.period_of_service_id = period_service.period_of_service_id (+) AND sh.ref_date BETWEEN assignment_info.effective_start_date(+) AND assignment_info.effective_end_date(+) AND sh.person_id = personnamedpeo.person_id(+) AND sh.ref_date BETWEEN personnamedpeo.effective_start_date (+) AND personnamedpeo.effective_end_date(+) AND 1 = (CASE WHEN skill_dtls.job_profile_type = 'ORA_JOB' AND sh.ref_date BETWEEN skill_dtls.job_effective_start_date AND skill_dtls.job_effective_end_date THEN 1 WHEN skill_dtls.job_profile_type = 'ORA_POSITION' AND sh.ref_date BETWEEN skill_dtls.pos_effective_start_date AND skill_dtls.pos_effective_end_date THEN 1 WHEN skill_dtls.job_profile_type = 'ORA_JOB_FAMILY' AND sh.ref_date BETWEEN skill_dtls.job_fam_effective_start_date AND skill_dtls.job_fam_effective_end_date THEN 1 WHEN skill_dtls.job_profile_type = 'ORA_JOB_SCH_GROUP' THEN 1 ELSE 2 END )
```

---

[← Back to Index](../35_Workforce_Scheduling_Views_Index.md)
