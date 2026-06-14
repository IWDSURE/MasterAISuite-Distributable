# HWM_TM_REP_S_ABS_TEP_ATRBS_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepsabstepatrbsv-8368.html#hwmtmrepsabstepatrbsv-8368](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepsabstepatrbsv-8368.html#hwmtmrepsabstepatrbsv-8368)

## Columns

- ANC_TIME_REPOS_ATRB_ID
- ANC_DURATION_PAID
- USAGES_SOURCE_ID
- USAGES_SOURCE_VERSION

## Query

```sql
SELECT AbsenceTimeEntryAtrbs.tm_rep_atrb_id Anc_Time_Repos_Atrb_id, AbsenceTimeEntryAtrbs.attribute_number1 Anc_Duration_Paid, AbsenceTimeEntryAtrbsUsg.usages_source_id, AbsenceTimeEntryAtrbsUsg.usages_source_version FROM hwm_tm_rep_atrbs AbsenceTimeEntryAtrbs, hwm_tm_rep_atrb_usages AbsenceTimeEntryAtrbsUsg WHERE AbsenceTimeEntryAtrbs.tm_rep_atrb_id = AbsenceTimeEntryAtrbsUsg.tm_rep_atrb_id and AbsenceTimeEntryAtrbs.attribute_category = 'AbsenceTimeEntryParams'
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
