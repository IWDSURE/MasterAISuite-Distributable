# HWM_TM_REP_M_ANC_ATRBS_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepmancatrbsv-7706.html#hwmtmrepmancatrbsv-7706](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepmancatrbsv-7706.html#hwmtmrepmancatrbsv-7706)

## Columns

- ANC_MASTER_TIME_REPOS_ATRB_ID
- ANC_ABSENCE_TYPE
- USAGES_SOURCE_ID
- USAGES_SOURCE_VERSION

## Query

```sql
SELECT AncAtrbs.tm_rep_atrb_id Anc_Master_Time_Repos_Atrb_id, AncAtrbs.attribute_category Anc_Absence_Type, AncAtrbsUsg.usages_source_id, AncAtrbsUsg.usages_source_version FROM hwm_tm_rep_atrbs AncAtrbs, hwm_tm_rep_atrb_usages AncAtrbsUsg WHERE EXISTS (SELECT 1 FROM HWM_TM_ATRB_FLDS_B WHERE TM_ATRB_FLD_ID = MASTER_ATTRIBUTE_ID AND name = 'AbsenceType' ) and AncAtrbs.tm_rep_atrb_id = AncAtrbsUsg.tm_rep_atrb_id
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
