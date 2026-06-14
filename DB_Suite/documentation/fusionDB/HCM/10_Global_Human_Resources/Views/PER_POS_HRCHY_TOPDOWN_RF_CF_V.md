# PER_POS_HRCHY_TOPDOWN_RF_CF_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perposhrchytopdownrfcfv-6781.html#perposhrchytopdownrfcfv-6781](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perposhrchytopdownrfcfv-6781.html#perposhrchytopdownrfcfv-6781)

## Columns

- POSITION_ID
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- CHILD_LEVEL
- CHILD_POS_ID1
- CHILD_POS_ID2
- CHILD_POS_ID3
- CHILD_POS_ID4
- CHILD_POS_ID5
- CHILD_POS_ID6
- CHILD_POS_ID7
- CHILD_POS_ID8
- CHILD_POS_ID9
- CHILD_POS_ID10
- CHILD_POS_ID11
- CHILD_POS_ID12
- CHILD_POS_ID13
- CHILD_POS_ID14
- CHILD_POS_ID15
- NONNULL_CHILD_POS_ID15

## Query

```sql
SELECT /*+ NO_MERGE*/ top_ancestor_position_id position_id, top_effective_start_date effective_start_date, top_effective_end_date effective_end_date, top_pos_level child_level, MAX(case when ldiff = 1 then mid_ancestor_position_id when ldiff = 0 and mid_pos_level = 1 then top_position_id end) child_pos_id1 , MAX(case when ldiff = 2 then mid_ancestor_position_id when ldiff = 1 and mid_pos_level = 1 then top_position_id end) child_pos_id2 , MAX(case when ldiff = 3 then mid_ancestor_position_id when ldiff = 2 and mid_pos_level = 1 then top_position_id end) child_pos_id3 , MAX(case when ldiff = 4 then mid_ancestor_position_id when ldiff = 3 and mid_pos_level = 1 then top_position_id end) child_pos_id4 , MAX(case when ldiff = 5 then mid_ancestor_position_id when ldiff = 4 and mid_pos_level = 1 then top_position_id end) child_pos_id5 , MAX(case when ldiff = 6 then mid_ancestor_position_id when ldiff = 5 and mid_pos_level = 1 then top_position_id end) child_pos_id6 , MAX(case when ldiff = 7 then mid_ancestor_position_id when ldiff = 6 and mid_pos_level = 1 then top_position_id end) child_pos_id7 , MAX(case when ldiff = 8 then mid_ancestor_position_id when ldiff = 7 and mid_pos_level = 1 then top_position_id end) child_pos_id8 , MAX(case when ldiff = 9 then mid_ancestor_position_id when ldiff = 8 and mid_pos_level = 1 then top_position_id end) child_pos_id9 , MAX(case when ldiff = 10 then mid_ancestor_position_id when ldiff = 9 and mid_pos_level = 1 then top_position_id end) child_pos_id10 , MAX(case when ldiff = 11 then mid_ancestor_position_id when ldiff = 10 and mid_pos_level = 1 then top_position_id end) child_pos_id11 , MAX(case when ldiff = 12 then mid_ancestor_position_id when ldiff = 11 and mid_pos_level = 1 then top_position_id end) child_pos_id12 , MAX(case when ldiff = 13 then mid_ancestor_position_id when ldiff = 12 and mid_pos_level = 1 then top_position_id end) child_pos_id13 , MAX(case when ldiff = 14 then mid_ancestor_position_id when ldiff = 13 and mid_pos_level = 1 then top_position_id end) child_pos_id14 , MAX(case when ldiff = 15 then mid_ancestor_position_id when ldiff = 14 and mid_pos_level = 1 then top_position_id end) child_pos_id15 , MAX(case when ldiff = 15 then mid_ancestor_position_id else top_position_id end) nonnull_child_pos_id15 FROM ( SELECT toppos.effective_start_date top_effective_start_date, toppos.effective_end_date top_effective_end_date, toppos.position_id top_position_id, toppos.ancestor_position_id top_ancestor_position_id, toppos.node_level top_pos_level, midpos.effective_start_date mid_effective_start_date, midpos.effective_end_date mid_effective_end_date, midpos.position_id mid_position_id, midpos.ancestor_position_id mid_ancestor_position_id, midpos.node_level mid_pos_level, (toppos.node_level - midpos.node_level) ldiff FROM PER_POSITION_HRCHY_RF toppos, PER_POSITION_HRCHY_RF midpos WHERE midpos.position_id = toppos.position_id AND toppos.effective_start_date between midpos.effective_start_date and midpos.effective_end_date AND midpos.node_level <= toppos.node_level ) GROUP BY top_position_id, top_ancestor_position_id, TOP_EFFECTIVE_START_DATE ,TOP_EFFECTIVE_END_DATE,top_pos_level
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
