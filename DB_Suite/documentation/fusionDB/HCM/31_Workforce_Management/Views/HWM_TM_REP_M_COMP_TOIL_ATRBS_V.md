# HWM_TM_REP_M_COMP_TOIL_ATRBS_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepmcomptoilatrbsv-6457.html#hwmtmrepmcomptoilatrbsv-6457](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepmcomptoilatrbsv-6457.html#hwmtmrepmcomptoilatrbsv-6457)

## Columns

- TOIL_REPOS_ATRB_ID
- TOIL_TIME_TYPE
- USAGES_SOURCE_ID
- USAGES_SOURCE_VERSION

## Query

```sql
SELECT ToilAtrbs.tm_rep_atrb_id Toil_Repos_Atrb_id, ToilAtrbs.attribute_category Toil_Time_Type, ToilAtrbsUsg.usages_source_id, ToilAtrbsUsg.usages_source_version FROM HWM_TM_REP_ATRBS ToilAtrbs, hwm_tm_rep_atrb_usages ToilAtrbsUsg WHERE EXISTS (SELECT 1 FROM HWM_TM_ATRB_FLDS_B WHERE TM_ATRB_FLD_ID = MASTER_ATTRIBUTE_ID AND name = 'CompensatoryTimeAbsencePlan' ) and ToilAtrbs.tm_rep_atrb_id = ToilAtrbsUsg.tm_rep_atrb_id
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
