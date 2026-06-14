# HWM_XFR_TRANS_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmxfrtransv-5180.html#hwmxfrtransv-5180](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmxfrtransv-5180.html#hwmxfrtransv-5180)

## Columns

- XFR_TRANS_ID
- ENTERPRISE_ID
- OBJECT_VERSION_NUMBER
- XFR_JOB_ID
- XFR_GRP_ID
- XFR_TM_UNQ_REC_ID
- XFR_ROW_STATUS
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- TCSMRS_ID
- TM_REC_ID
- TM_REC_VERSION
- TM_REC_GRP_ID
- TM_REC_GRP_VERSION
- IN_USE_FLAG

## Query

```sql
SELECT trn.XFR_TRANS_ID, trn.ENTERPRISE_ID, trn.OBJECT_VERSION_NUMBER, trn.XFR_JOB_ID, trn.XFR_GRP_ID, trn.XFR_TM_UNQ_REC_ID, trn.XFR_ROW_STATUS, trn.CREATED_BY, trn.CREATION_DATE, trn.LAST_UPDATED_BY, trn.LAST_UPDATE_DATE, trn.LAST_UPDATE_LOGIN, trn.TCSMRS_ID, unq.TM_REC_ID, unq.TM_REC_VERSION, unq.TM_REC_GRP_ID, unq.TM_REC_GRP_VERSION, unq.IN_USE_FLAG FROM HWM_XFR_TRANS trn, HWM_XFRS_UNQ_RECS unq WHERE trn.XFR_TM_UNQ_REC_ID = unq.XFR_TM_UNQ_REC_ID
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
