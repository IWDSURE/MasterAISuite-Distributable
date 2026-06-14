# HWM_TM_REP_XFR_QUERY_4PYR_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepxfrquery4pyrv-7183.html#hwmtmrepxfrquery4pyrv-7183](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepxfrquery4pyrv-7183.html#hwmtmrepxfrquery4pyrv-7183)

## Columns

- TM_REC_GRP_ID
- TM_REC_GRP_VERSION
- PERSON_ID
- ASSIGNMENT_ID
- XFR_READY_REC_GRP_ID
- MARK_FOR_TRANSFER
- START_TIME
- STOP_TIME

## Query

```sql
SELECT CALC_REC_GRP_ID TM_REC_GRP_ID, CALC_REC_GRP_VERSION TM_REC_GRP_VERSION, RESOURCE_ID PERSON_ID, SUBRESOURCE_ID ASSIGNMENT_ID, XFR_READY_REC_GRP_ID, MARK_FOR_TRANSFER, START_TIME, STOP_TIME FROM HWM_XFR_READY_REC_GRP WHERE TCSMRS_ID = (SELECT TCSMRS_ID FROM HWM_TCSMRS_B WHERE TCSMRS_CODE = 'PYR' ) AND XFR_STATUS = 1
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
