# PER_POS_HRCHY_TOPDOWN_INDENT_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perposhrchytopdownindentv-6154.html#perposhrchytopdownindentv-6154](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perposhrchytopdownindentv-6154.html#perposhrchytopdownindentv-6154)

## Columns

- POSITION_CODE_OR_ID_INDENTED
- BUSINESS_UNIT
- LAST_UPDATE_DATE
- CREATION_DATE
- POSITION_ID_INDENTED
- BUSINESS_GROUP_ID
- NODE_LEVEL
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- POSITION_CODE
- POSITION_CODE_UPPER
- TOP_POSITION_CODE
- TOP_POSITION_CODE_UPPER
- POSITION_ID
- TOP_POSITION_ID
- ORDER1
- IS_CYCLE

## Query

```sql
WITH level1 (ancestor_position_id,position_id,effective_start_date,effective_end_date,node_level,business_group_id) AS ( SELECT /*+ PARALLEL(DEFAULT)*/ nvl(hp.parent_position_id,hp.position_id) pos_id_start,nvl(hp.parent_position_id,hp.position_id) ,hp.effective_start_date, hp.effective_end_date ,1,hp.business_group_id from fusion.PER_POSITION_HIERARCHY_F hp where trunc(SYSDATE) between hp.effective_start_date and hp.effective_end_date and not exists (select 1 from fusion.PER_POSITION_HIERARCHY_F hc where hc.position_id = hp.parent_position_id and hc.business_group_id=hp.business_group_id and trunc(SYSDATE) between hc.effective_start_date and hc.effective_end_date) UNION ALL SELECT p.ancestor_position_id,c.position_id,greatest(c.effective_start_date,nvl(p.effective_start_date,c.effective_start_date)) ,least(c.effective_end_date, nvl(p.effective_end_date,c.effective_end_date)), node_level+1 /*provides recursion*/,c.business_group_id FROM fusion.PER_POSITION_HIERARCHY_F c, level1 p WHERE p.position_id = c.parent_position_id AND p.business_group_id=c.business_group_id AND trunc(SYSDATE) between c.effective_start_date and c.effective_end_date ) SEARCH DEPTH FIRST BY position_id desc SET order1 cycle position_id set is_cycle to '1' default '0' select /*+ FIRST_ROWS(20) PARALLEL(DEFAULT)*/ lpad('-',node_level*2,'-')|| node_level||'. '|| nvl(p.position_code,h.position_id||' (ID)') position_code_or_id_indented,b.bu_name business_unit, p.last_update_date,p.creation_date,lpad('-',node_level*2,'-')|| case when h.ancestor_position_id is not null then node_level||'. '|| h.ancestor_position_id||' - ' end || case when h.ancestor_position_id is null and h.position_id is not null then node_level || '. ' end || h.position_id position_id_indented, h.business_group_id,h.node_level,h.effective_start_date,h.effective_end_date,p.position_code,upper(p.position_code) position_code_upper, pp.position_code top_position_code,upper(pp.position_code) top_position_code_upper,h.position_id,h.ancestor_position_id top_position_id,h.order1,h.is_cycle from level1 h, hr_all_positions_f p, hr_all_positions_f pp, FUN_ALL_BUSINESS_UNITS_V b where h.position_id=p.position_id(+) and h.business_group_id=p.business_group_id(+) and h.effective_end_date between p.effective_start_date(+) and p.effective_end_date(+) and h.ancestor_position_id=pp.position_id(+) and h.business_group_id=pp.business_group_id(+) and h.effective_end_date between pp.effective_start_date(+) and pp.effective_end_date(+) and p.business_unit_id = b.bu_id and p.business_group_id = b.business_group_id order by order1
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
