# HWM_TM_REP_M_PJC_DOC_ATRBS_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepmpjcdocatrbsv-5834.html#hwmtmrepmpjcdocatrbsv-5834](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepmpjcdocatrbsv-5834.html#hwmtmrepmpjcdocatrbsv-5834)

## Columns

- PJC_DOC_TIME_REPOS_ATRB_ID
- PJC_DOCUMENT_TYPE
- USAGES_SOURCE_ID
- USAGES_SOURCE_VERSION

## Query

```sql
SELECT PjcDocAtrbs.tm_rep_atrb_id Pjc_Doc_Time_Repos_Atrb_id, PjcDocAtrbs.attribute_category Pjc_Document_Type, PjcDocAtrbsUsg.usages_source_id, PjcDocAtrbsUsg.usages_source_version FROM HWM_TM_REP_ATRBS PjcDocAtrbs, hwm_tm_rep_atrb_usages PjcDocAtrbsUsg WHERE EXISTS (SELECT 1 FROM HWM_TM_ATRB_FLDS_B WHERE TM_ATRB_FLD_ID = MASTER_ATTRIBUTE_ID AND name = 'PJC_SYSTEM_LINKAGE_FUNCTION' ) and PjcDocAtrbs.tm_rep_atrb_id = PjcDocAtrbsUsg.tm_rep_atrb_id
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
