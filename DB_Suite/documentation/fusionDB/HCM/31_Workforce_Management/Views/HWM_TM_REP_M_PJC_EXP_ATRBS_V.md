# HWM_TM_REP_M_PJC_EXP_ATRBS_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepmpjcexpatrbsv-6350.html#hwmtmrepmpjcexpatrbsv-6350](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepmpjcexpatrbsv-6350.html#hwmtmrepmpjcexpatrbsv-6350)

## Columns

- PJC_EXP_TIME_REPOS_ATRB_ID
- PJC_EXPENDITURE_TYPE
- USAGES_SOURCE_ID
- USAGES_SOURCE_VERSION

## Query

```sql
SELECT PjcExpAtrbs.tm_rep_atrb_id Pjc_Exp_Time_Repos_Atrb_id, PjcExpAtrbs.attribute_category Pjc_Expenditure_Type, PjcExpAtrbsUsg.usages_source_id, PjcExpAtrbsUsg.usages_source_version FROM hwm_tm_rep_atrbs PjcExpAtrbs, hwm_tm_rep_atrb_usages PjcExpAtrbsUsg, HWM_TM_ATRB_FLDS_B PjcExpAtrbFlds WHERE PjcExpAtrbFlds.TM_ATRB_FLD_ID = PjcExpAtrbs.MASTER_ATTRIBUTE_ID AND PjcExpAtrbFlds.name = 'PJC_EXPENDITURE_TYPE_ID' AND PjcExpAtrbs.tm_rep_atrb_id = PjcExpAtrbsUsg.tm_rep_atrb_id
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
