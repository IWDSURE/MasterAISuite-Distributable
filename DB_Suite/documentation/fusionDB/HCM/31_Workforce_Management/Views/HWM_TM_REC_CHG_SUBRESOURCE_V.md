# HWM_TM_REC_CHG_SUBRESOURCE_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrecchgsubresourcev-4583.html#hwmtmrecchgsubresourcev-4583](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrecchgsubresourcev-4583.html#hwmtmrecchgsubresourcev-4583)

## Columns

- TM_REC_CHANGE_ID
- SUBRESOURCE_ID

## Query

```sql
SELECT HwmTmRecChangeAtrbs.TM_REC_CHANGE_ID TM_REC_CHANGE_ID, HwmTmRecChangeAtrbs.VALUE_NUMBER SUBRESOURCE_ID FROM HWM_TM_REC_CHANGE_ATRBS HwmTmRecChangeAtrbs, HWM_TM_ATRB_FLDS_B HwmTmAtrbFldsB WHERE HwmTmRecChangeAtrbs.TM_ATRB_FLD_ID = HwmTmAtrbFldsB.TM_ATRB_FLD_ID AND HwmTmAtrbFldsB.NAME = 'SubresourceId'
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
