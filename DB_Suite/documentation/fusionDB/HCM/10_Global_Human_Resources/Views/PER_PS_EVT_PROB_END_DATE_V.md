# PER_PS_EVT_PROB_END_DATE_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpsevtprobenddatev-4340.html#perpsevtprobenddatev-4340](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpsevtprobenddatev-4340.html#perpsevtprobenddatev-4340)

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
SELECT asg.person_id person_id, asg.assignment_id assignment_id, EXTRACT(YEAR FROM asg.date_probation_end) event_year, 0 event_days, '{"strKey":"FdHIProbationenddate"}' event_title, EXTRACT(YEAR FROM asg.date_probation_end) event_details, asg.date_probation_end event_date, '?pAssignmentId=' || asg.assignment_id link_text FROM per_all_assignments_m asg WHERE trunc(sysdate) BETWEEN asg.effective_start_date AND asg.effective_end_date AND asg.effective_latest_change = 'Y' AND asg.assignment_type IN ( 'E' ) AND asg.date_probation_end IS NOT NULL
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
