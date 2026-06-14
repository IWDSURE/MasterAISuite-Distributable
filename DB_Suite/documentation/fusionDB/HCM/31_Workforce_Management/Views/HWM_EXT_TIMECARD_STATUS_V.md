# HWM_EXT_TIMECARD_STATUS_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmexttimecardstatusv-8339.html#hwmexttimecardstatusv-8339](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmexttimecardstatusv-8339.html#hwmexttimecardstatusv-8339)

## Columns

- STATUS_ID
- RESOURCE_ID
- TM_BLDG_BLK_ID
- TM_BLDG_BLK_VERSION
- DATE_FROM
- DATE_TO
- DATE_FROM_TRUNC
- DATE_TO_TRUNC
- TM_STATUS_DEF_ID
- STATUS_VALUE
- TM_STATUS_TYPE
- TCSMRS_ID
- SCOPE
- REPOSITORY_TYPE
- DEFINITIONCODE
- TCSMRS_CODE
- TM_ATRB_STRUCTURE_ID
- FUSION_APPLICATION
- NAME

## Query

```sql
SELECT S.STATUS_ID ,S.RESOURCE_ID ,S.TM_BLDG_BLK_ID ,S.TM_BLDG_BLK_VERSION ,S.DATE_FROM ,S.DATE_TO ,trunc(s.DATE_FROM) DATE_FROM_TRUNC ,trunc(s.DATE_TO) DATE_TO_TRUNC ,S.TM_STATUS_DEF_ID ,S.STATUS_VALUE ,D.TM_STATUS_TYPE ,D.TCSMRS_ID ,D.SCOPE ,D.REPOSITORY_TYPE ,D.DEFINITIONCODE ,T.TCSMRS_CODE ,T.TM_ATRB_STRUCTURE_ID ,T.FUSION_APPLICATION ,T.NAME from hwm_tm_statuses s , HWM_TM_STATUS_DEF_B d , HWM_TCSMRS_VL t where s.tm_status_def_id = d.tm_status_def_id AND s.date_from <= SYSTIMESTAMP AND s.date_to = to_timestamp('4712-12-31 23:59:59.999','yyyy-mm-dd hh24:mi:ssxff') AND NOT EXISTS (SELECT 1 FROM hwm_tm_statuses s2 WHERE s2.tm_bldg_blk_id = s.tm_bldg_blk_id AND s2.tm_bldg_blk_version = s.tm_bldg_blk_version AND s2.tm_status_def_id = s.tm_status_def_id AND s2.date_from <= SYSTIMESTAMP AND s2.date_to = to_timestamp('4712-12-31 23:59:59.999','yyyy-mm-dd hh24:mi:ssxff') AND (s2.date_from > s.date_from OR (s2.date_from = s.date_from AND s2.last_update_date > s.last_update_date) ) ) and d.tcsmrs_id = t.TCSMRS_ID(+)
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
