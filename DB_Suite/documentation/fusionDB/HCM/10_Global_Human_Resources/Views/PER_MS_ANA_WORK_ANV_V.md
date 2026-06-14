# PER_MS_ANA_WORK_ANV_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/permsanaworkanvv-4802.html#permsanaworkanvv-4802](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/permsanaworkanvv-4802.html#permsanaworkanvv-4802)

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
SELECT asg.person_id person_id, asg.assignment_id assignment_id, '{"strKey":"HdrSWorkanniversary"}' text_title, hrl_df_util.date_to_char(add_months(anv.anniversary_date, 12 * yrs.ycnt)) text_metric, decode(trunc(add_months(anv.anniversary_date, 12 * yrs.ycnt) - trunc(sysdate)), 0, '{"strKey":"PgHIItstodaycongratulatethem"}', 1, '{"strKey":"PgHITomorrow"}', '{"strKey":"PgHIComingupinDAYSNUMdays", "tokens":{"DAYS_NUM":"' ||(trunc(add_months(anv.anniversary_date, 12 * yrs.ycnt) - trunc(sysdate)) || '"}}')) text_meta, decode(sign((add_months(anv.anniversary_date, 12 * yrs.ycnt) - trunc(sysdate)) - 8), - 1, '{"strKey":"BdgInfo"}', NULL) badge_text, decode(sign((add_months(anv.anniversary_date, 12 * yrs.ycnt) - trunc(sysdate)) - 8), - 1, 'info', NULL) badge_status, NULL period_chn_ind_val, NULL period_chn_ind_cmp, NULL chart_type, NULL chart_color, NULL chart_data, '?pAssignmentId=' || asg.assignment_id link_text FROM per_all_assignments_m asg, ( SELECT person_id, period_type, MIN(date_start) anniversary_date, ceil(months_between(trunc(sysdate), MIN(date_start)) / 12) tot_years FROM per_periods_of_service GROUP BY person_id, period_type ) anv, ( SELECT level - 1 ycnt FROM dual CONNECT BY level <= 60 ) yrs WHERE trunc(sysdate) BETWEEN asg.effective_start_date AND asg.effective_end_date AND asg.person_id = anv.person_id AND asg.assignment_type = anv.period_type AND asg.effective_latest_change = 'Y' AND yrs.ycnt >= 1 AND add_months(anv.anniversary_date, 12 * yrs.ycnt) BETWEEN trunc(sysdate) AND add_months(trunc(sysdate), 12) AND add_months(anv.anniversary_date, 12 * yrs.ycnt) BETWEEN trunc(sysdate) AND ( trunc(sysdate) + 30 )
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
