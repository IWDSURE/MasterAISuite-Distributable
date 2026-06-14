# CMP_MS_ANA_CURRENT_SAL_V

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmsanacurrentsalv-4450.html#cmpmsanacurrentsalv-4450](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmsanacurrentsalv-4450.html#cmpmsanacurrentsalv-4450)

## Query

```sql
SELECT a.person_id, a.assignment_id, '{"strKey":"HdrSSalary1"}' text_title, hrl_df_util.number_to_char(a.salary_amount) || ' ' || a.currency_code || ' ' || a.salary_frequency text_metric, decode(trunc(months_between(trunc(sysdate), a.date_from)), 0, '{"strKey":"PgHISALCHNGthismonth","tokens":{"SAL_CHNG":"', 1, '{"strKey":"PgHISALCHNGlastmonth","tokens":{"SAL_CHNG":"', '{"strKey":"PgHISALCHNGMONDURago","tokens":{"SAL_CHNG":"') || decode(a.last_change_amount, NULL, '', decode(sign(nvl(a.last_change_amount, 0)), 1, '+', - 1, '', 0, NULL) || hrl_df_util.number_to_char(round(last_change_percent, 2)) || '% (' || hrl_df_util.number_to_char(round(a.last_change_amount, 2)) || ')') || '"' || decode(trunc(months_between(trunc(sysdate), a.date_from)), 0, '}}', 1, '}}', ',"MON_DUR":"' || trunc(months_between(trunc(sysdate), a.date_from)) || '"}}') text_meta, decode(sign((sysdate - a.date_from) - 7), - 1, '{"strKey":"BdgNew3"}', NULL) badge_text, decode(sign((sysdate - a.date_from) - 7), - 1, 'info', NULL) badge_status, NULL period_chn_ind_val, NULL period_chn_ind_cmp, 'lineWithArea' chart_type, decode(sign(a.last_change_amount), 1, 'success', 'neutral') chart_color, ( SELECT JSON_ARRAYAGG( JSON_OBJECT( 'ID' IS hrl_df_util.date_to_char(date_from), 'Value' IS salary_amount ) ORDER BY date_from ) FROM ( SELECT date_from, salary_amount FROM cmp_salary WHERE assignment_id = a.assignment_id ORDER BY date_from DESC FETCH FIRST 5 ROWS ONLY ) ) chart_data, '?pPersonId=' || a.person_id || '&pAssignmentId=' || a.assignment_id || '&pAssignmentNumber=' || b.assignment_number || '&pBusinessTitle=' || b.assignment_name || '&pDisplayName=' || c.display_name || '&pPersonNumber=' || d.person_number || '&pEffectiveDate=' || to_char(sysdate, 'YYYY-MM-DD') link_text FROM cmp_asg_salary_v a, per_all_assignments_f b, per_person_names_f_v c, per_all_people_f d WHERE trunc(sysdate) BETWEEN a.date_from AND a.date_to AND a.assignment_id = b.assignment_id AND trunc(sysdate) BETWEEN b.effective_start_date AND b.effective_end_date AND a.person_id = c.person_id AND trunc(sysdate) BETWEEN c.effective_start_date AND c.effective_end_date AND a.person_id = d.person_id AND trunc(sysdate) BETWEEN d.effective_start_date AND d.effective_end_date
```

---

[← Back to Index](../7_Compensation_Views_Index.md)
