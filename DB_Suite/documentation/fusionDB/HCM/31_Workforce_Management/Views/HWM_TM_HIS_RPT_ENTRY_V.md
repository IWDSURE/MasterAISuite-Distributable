# HWM_TM_HIS_RPT_ENTRY_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmhisrptentryv-4721.html#hwmtmhisrptentryv-4721](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmhisrptentryv-4721.html#hwmtmhisrptentryv-4721)

## Columns

- TIME_CARD_TM_REC_GRP_ID
- TIME_CARD_TM_REC_GRP_VERSION
- DAY_TM_REC_GRP_ID
- DAY_TM_REC_GRP_VERSION
- TIME_RECORD_ID
- TIME_RECORD_VERSION
- GROUP_TYPE_ID
- TIME_RECORD_LAYER_CODE
- HISTORIC_CHANGE_TIME
- HISTORIC_CHANGE_DATE_FROM
- HISTORIC_CHANGE_DATE_TO
- TC_USER_STATUS_VALUE
- TC_UI_STATUS_VALUE
- TC_SUBMITTED_TIMESTAMP
- TC_APPROVED_TIMESTAMP

## Query

```sql
SELECT his.TIME_CARD_TM_REC_GRP_ID, his.TIME_CARD_TM_REC_GRP_VERSION, his.DAY_TM_REC_GRP_ID, his.DAY_TM_REC_GRP_VERSION, his.TIME_RECORD_ID, his.TIME_RECORD_VERSION, his.GROUP_TYPE_ID, his.TIME_RECORD_LAYER_CODE, his.HISTORIC_CHANGE_TIME, his.HISTORIC_CHANGE_DATE_FROM, his.HISTORIC_CHANGE_DATE_TO, auser.status_value TC_USER_STATUS_VALUE, dtmui.status_value TC_UI_STATUS_VALUE, tcsubts.submitted_timestamp TC_SUBMITTED_TIMESTAMP, tcappts.approved_timestamp TC_APPROVED_TIMESTAMP FROM (SELECT te.TC_TM_REC_GRP_ID TIME_CARD_TM_REC_GRP_ID, te.TC_TM_REC_GRP_VERSION TIME_CARD_TM_REC_GRP_VERSION, te.DAY_TM_REC_GRP_ID DAY_TM_REC_GRP_ID, te.DAY_TM_REC_GRP_VERSION DAY_TM_REC_GRP_VERSION, te.TE_TM_REC_ID TIME_RECORD_ID, te.TE_TM_REC_VERSION TIME_RECORD_VERSION, te.TE_DATE_FROM TIME_RECORD_DATE_FROM, te.TE_DATE_TO TIME_RECORD_DATE_TO, te.TC_GRP_TYPE_ID GROUP_TYPE_ID, te.TE_LAYER_CODE TIME_RECORD_LAYER_CODE, CASE WHEN ht.AS_OF_TIME > te.TE_DATE_FROM THEN ht.AS_OF_TIME ELSE te.TE_DATE_FROM END Historic_Change_Time, CASE WHEN te.TE_DATE_FROM > ht.STATUS_DATE_FROM THEN te.TE_DATE_FROM ELSE ht.STATUS_DATE_FROM END Historic_Change_Date_From, CASE WHEN te.TE_DATE_TO < (ht.STATUS_DATE_TO+1/24/3600) THEN te.TE_DATE_TO ELSE ht.STATUS_DATE_TO END Historic_Change_Date_To FROM (SELECT TimeCard.TM_REC_GRP_ID TC_TM_REC_GRP_ID, TimeCard.TM_REC_GRP_VERSION TC_TM_REC_GRP_VERSION, TimeCard.DATE_FROM TC_DATE_FROM, TimeCard.DATE_TO TC_DATE_TO, TimeCard.GRP_TYPE_ID TC_GRP_TYPE_ID, TimeCard.DELETE_FLAG TC_DELETE_FLAG, TimeCardDay.TM_REC_GRP_ID DAY_TM_REC_GRP_ID, TimeCardDay.TM_REC_GRP_VERSION DAY_TM_REC_GRP_VERSION, TimeCardDay.DATE_FROM DAY_DATE_FROM, TimeCardDay.DATE_TO DAY_DATE_TO, TimeCardDay.DELETE_FLAG DAY_DELETE_FLAG, TimeEntry.TM_REC_ID TE_TM_REC_ID, TimeEntry.TM_REC_VERSION TE_TM_REC_VERSION, TimeEntry.DATE_FROM TE_DATE_FROM, TimeEntry.DATE_TO TE_DATE_TO, TimeEntry.DELETE_FLAG TE_DELETE_FLAG, TimeEntry.LAYER_CODE TE_LAYER_CODE FROM HWM_TM_REC TimeEntry, HWM_TM_REC_GRP TimeCard, HWM_TM_REC_GRP TimeCardDay WHERE TimeCard.TM_REC_GRP_ID = TimeCardDay.PARENT_TM_REC_GRP_ID AND TimeCard.TM_REC_GRP_VERSION = TimeCardDay.PARENT_TM_REC_GRP_VERSION AND TimeEntry.START_TIME BETWEEN TimeCardDay.START_TIME AND TimeCardDay.STOP_TIME AND TimeEntry.RESOURCE_ID = TimeCardDay.RESOURCE_ID AND TimeEntry.LAYER_CODE = 'ABSENCES' UNION SELECT TimeCard.TM_REC_GRP_ID TC_TM_REC_GRP_ID, TimeCard.TM_REC_GRP_VERSION TC_TM_REC_GRP_VERSION, TimeCard.DATE_FROM TC_DATE_FROM, TimeCard.DATE_TO TC_DATE_TO, TimeCard.GRP_TYPE_ID TC_GRP_TYPE_ID, TimeCard.DELETE_FLAG TC_DELETE_FLAG, TimeCardDay.TM_REC_GRP_ID DAY_TM_REC_GRP_ID, TimeCardDay.TM_REC_GRP_VERSION DAY_TM_REC_GRP_VERSION, TimeCardDay.DATE_FROM DAY_DATE_FROM, TimeCardDay.DATE_TO DAY_DATE_TO, TimeCardDay.DELETE_FLAG DAY_DELETE_FLAG, TimeEntry.TM_REC_ID TE_TM_REC_ID, TimeEntry.TM_REC_VERSION TE_TM_REC_VERSION, TimeEntry.DATE_FROM TE_DATE_FROM, TimeEntry.DATE_TO TE_DATE_TO, TimeEntry.DELETE_FLAG TE_DELETE_FLAG, TimeEntry.LAYER_CODE TE_LAYER_CODE FROM HWM_TM_REC TimeEntry, HWM_TM_REC_GRP TimeCard, HWM_TM_REC_GRP TimeCardDay, HWM_TM_REC_GRP_USAGES TimeCardUsg WHERE TimeCard.TM_REC_GRP_ID = TimeCardDay.PARENT_TM_REC_GRP_ID AND TimeCard.TM_REC_GRP_VERSION = TimeCardDay.PARENT_TM_REC_GRP_VERSION AND TimeCardDay.TM_REC_GRP_ID = TimeCardUsg.TM_REC_GRP_ID AND TimeCardDay.TM_REC_GRP_VERSION = TimeCardUsg.TM_REC_GRP_VERSION AND TimeEntry.TM_REC_ID = TimeCardUsg.TM_REC_ID AND TimeEntry.TM_REC_VERSION = TimeCardUsg.TM_REC_VERSION AND UPPER(TimeEntry.UNIT_OF_MEASURE) IN ('HR', 'UN') ) te, (SELECT G.TM_REC_GRP_ID, G.TM_REC_GRP_VERSION, S.DATE_FROM STATUS_DATE_FROM, S.DATE_TO STATUS_DATE_TO, CASE WHEN S.CREATION_DATE > G.DATE_FROM THEN S.CREATION_DATE ELSE G.DATE_FROM END AS_OF_TIME FROM HWM_TM_STATUSES S LEFT JOIN HWM_TM_REC_GRP G ON G.TM_REC_GRP_ID = S.TM_BLDG_BLK_ID AND G.TM_REC_GRP_VERSION = S.TM_BLDG_BLK_VERSION INNER JOIN hwm_tm_status_def_b d ON S.tm_status_def_id = d.tm_status_def_id WHERE d.status_def_cd = 'D_TM_UI_STATUS' AND (S.object_version_number > 1 OR S.date_to >= to_date('4712-12-31', 'yyyy-MM-dd')) ) ht WHERE ht.TM_REC_GRP_ID = te.TC_TM_REC_GRP_ID AND ht.TM_REC_GRP_VERSION = te.TC_TM_REC_GRP_VERSION AND ht.AS_OF_TIME BETWEEN te.TC_DATE_FROM AND te.TC_DATE_TO AND ht.AS_OF_TIME BETWEEN te.DAY_DATE_FROM AND te.DAY_DATE_TO AND (ht.AS_OF_TIME <= te.TE_DATE_FROM OR ht.AS_OF_TIME BETWEEN te.TE_DATE_FROM AND te.TE_DATE_TO) AND (te.TE_DATE_FROM <= ht.STATUS_DATE_TO AND te.TE_DATE_TO >= (ht.STATUS_DATE_FROM+1/24/3600)) AND NVL(te.TE_DELETE_FLAG,'N') = 'N' AND NVL(te.DAY_DELETE_FLAG,'N') = 'N' AND NVL(te.TC_DELETE_FLAG,'N') = 'N' AND te.TC_GRP_TYPE_ID = 100 ) his LEFT JOIN (SELECT statuses.status_id, statuses.tm_bldg_blk_id, statuses.tm_bldg_blk_version, statuses.status_value, statuses.date_from, statuses.date_to FROM hwm_tm_statuses statuses WHERE EXISTS (SELECT 1 FROM hwm_tm_status_def_b WHERE statuses.tm_status_def_id = tm_status_def_id AND status_def_cd = 'A_USR_STATUS' ) ) auser ON auser.tm_bldg_blk_id = his.TIME_CARD_TM_REC_GRP_ID AND auser.tm_bldg_blk_version = his.TIME_CARD_TM_REC_GRP_VERSION AND his.Historic_Change_Time BETWEEN auser.date_from AND auser.date_to LEFT JOIN (SELECT statuses.status_id, statuses.tm_bldg_blk_id, statuses.tm_bldg_blk_version, statuses.status_value, statuses.date_from, statuses.date_to FROM hwm_tm_statuses statuses WHERE EXISTS (SELECT 1 FROM hwm_tm_status_def_b WHERE statuses.tm_status_def_id = tm_status_def_id AND status_def_cd = 'D_TM_UI_STATUS' ) ) dtmui ON dtmui.tm_bldg_blk_id = his.TIME_CARD_TM_REC_GRP_ID AND dtmui.tm_bldg_blk_version = his.TIME_CARD_TM_REC_GRP_VERSION AND his.Historic_Change_Time BETWEEN dtmui.date_from AND dtmui.date_to LEFT JOIN (SELECT statuses.date_from submitted_timestamp, statuses.tm_bldg_blk_id, statuses.tm_bldg_blk_version, statuses.status_id, statuses.date_from, statuses.date_to FROM hwm_tm_statuses statuses WHERE statuses.status_value = 'SUBMITTED' AND EXISTS (SELECT 1 FROM hwm_tm_status_def_b WHERE statuses.tm_status_def_id = tm_status_def_id AND status_def_cd = 'A_USR_STATUS' ) ) tcsubts ON tcsubts.tm_bldg_blk_id = his.TIME_CARD_TM_REC_GRP_ID AND tcsubts.tm_bldg_blk_version = his.TIME_CARD_TM_REC_GRP_VERSION AND his.Historic_Change_Time BETWEEN tcsubts.date_from AND tcsubts.date_to LEFT JOIN (SELECT statuses.date_from approved_timestamp, statuses.tm_bldg_blk_id, statuses.tm_bldg_blk_version, statuses.status_id, statuses.date_from, statuses.date_to FROM hwm_tm_statuses statuses WHERE statuses.status_value = 'APPROVED' AND EXISTS (SELECT 1 FROM hwm_tm_status_def_b WHERE statuses.tm_status_def_id = tm_status_def_id AND status_def_cd = 'D_TM_UI_STATUS' ) ) tcappts ON tcappts.tm_bldg_blk_id = his.TIME_CARD_TM_REC_GRP_ID AND tcappts.tm_bldg_blk_version = his.TIME_CARD_TM_REC_GRP_VERSION AND his.Historic_Change_Time BETWEEN tcappts.date_from AND tcappts.date_to
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
