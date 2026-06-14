# HWM_TC_VERSION_STATUS_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcversionstatusv-8083.html#hwmtcversionstatusv-8083](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcversionstatusv-8083.html#hwmtcversionstatusv-8083)

## Columns

- TM_BLDG_BLK_ID
- TM_BLDG_BLK_VERSION
- MAX_D_UI_STATUS_ID
- MAX_A_USER_STATUS_ID

## Query

```sql
SELECT s.tm_bldg_blk_id, s.tm_bldg_blk_version, MAX(DECODE(sd.status_def_cd, 'D_TM_UI_STATUS', s.status_id, NULL)) MAX_D_UI_STATUS_ID, MAX(DECODE(sd.status_def_cd, 'A_USR_STATUS', s.status_id, NULL)) MAX_A_USER_STATUS_ID FROM hwm_tm_statuses s, hwm_tm_status_def_b sd WHERE s.tm_status_def_id = sd.tm_status_def_id GROUP BY s.tm_bldg_blk_id, s.tm_bldg_blk_version
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
