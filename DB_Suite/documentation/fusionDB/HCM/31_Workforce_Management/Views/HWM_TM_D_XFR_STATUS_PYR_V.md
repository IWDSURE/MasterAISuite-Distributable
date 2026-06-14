# HWM_TM_D_XFR_STATUS_PYR_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmdxfrstatuspyrv-6643.html#hwmtmdxfrstatuspyrv-6643](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmdxfrstatuspyrv-6643.html#hwmtmdxfrstatuspyrv-6643)

## Columns

- STATUS_ID
- TM_BLDG_BLK_ID
- TM_BLDG_BLK_VERSION
- STATUS_VALUE
- TM_STATUS_DEF_ID

## Query

```sql
SELECT statuses.status_id, statuses.tm_bldg_blk_id, statuses.tm_bldg_blk_version, statuses.status_value, statuses.tm_status_def_id FROM hwm_tm_active_status_v statuses WHERE statuses.status_def_cd = 'D_READY_XFR_STATUS_PYR' /** FROM hwm_tm_statuses statuses WHERE statuses.date_from <= sysdate AND statuses.date_to >= sysdate AND EXISTS (SELECT 1 FROM hwm_tm_status_def_b WHERE statuses.tm_status_def_id = tm_status_def_id AND status_def_cd = 'D_READY_XFR_STATUS_PYR' ) **/
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
