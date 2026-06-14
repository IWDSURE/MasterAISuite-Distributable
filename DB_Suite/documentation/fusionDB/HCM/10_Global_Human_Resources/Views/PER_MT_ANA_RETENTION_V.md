# PER_MT_ANA_RETENTION_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/permtanaretentionv-7105.html#permtanaretentionv-7105](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/permtanaretentionv-7105.html#permtanaretentionv-7105)

## Columns

- PERSON_ID
- ASSIGNMENT_ID
- TEXT_TITLE
- TEXT_METRIC
- TEXT_META
- BADGE_TEXT
- BADGE_STATUS
- PERIOD_CHN_IND_VAL
- PERIOD_CHN_IND_CMP
- CHART_TYPE
- CHART_COLOR
- CHART_DATA
- LINK_TEXT

## Query

```sql
select x.person_id person_id, x.assignment_id assignment_id, '{"strKey":"HdrSRetention1"}' text_title, round(1- (NVL(y.term_cnt,0) / (decode(nvl(z1.tot_cnt,0)+nvl(z2.tot_cnt,0), 0, null, nvl(z1.tot_cnt,0)+nvl(z2.tot_cnt,0)) /2)),2) * 100 || '%' text_metric, '{"strKey":"PgHIInyourorganization"}' text_meta, NULL badge_text, NULL badge_status, NULL period_chn_ind_val, NULL period_chn_ind_cmp, NULL chart_type, NULL chart_color, NULL chart_data, NULL link_text from per_all_assignments_f x, (select manager_id, manager_assignment_id, count(*) term_cnt from per_manager_hrchy_dn x, per_all_assignments_m a, per_action_occurrences b, per_actions_vl d WHERE x.person_id = a.person_id and x.assignment_id = a.assignment_id and x.manager_type = 'LINE_MANAGER' and a.effective_start_date-1 between x.effective_start_date and x.effective_end_date and a.action_occurrence_id = b.action_occurrence_id AND a.assignment_type IN ( 'E', 'C','N','P' ) AND b.action_id = d.action_id and d.action_type_code = 'EMPL_TERMINATE' and a.effective_start_date between sysdate-365 and sysdate group by manager_id, manager_assignment_id ) y, (select manager_id, manager_assignment_id, count(*) tot_cnt from per_manager_hrchy_dn x, per_all_assignments_m a where x.person_id = a.person_id and x.assignment_id = a.assignment_id and x.manager_type = 'LINE_MANAGER' and trunc(sysdate) between x.effective_start_date and x.effective_end_date and trunc(sysdate) between a.effective_start_date and a.effective_end_date AND a.assignment_type IN ( 'E', 'C','N','P' ) and a.assignment_status_type != 'INACTIVE' group by manager_id, manager_assignment_id ) z1, (select manager_id, manager_assignment_id, count(*) tot_cnt from per_manager_hrchy_dn x, per_all_assignments_m a where x.person_id = a.person_id and x.assignment_id = a.assignment_id and x.manager_type = 'LINE_MANAGER' and trunc(sysdate)-365 between x.effective_start_date and x.effective_end_date and trunc(sysdate)-365 between a.effective_start_date and a.effective_end_date AND a.assignment_type IN ( 'E', 'C','N','P' ) and a.assignment_status_type != 'INACTIVE' group by manager_id, manager_assignment_id ) z2 where trunc(sysdate) between x.effective_start_date and x.effective_end_date and assignment_type IN ('E','C','N','P') and x.person_id = y.manager_id(+) and x.assignment_id = z1.manager_assignment_id(+) and x.person_id = z1.manager_id(+) and x.assignment_id = y.manager_assignment_id(+) and x.person_id = z2.manager_id(+) and x.assignment_id = z2.manager_assignment_id(+)
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
