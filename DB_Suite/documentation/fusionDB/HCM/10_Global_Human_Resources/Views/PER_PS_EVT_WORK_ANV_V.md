# PER_PS_EVT_WORK_ANV_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpsevtworkanvv-4576.html#perpsevtworkanvv-4576](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpsevtworkanvv-4576.html#perpsevtworkanvv-4576)

## Columns

- PERSON_ID
- ASSIGNMENT_ID
- EVENT_YEAR
- EVENT_DAYS
- EVENT_TITLE
- EVENT_DETAILS
- EVENT_DATE
- LINK_TEXT

## Query

```sql
SELECT asg.person_id person_id, asg.assignment_id assignment_id, to_char(add_months(anv.anniversary_date, 12 * yrs.ycnt), 'YYYY') event_year, 0 event_days, '{"strKey":"HdrSWorkanniversary"}' event_title, '{"strKey":"FdHIYearYEARNUM", "tokens":{"YEAR_NUM":"' || yrs.ycnt || '"}}' event_details, add_months(anv.anniversary_date, 12 * yrs.ycnt) event_date, '?pAssignmentId=' || asg.assignment_id link_text FROM per_all_assignments_m asg, ( SELECT person_id, period_type, MIN(date_start) anniversary_date, ceil(months_between(sysdate, MIN(date_start)) / 12) tot_years FROM per_periods_of_service GROUP BY person_id, period_type ) anv, ( SELECT level - 1 ycnt FROM dual CONNECT BY level <= 60 ) yrs WHERE trunc(sysdate) BETWEEN asg.effective_start_date AND asg.effective_end_date AND asg.effective_latest_change = 'Y' AND asg.person_id = anv.person_id AND asg.assignment_type = anv.period_type AND ( yrs.ycnt >= 1 AND yrs.ycnt <= anv.tot_years )
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
