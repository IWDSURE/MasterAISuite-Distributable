# HWM_TM_REP_S_ABS_HP_ATRBS_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepsabshpatrbsv-6372.html#hwmtmrepsabshpatrbsv-6372](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepsabshpatrbsv-6372.html#hwmtmrepsabshpatrbsv-6372)

## Columns

- ANC_TIME_REPOS_ATRB_ID
- ANC_ATTRIBUTE_CATEGORY
- ANC_ABSENCE_ENTRY_ID
- ANC_END_OF_BREAKDOWN
- USAGES_SOURCE_ID
- USAGES_SOURCE_VERSION

## Query

```sql
select TimeAttribute.tm_rep_atrb_id Anc_Time_Repos_Atrb_id, TimeAttribute.attribute_category Anc_Attribute_Category, TimeAttribute.attribute_number3 Anc_Absence_Entry_Id, TimeAttribute.attribute_timestamp1 Anc_End_Of_Breakdown, TimeAttributeUsages.usages_source_id, TimeAttributeUsages.usages_source_version from HWM_TM_REC_GRP TimeCard, HWM_TM_REC_GRP_USAGES TimeRecordGroupUsages, HWM_TM_REC TimeEntry, HWM_TM_REP_ATRBS TimeAttribute, HWM_TM_REP_ATRB_USAGES TimeAttributeUsages where TimeCard.TM_REC_GRP_ID = TimeRecordGroupUsages.TM_REC_GRP_ID and TimeCard.TM_REC_GRP_VERSION = TimeRecordGroupUsages.TM_REC_GRP_VERSION and TimeEntry.TM_REC_ID = TimeRecordGroupUsages.TM_REC_ID and TimeEntry.TM_REC_VERSION = TimeRecordGroupUsages.TM_REC_VERSION and TimeEntry.TM_REC_ID = TimeAttributeUsages.USAGES_SOURCE_ID and TimeEntry.TM_REC_VERSION = TimeAttributeUsages.USAGES_SOURCE_VERSION and TimeAttribute.TM_REP_ATRB_ID = TimeAttributeUsages.TM_REP_ATRB_ID and TimeCard.GRP_TYPE_ID = 105 and TimeAttribute.attribute_category = 'AbsenceHeaderParams'
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
