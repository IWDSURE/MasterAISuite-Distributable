# PER_MT_ANA_WORKERS_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/permtanaworkersv-8435.html#permtanaworkersv-8435](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/permtanaworkersv-8435.html#permtanaworkersv-8435)

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
SELECT sup.manager_id person_id, sup.manager_assignment_id assignment_id, '{"strKey":"HdrSWorkers"}' text_title, '{"strKey":"PgHIDIRNUMdirectsTOTNUMtotal", "tokens":{"DIR_NUM":"' || nvl(SUM(decode(sup.manager_level, 1, 1, 0)),0) || '","TOT_NUM":"' || COUNT(1) || '"}}' text_metric, '{"strKey":"PgHIInyourorganization"}' text_meta, NULL badge_text, NULL badge_status, NULL period_chn_ind_val, NULL period_chn_ind_cmp, NULL chart_type, NULL chart_color, NULL chart_data, NULL link_text FROM per_manager_hrchy_dn sup, per_all_assignments_f paaf WHERE trunc(sysdate) BETWEEN sup.effective_start_date AND sup.effective_end_date and paaf.person_id = sup.person_id and paaf.assignment_id = sup.assignment_id and trunc(sysdate) BETWEEN paaf.effective_start_date AND paaf.effective_end_date and paaf.assignment_status_type != 'INACTIVE' and paaf.assignment_type IN ('E','C','N','P') and sup.manager_type = 'LINE_MANAGER' GROUP BY sup.manager_id, sup.manager_assignment_id
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
