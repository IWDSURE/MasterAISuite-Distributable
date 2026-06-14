# HWM_EXT_TIMECARD_ENTRY_XFR_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmexttimecardentryxfrv-8036.html#hwmexttimecardentryxfrv-8036](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmexttimecardentryxfrv-8036.html#hwmexttimecardentryxfrv-8036)

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
- TCSMR_CODE

## Query

```sql
SELECT rec.tm_rec_id tm_rec_id, rec.tm_rec_version tm_rec_version, rec.tm_rec_type tm_rec_type, rec.measure measure, rec.unit_of_measure unit_of_measure, trunc(rec.start_time) start_time_truncated, rec.start_time start_time, rec.stop_time stop_time, rec.resource_id person_id, rec.subresource_id assignment_id, rec.time_reporter_id time_reporter_id, rec.delete_flag delete_status, hdv.parent_tm_rec_grp_id tm_rec_grp_id, hdv.parent_tm_rec_grp_version tm_rec_grp_version, stat.ldg_or_bu_id ldg_or_bu_id, stat.date_from date_from, trunc(stat.date_from) date_from_truncated, substr(stat_def.status_def_cd,(length('D_READY_XFR_STATUS_')+1)) tcsmr_code FROM HWM_TM_REC rec, HWM_TM_REC_GRP_USAGES usg , HWM_TM_STATUSES stat, hwm_tm_status_def_b stat_def, HWM_TM_REC_GRP hdv , ( select decode(pay_report_utils.get_parameter_value('CONSUMER'),'ORA_HWM_TIME_CONSUMER_PEM','PJT','ORA_HWM_TIME_CONSUMER_PJC','PJC','ORA_HWM_TIME_CONSUMER_PYR','PYR',null) status_def_cd, pay_report_utils.get_parameter_value_number('LDG_OR_BUSINESS_UNIT') LDG_Or_BU_id, pay_report_utils.get_parameter_value_date('EFFECTIVE_DATE') end_date, pay_report_utils.get_parameter_value_date('START_DATE') start_date, pay_report_utils.get_parameter_value_date('FROM_APPROVAL_DATE') apr_date FROM dual ) para_value WHERE REC.TM_REC_ID = USG.TM_REC_ID AND REC.TM_REC_VERSION = USG.TM_REC_VERSION AND usg.TM_REC_GRP_ID = hdv.TM_REC_GRP_ID AND usg.TM_REC_GRP_VERSION = hdv.TM_REC_GRP_VERSION AND usg.latest_version = 'Y' AND rec.grp_type_id=202 AND rec.latest_version ='Y' and (case when para_value.status_def_cd is not null then (case when stat_def.status_def_cd = 'D_READY_XFR_STATUS_'||para_value.status_def_cd then 1 else 0 end) when para_value.status_def_cd is null then (case when stat_def.status_def_cd like 'D_READY_XFR_STATUS_%' then 1 else 0 end) else 0 end) = 1 AND trunc(rec.start_time) between nvl(trunc(para_value.start_date), to_date('1952-01-01','YYYY-MM-DD')) and nvl(trunc(para_value.end_date), to_date('4712-12-31','YYYY-MM-DD')) AND stat.date_from >= nvl(para_value.apr_date, stat.date_from) AND stat.ldg_or_bu_id = nvl(para_value.LDG_Or_BU_id, stat.ldg_or_bu_id) AND stat.tm_status_def_id = stat_def.tm_status_def_id AND rec.tm_rec_id = stat.tm_bldg_blk_id AND rec.tm_rec_version = stat.tm_bldg_blk_version AND stat.status_value = 'TRUE' AND sysdate BETWEEN stat.date_from AND stat.date_to
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
