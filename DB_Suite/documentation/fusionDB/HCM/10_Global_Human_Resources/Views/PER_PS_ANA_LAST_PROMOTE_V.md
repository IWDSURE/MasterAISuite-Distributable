# PER_PS_ANA_LAST_PROMOTE_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpsanalastpromotev-3119.html#perpsanalastpromotev-3119](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpsanalastpromotev-3119.html#perpsanalastpromotev-3119)

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
SELECT asg.person_id person_id, asg.assignment_id assignment_id, '{"strKey":"HdrSLastpromotion"}' text_title, hrl_df_util.date_to_char(asg.effective_start_date) text_metric, decode(trunc(trunc(sysdate) - asg.effective_start_date), 0, '{"strKey":"PgHIYouvebeenpromotedCongratulations"}', 1, '{"strKey":"PgHIYesterday"}', '{"strKey":"PgHIDAYSNUMdaysago", "tokens":{"DAYS_NUM":"' ||(trunc(trunc(sysdate) - asg.effective_start_date)) || '"}}') text_meta, decode(sign((trunc(sysdate) - asg.effective_start_date) - 8), - 1, '{"strKey":"BdgInfo"}', NULL) badge_text, decode(sign((trunc(sysdate) - asg.effective_start_date) - 8), - 1, 'info', NULL) badge_status, NULL period_chn_ind_val, NULL period_chn_ind_cmp, NULL chart_type, NULL chart_color, NULL chart_data, '?pAssignmentId=' || asg.assignment_id link_text FROM per_all_assignments_m asg WHERE asg.assignment_type IN ( 'E', 'C', 'N', 'P' ) AND asg.effective_latest_change = 'Y' AND asg.effective_start_date = ( SELECT MAX(a.effective_start_date) AS date_of_last_promotion FROM per_all_assignments_m a, per_action_occurrences c WHERE a.person_id = asg.person_id AND a.assignment_id = asg.assignment_id AND a.action_occurrence_id = c.action_occurrence_id AND a.effective_start_date <= trunc(sysdate) AND EXISTS ( SELECT 1 FROM per_actions_b b WHERE b.action_type_code = 'EMPL_PROMOTION' AND c.action_id = b.action_id ) ) AND trunc(trunc(sysdate) - asg.effective_start_date) BETWEEN 0 AND 30
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
