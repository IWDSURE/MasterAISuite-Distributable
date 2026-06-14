# HWM_EXT_TIMEENTRY_XFR_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmexttimeentryxfrv-4767.html#hwmexttimeentryxfrv-4767](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmexttimeentryxfrv-4767.html#hwmexttimeentryxfrv-4767)

## Columns

- TM_REC_ID
- TM_REC_VERSION
- TM_REC_TYPE
- MEASURE
- UNIT_OF_MEASURE
- START_TIME_TRUNCATED
- START_TIME
- STOP_TIME
- PERSON_ID
- ASSIGNMENT_ID
- TIME_REPORTER_ID
- DELETE_STATUS
- TM_REC_GRP_ID
- TM_REC_GRP_VERSION
- LDG_OR_BU_ID
- DATE_FROM
- DATE_FROM_TRUNCATED
- ASSIGNMENT_NUMBER
- PERSON_NUMBER
- TCSMR_CODE

## Query

```sql
SELECT rec.tm_rec_id tm_rec_id, rec.tm_rec_version tm_rec_version, rec.tm_rec_type tm_rec_type, rec.measure measure, rec.unit_of_measure unit_of_measure, trunc(rec.start_time) start_time_truncated, rec.start_time start_time, rec.stop_time stop_time, rec.resource_id person_id, rec.subresource_id assignment_id, rec.time_reporter_id time_reporter_id, rec.delete_flag delete_status, rec_grp_final.parent_tm_rec_grp_id tm_rec_grp_id, rec_grp_final.parent_tm_rec_grp_version tm_rec_grp_version, stat.ldg_or_bu_id ldg_or_bu_id, stat.date_from date_from, trunc(stat.date_from) date_from_truncated, paa.assignment_number assignment_number, pap.person_number person_number, substr(stat_def.status_def_cd,(length('D_READY_XFR_STATUS_')+1)) tcsmr_code FROM hwm_tm_rec rec, hwm_tm_rec_grp_usages usages, PER_ALL_ASSIGNMENTS_M paa, PER_ALL_PEOPLE_F pap, hwm_tm_statuses stat, hwm_tm_status_def_b stat_def, (SELECT rec_grp.tm_rec_grp_id, rec_grp.tm_rec_grp_version, rec_grp.parent_tm_rec_grp_id, rec_grp.parent_tm_rec_grp_version FROM HWM_TM_REC_GRP rec_grp WHERE rec_grp.GRP_TYPE_ID =201) rec_grp_final, ( select decode(pay_report_utils.get_parameter_value('CONSUMER'),'ORA_HWM_TIME_CONSUMER_PEM','PJT','ORA_HWM_TIME_CONSUMER_PJC','PJC','ORA_HWM_TIME_CONSUMER_PYR','PYR',null) status_def_cd, pay_report_utils.get_parameter_value_number('LDG_OR_BUSINESS_UNIT') LDG_Or_BU_id, pay_report_utils.get_parameter_value_date('EFFECTIVE_DATE') end_date, pay_report_utils.get_parameter_value_date('START_DATE') start_date, pay_report_utils.get_parameter_value_date('FROM_APPROVAL_DATE') apr_date, pay_report_utils.get_parameter_value('ASSIGNMENT_NUMBER') asmnt_number, pay_report_utils.get_parameter_value('PERSON_NUMBER') person_number FROM dual ) para_value WHERE usages.tm_Rec_grp_id = rec_grp_final.tm_Rec_grp_id AND trunc(rec.start_time) between nvl(trunc(para_value.start_date), to_date('1952-01-01','YYYY-MM-DD')) and nvl(trunc(para_value.end_date), to_date('4712-12-31','YYYY-MM-DD')) AND stat.date_from >= nvl(para_value.apr_date, stat.date_from) AND stat.ldg_or_bu_id = nvl(para_value.LDG_Or_BU_id, stat.ldg_or_bu_id) and (case when para_value.status_def_cd is not null then (case when stat_def.status_def_cd = 'D_READY_XFR_STATUS_'||para_value.status_def_cd then 1 else 0 end) when para_value.status_def_cd is null then (case when stat_def.status_def_cd like 'D_READY_XFR_STATUS_%' then 1 else 0 end) else 0 end) = 1 AND usages.tm_rec_grp_version = rec_grp_final.tm_rec_grp_version AND usages.tm_rec_id = rec.tm_rec_id AND usages.tm_rec_version = rec.tm_rec_version AND usages.latest_version = 'Y' AND rec.latest_version ='Y' AND rec.tm_rec_id = stat.tm_bldg_blk_id AND rec.tm_rec_version = stat.tm_bldg_blk_version AND stat.tm_status_def_id = stat_def.tm_status_def_id AND stat.status_value = 'TRUE' AND sysdate BETWEEN stat.date_from AND stat.date_to AND (para_value.asmnt_number is null or paa.assignment_number = para_value.asmnt_number) AND rec.resource_id = pap.person_id AND (para_value.person_number is null or pap.person_number = para_value.person_number) AND rec.subresource_id = paa.assignment_id AND trunc(rec.start_time) BETWEEN pap.effective_start_date AND pap.effective_end_date AND trunc(rec.start_time) BETWEEN paa.effective_start_date AND paa.effective_end_date AND paa.effective_latest_change = 'Y'
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
