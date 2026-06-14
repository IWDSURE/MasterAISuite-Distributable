# PER_PS_ANA_CONTRACT_END_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpsanacontractendv-4675.html#perpsanacontractendv-4675](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpsanacontractendv-4675.html#perpsanacontractendv-4675)

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
SELECT asg.person_id person_id, asg.assignment_id assignment_id, '{"strKey":"HdrSContractend"}' text_title, hrl_df_util.date_to_char(ctr.contract_end_date) text_metric, decode(trunc(ctr.contract_end_date - trunc(sysdate)), 0, '{"strKey":"PgHIEndstoday"}', 1, '{"strKey":"PgHIEndstomorrow"}', '{"strKey":"PgHIEndinginDAYSNUMdays", "tokens":{"DAYS_NUM":"' ||(trunc(ctr.contract_end_date - trunc(sysdate))) || '"}}') text_meta, decode(sign((ctr.contract_end_date - trunc(sysdate)) - 8), - 1, '{"strKey":"BdgInfo"}', NULL) badge_text, decode(sign((ctr.contract_end_date - trunc(sysdate)) - 8), - 1, 'info', NULL) badge_status, NULL period_chn_ind_val, NULL period_chn_ind_cmp, NULL chart_type, NULL chart_color, NULL chart_data, '?pAssignmentId=' || asg.assignment_id link_text FROM per_contracts_f ctr, per_all_assignments_m asg WHERE asg.assignment_type IN ( 'E', 'C', 'N', 'P' ) AND asg.effective_latest_change = 'Y' AND trunc(sysdate) BETWEEN asg.effective_start_date AND asg.effective_end_date AND asg.contract_id = ctr.contract_id AND ctr.contract_end_date >= trunc(sysdate) AND ctr.effective_end_date = TO_DATE('31-12-4712', 'DD-MM-YYYY') AND trunc(ctr.contract_end_date - trunc(sysdate)) BETWEEN 0 AND 30
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
