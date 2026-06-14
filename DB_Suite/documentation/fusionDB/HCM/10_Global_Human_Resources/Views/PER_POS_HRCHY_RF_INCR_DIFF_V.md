# PER_POS_HRCHY_RF_INCR_DIFF_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perposhrchyrfincrdiffv-4348.html#perposhrchyrfincrdiffv-4348](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perposhrchyrfincrdiffv-4348.html#perposhrchyrfincrdiffv-4348)

## Columns

- rowid
- TYPE
- POSITION_CODE_INDENTED
- POSITION_ID_INDENTED
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- NODE_LEVEL
- POSITION_ID
- POSITION_CODE
- ANCESTOR_POSITION_ID
- ANCESTOR_POSITION_CODE
- BUSINESS_GROUP_ID

## Query

```sql
WITH PER_POS_HRCHY_RF_COALESCED AS (SELECT /*+ parallel(default) */ position_id,ancestor_position_id,MIN (effective_start_date) AS effective_start_date, MAX (effective_end_date) AS effective_end_date,node_level FROM (SELECT /*+ parallel(default) */ f.* , ROW_NUMBER () OVER ( PARTITION by position_id,node_level ORDER BY ancestor_position_id,effective_start_date) - ROW_NUMBER () OVER ( PARTITION BY position_id,node_level,ancestor_position_id ORDER BY effective_start_date) AS output_group FROM fusion.PER_POSITION_HRCHY_RF f ) GROUP BY position_id,ancestor_position_id,node_level,output_group), PER_POS_HRCHY_RF_DYN (position_id,ancestor_position_id,effective_start_date,effective_end_date,node_level,business_group_id) AS ( SELECT position_id,parent_position_id ancestor_position_id,effective_start_date,effective_end_date,1 node_level,business_group_id from PER_POSITION_HIERARCHY_F WHERE parent_position_id is not null UNION ALL SELECT p.position_id,c.parent_position_id ancestor_position_id,greatest(c.effective_start_date,nvl(p.effective_start_date,c.effective_start_date)) ,least(c.effective_end_date, nvl(p.effective_end_date,c.effective_end_date)), node_level+1 node_level /*provides recursion*/, c.business_group_id business_group_id FROM PER_POSITION_HIERARCHY_F c, PER_POS_HRCHY_RF_DYN p WHERE c.position_id = p.ancestor_position_id AND c.business_group_id=p.business_group_id AND c.effective_end_date >= p.effective_start_date and p.effective_end_date >= c.effective_start_date AND c.parent_position_id is not null ), PER_POS_HRCHY_RF_DYN_COALESCED AS (SELECT /*+ parallel(default) */ position_id,ancestor_position_id,MIN (effective_start_date) AS effective_start_date, MAX (effective_end_date) AS effective_end_date,node_level FROM (SELECT /*+ parallel(default) */ f.* , ROW_NUMBER () OVER ( PARTITION by position_id,node_level ORDER BY ancestor_position_id,effective_start_date) - ROW_NUMBER () OVER ( PARTITION BY position_id,node_level,ancestor_position_id ORDER BY effective_start_date) AS output_group FROM PER_POS_HRCHY_RF_DYN f ) GROUP BY position_id,ancestor_position_id,node_level,output_group) select p.rowid "rowid",/*+ parallel(default) */ TYPE, lpad(' lpad(' h.effective_start_date,h.effective_end_date,node_level, h.position_id, p.position_code, ancestor_position_id,pp.position_code ancestor_position_code,p.business_group_id from (select /*+ parallel(default) */ 'DELETED' TYPE,a_b.* from ( select * from PER_POS_HRCHY_RF_DYN_COALESCED fo where (position_id,ancestor_position_id,effective_start_date,effective_end_date,node_level) in (select position_id,ancestor_position_id,effective_start_date,effective_end_date,node_level from PER_POS_HRCHY_RF_DYN_COALESCED minus select position_id,ancestor_position_id,effective_start_date,effective_end_date,node_level from PER_POS_HRCHY_RF_COALESCED)) a_b union all select /*+ parallel(default) */ 'ADDED',b_a.* from ( select * from PER_POS_HRCHY_RF_COALESCED fo where (position_id,ancestor_position_id,effective_start_date,effective_end_date,node_level) in (select position_id,ancestor_position_id,effective_start_date,effective_end_date,node_level from PER_POS_HRCHY_RF_COALESCED minus select position_id,ancestor_position_id,effective_start_date,effective_end_date,node_level from PER_POS_HRCHY_RF_DYN_COALESCED)) b_a ) h, hr_all_positions_f p, hr_all_positions_f pp where h.position_id=p.position_id(+) and h.effective_start_date between p.effective_start_date(+) and p.effective_end_date(+) and h.ancestor_position_id=pp.position_id(+) and h.effective_start_date between pp.effective_start_date(+) and pp.effective_end_date(+) order by position_id desc,node_level,effective_start_date
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
