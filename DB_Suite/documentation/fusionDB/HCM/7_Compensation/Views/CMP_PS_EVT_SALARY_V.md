# CMP_PS_EVT_SALARY_V

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmppsevtsalaryv-5963.html#cmppsevtsalaryv-5963](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmppsevtsalaryv-5963.html#cmppsevtsalaryv-5963)

## Columns

- PERSON_ID
- ASSIGNMENT_ID
- EVENT_YEAR
- EVENT_DATE
- EVENT_DAYS
- EVENT_TITLE
- EVENT_DETAILS
- LINK_TEXT

## Query

```sql
SELECT a.person_id person_id, a.assignment_id assignment_id, EXTRACT(YEAR FROM trunc(a.date_from)) event_year, a.date_from event_date, 0 event_days, a.action_name event_title, decode ( sign(NVL(a.last_change_percent,0)),0, '', decode(sign(NVL(a.last_change_amount,0)), 1, '{"strKey":"FdHISALCHNGincrease", "tokens":{"SAL_CHNG":"' || hrl_df_util.number_to_char(round(a.last_change_percent, 2)) || '%"}}', '{"strKey":"FdHISALCHNGdecrease", "tokens":{"SAL_CHNG":"' || hrl_df_util.number_to_char(round(a.last_change_percent * -1, 2)) || '%"}}' )) event_details, '?pSalaryId=' || a.salary_id || '&pAssignmentId=' || a.assignment_id link_text FROM cmp_asg_salary_v a WHERE 1 = 1 AND a.last_change_percent IS NOT NULL AND a.date_from <= trunc(SYSDATE)
```

---

[← Back to Index](../7_Compensation_Views_Index.md)
