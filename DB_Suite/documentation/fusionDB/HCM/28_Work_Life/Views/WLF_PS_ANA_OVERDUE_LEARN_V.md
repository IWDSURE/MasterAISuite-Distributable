# WLF_PS_ANA_OVERDUE_LEARN_V

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfpsanaoverduelearnv-3091.html#wlfpsanaoverduelearnv-3091](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfpsanaoverduelearnv-3091.html#wlfpsanaoverduelearnv-3091)

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
SELECT learner_id person_id, NULL assignment_id, '{"strKey":"HdrSOverduelearning"}' text_title, decode(COUNT(1), 1, '{"strKey":"FdHI1item"}', '{"strKey":"FdHIITEMNUMitems", "tokens":{"ITEM_NUM":"' || COUNT(1) || '"}}') text_metric, NULL text_meta, '{"strKey":"BdgOverdue1"}' badge_text, 'danger' badge_status, NULL period_chn_ind_val, NULL period_chn_ind_cmp, NULL chart_type, NULL chart_color, NULL chart_data, '' link_text FROM wlf_assignment_records_f WHERE calculated_due_date < trunc(sysdate) AND event_type IN ( 'ORA_REQUIRE_ASSIGNMENT', 'ORA_JOIN_ASSIGNMENT' ) AND status IN ( 'ORA_ASSN_REC_ACTIVE', 'ORA_ASSN_REC_CONTENT_COMPLETE', 'ORA_ASSN_REC_WITHDRAW_PENDING' ) AND learning_item_type IN ( 'ORA_COURSE', 'ORA_SPECIALIZATION', 'ORA_VIDEO', 'ORA_TUTORIAL', 'ORA_ELEARNING', 'ORA_NON_CATALOG', 'ORA_LEGACY' ) AND ( trunc(sysdate) BETWEEN effective_start_date AND effective_end_date ) GROUP BY learner_id
```

---

[← Back to Index](../28_Work_Life_Views_Index.md)
