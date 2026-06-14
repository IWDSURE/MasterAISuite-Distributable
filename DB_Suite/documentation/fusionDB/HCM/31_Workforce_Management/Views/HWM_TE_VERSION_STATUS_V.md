# HWM_TE_VERSION_STATUS_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmteversionstatusv-3270.html#hwmteversionstatusv-3270](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmteversionstatusv-3270.html#hwmteversionstatusv-3270)

## Columns

- TM_BLDG_BLK_ID
- TM_BLDG_BLK_VERSION
- MAX_A_APP_STATUS_PJC_ID
- MAX_A_APP_STATUS_PYR_ID
- MAX_A_TE_COMPLETED_ID
- MAX_A_TR_ERR_STATUS_ID
- MAX_A_XFR_STATUS_PJC_ID
- MAX_A_XFR_STATUS_PYR_ID
- MAX_D_READY_XFR_STATUS_PJC_ID
- MAX_D_READY_XFR_STATUS_PYR_ID

## Query

```sql
SELECT s.tm_bldg_blk_id, s.tm_bldg_blk_version, MAX(DECODE(sd.status_def_cd, 'A_APP_STATUS_PJC', s.status_id, NULL)) MAX_A_APP_STATUS_PJC_ID, MAX(DECODE(sd.status_def_cd, 'A_APP_STATUS_PYR', s.status_id, NULL)) MAX_A_APP_STATUS_PYR_ID, MAX(DECODE(sd.status_def_cd, 'A_TE_COMPLETED', s.status_id, NULL)) MAX_A_TE_COMPLETED_ID, MAX(DECODE(sd.status_def_cd, 'A_TR_ERR_STATUS', s.status_id, NULL)) MAX_A_TR_ERR_STATUS_ID, MAX(DECODE(sd.status_def_cd, 'A_XFR_STATUS_PJC', s.status_id, NULL)) MAX_A_XFR_STATUS_PJC_ID, MAX(DECODE(sd.status_def_cd, 'A_XFR_STATUS_PYR', s.status_id, NULL)) MAX_A_XFR_STATUS_PYR_ID, MAX(DECODE(sd.status_def_cd, 'D_READY_XFR_STATUS_PJC', s.status_id, NULL)) MAX_D_READY_XFR_STATUS_PJC_ID, MAX(DECODE(sd.status_def_cd, 'D_READY_XFR_STATUS_PYR', s.status_id, NULL)) MAX_D_READY_XFR_STATUS_PYR_ID FROM hwm_tm_statuses s, hwm_tm_status_def_b sd WHERE s.tm_status_def_id = sd.tm_status_def_id GROUP BY s.tm_bldg_blk_id, s.tm_bldg_blk_version
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
