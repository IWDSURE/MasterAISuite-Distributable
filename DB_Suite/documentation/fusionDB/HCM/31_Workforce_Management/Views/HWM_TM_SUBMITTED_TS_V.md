# HWM_TM_SUBMITTED_TS_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmsubmittedtsv-3016.html#hwmtmsubmittedtsv-3016](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmsubmittedtsv-3016.html#hwmtmsubmittedtsv-3016)

## Columns

- SUBMITTED_TIMESTAMP
- TM_BLDG_BLK_ID
- TM_BLDG_BLK_VERSION
- STATUS_ID

## Query

```sql
SELECT statuses.date_from submitted_timestamp, statuses.tm_bldg_blk_id, statuses.tm_bldg_blk_version, statuses.status_id FROM hwm_tm_active_status_v statuses WHERE statuses.status_def_cd = 'A_USR_STATUS' and statuses.status_value = 'SUBMITTED' /** FROM hwm_tm_statuses statuses WHERE statuses.date_from <= sysdate AND statuses.date_to >= sysdate AND statuses.status_value = 'SUBMITTED' AND EXISTS (SELECT 1 FROM hwm_tm_status_def_b WHERE statuses.tm_status_def_id = tm_status_def_id AND status_def_cd = 'A_USR_STATUS' ) **/
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
