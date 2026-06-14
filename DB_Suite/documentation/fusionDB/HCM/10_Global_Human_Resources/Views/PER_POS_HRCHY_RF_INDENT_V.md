# PER_POS_HRCHY_RF_INDENT_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perposhrchyrfindentv-5387.html#perposhrchyrfindentv-5387](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perposhrchyrfindentv-5387.html#perposhrchyrfindentv-5387)

## Columns

- POSITION_CODE_OR_ID_INDENTED
- ESD
- EED
- LEV
- LAST_UPDATE_DATE
- POSITION_ID_INDENTED
- ANCESTOR_POSITION_ID
- POSITION_ID
- POS_CODE_UPPER
- ANCESTOR_POS_CODE_UPPER
- POS_CODE
- ANCESTOR_POS_CODE
- LAST_UPDATE_LOGIN
- BUSINESS_UNIT
- BUSINESS_GROUP_ID

## Query

```sql
select /*+ FIRST_ROWS(20) USE_NL(p h pp)*/ lpad(' from hr_all_positions_f p, PER_POSITION_HRCHY_RF h, hr_all_positions_f pp, fusion.FUN_ALL_BUSINESS_UNITS_V b where h.position_id=p.position_id(+) and h.business_group_id=p.business_group_id(+) and h.effective_start_date between p.effective_start_date(+) and p.effective_end_date(+) and h.ancestor_position_id=pp.position_id(+) and h.business_group_id=pp.business_group_id(+) and h.effective_start_date between pp.effective_start_date(+) and pp.effective_end_date(+) and p.business_unit_id = b.bu_id and p.business_group_id = b.business_group_id order by position_id desc,h.effective_start_date,node_level
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
