# HWM_TM_REP_M_PTT_ATRBS_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepmpttatrbsv-6348.html#hwmtmrepmpttatrbsv-6348](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepmpttatrbsv-6348.html#hwmtmrepmpttatrbsv-6348)

## Columns

- PTT_TIME_REPOS_ATRB_ID
- PAY_PAYROLL_TIME_TYPE
- USAGES_SOURCE_ID
- USAGES_SOURCE_VERSION

## Query

```sql
SELECT PttTimeAtrbs.tm_rep_atrb_id Ptt_Time_Repos_Atrb_id, PttTimeAtrbs.attribute_category Pay_Payroll_Time_Type, PttTimeAtrbsUsg.usages_source_id, PttTimeAtrbsUsg.usages_source_version FROM HWM_TM_REP_ATRBS PttTimeAtrbs, hwm_tm_rep_atrb_usages PttTimeAtrbsUsg WHERE EXISTS (SELECT 1 FROM HWM_TM_ATRB_FLDS_B WHERE TM_ATRB_FLD_ID = MASTER_ATTRIBUTE_ID AND name = 'PayrollTimeType' ) and PttTimeAtrbs.tm_rep_atrb_id = PttTimeAtrbsUsg.tm_rep_atrb_id
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
