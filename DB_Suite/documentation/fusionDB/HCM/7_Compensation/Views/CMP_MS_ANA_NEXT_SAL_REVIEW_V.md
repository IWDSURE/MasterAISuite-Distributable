# CMP_MS_ANA_NEXT_SAL_REVIEW_V

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmsananextsalreviewv-3928.html#cmpmsananextsalreviewv-3928](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmsananextsalreviewv-3928.html#cmpmsananextsalreviewv-3928)

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
SELECT a.person_id, a.assignment_id, '{"strKey":"HdrSSalaryreviewdue"}' text_title, '{"strKey":"FdHIOnDATE", "tokens":{"DATE":"' || hrl_df_util.date_to_char(next_sal_review_date) || '"}}' text_metric, hrl_df_util.number_to_char(a.salary_amount) || ' ' || a.currency_code || ' ' || a.salary_frequency text_meta, decode(sign((next_sal_review_date - sysdate) - 7), - 1, '{"strKey":"BdgNew3"}', NULL) badge_text, decode(sign((next_sal_review_date - sysdate) - 7), - 1, 'info', NULL) badge_status, NULL period_chn_ind_val, NULL period_chn_ind_cmp, NULL chart_type, NULL chart_color, NULL chart_data, '?pPersonId=' || b.person_id || '&pAssignmentId=' || b.assignment_id || '&pAssignmentNumber=' || b.assignment_number || '&pBusinessTitle=' || b.assignment_name || '&pDisplayName=' || c.display_name || '&pPersonNumber=' || d.person_number || '&pEffectiveDate=' || to_char(sysdate, 'YYYY-MM-DD') link_text FROM cmp_asg_salary_v a, per_all_assignments_f b, per_person_names_f_v c, per_all_people_f d WHERE 1 = 1 AND a.assignment_id = b.assignment_id AND trunc(sysdate) BETWEEN b.effective_start_date AND b.effective_end_date AND b.person_id = c.person_id AND trunc(sysdate) BETWEEN c.effective_start_date AND c.effective_end_date AND b.person_id = d.person_id AND trunc(sysdate) BETWEEN d.effective_start_date AND d.effective_end_date AND trunc(sysdate) BETWEEN a.date_from AND a.date_to AND ( next_sal_review_date - trunc(sysdate) ) BETWEEN 0 AND 30
```

---

[← Back to Index](../7_Compensation_Views_Index.md)
