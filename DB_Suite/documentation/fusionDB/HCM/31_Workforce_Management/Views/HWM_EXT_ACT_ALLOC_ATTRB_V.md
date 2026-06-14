# HWM_EXT_ACT_ALLOC_ATTRB_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmextactallocattrbv-7514.html#hwmextactallocattrbv-7514](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmextactallocattrbv-7514.html#hwmextactallocattrbv-7514)

## Columns

- ALLOCATION_ID
- ALLOC_DETAILS_VERSION
- TIME_CARD_FLD_ID
- TIME_CARD_FLD_NAME
- DATA_TYPE
- VALUE_NUMBER
- VALUE_TEXT
- VALUE_DATE
- VALUE_TIMESTAMP
- DEFAULT_VALUE

## Query

```sql
select atrb.TM_ACT_ALLOC_ID as allocation_id, alloc.TM_ACT_ALLOC_VERSION as alloc_details_version, atrb.TM_CARD_FLD_ID as time_card_fld_id, tcfld.name as time_card_fld_name, atrb.DATA_TYPE as data_type, atrb.VALUE_NUMBER, atrb.VALUE_TEXT, (CASE WHEN atrb.DATA_TYPE='DATE' THEN atrb.VALUE_TIMESTAMP ELSE NULL end) as VALUE_DATE, (CASE WHEN atrb.DATA_TYPE='TIMESTAMP' THEN atrb.VALUE_TIMESTAMP ELSE NULL end) as VALUE_TIMESTAMP, atrb.is_default_value as default_value from HWM_TM_ACT_ALLOC_ATRBS atrb, HWM_TM_ACT_ALLOCS alloc,hxt_tclayfld_defns_vl tcfld where atrb.TM_ACT_ALLOC_ID = alloc.TM_ACT_ALLOC_ID and atrb.date_from <=alloc.date_from and alloc.date_to <= atrb.date_to and atrb.tm_card_fld_id=tcfld.tclayfld_defns_id(+)
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
