# HWM_TM_REP_S_COMMON_ATRBS_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepscommonatrbsv-3838.html#hwmtmrepscommonatrbsv-3838](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepscommonatrbsv-3838.html#hwmtmrepscommonatrbsv-3838)

## Columns

- COMMON_TIME_REPOS_ATRB_ID
- COMMON_ATTRIBUTE_CATEGORY
- COMMON_INTERNAL_SOURCE
- COMMON_OWNER
- USAGES_SOURCE_ID
- USAGES_SOURCE_VERSION

## Query

```sql
SELECT CommonAtrbs.tm_rep_atrb_id Common_Time_Repos_Atrb_Id, CommonAtrbs.attribute_category Common_attribute_category, CommonAtrbs.attribute_varchar2 Common_internal_source, CommonAtrbs.attribute_varchar1 Common_Owner, CommonAtrbsUsg.usages_source_id, CommonAtrbsUsg.usages_source_version FROM hwm_tm_rep_atrbs CommonAtrbs, hwm_tm_rep_atrb_usages CommonAtrbsUsg WHERE CommonAtrbs.tm_rep_atrb_id = CommonAtrbsUsg.tm_rep_atrb_id and CommonAtrbs.attribute_category = 'CommonAttributes'
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
