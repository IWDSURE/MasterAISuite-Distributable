# HRA_MS_EVT_EVALUATIONS_V

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hramsevtevaluationsv-8729.html#hramsevtevaluationsv-8729](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hramsevtevaluationsv-8729.html#hramsevtevaluationsv-8729)

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
SELECT he.worker_id person_id, he.assignment_id assignment_id, EXTRACT(YEAR FROM trunc(he.evaluation_date)) event_year, he.evaluation_date event_date, 0 event_days, '{"strKey":"OLabelCompletedPerformanceDocument1"}' event_title, htp.customary_name event_details, '?evaluationId=' || he.evaluation_id || '&workerPersonId=' || he.worker_id || '&workerAssignmentId=' || he.assignment_id || case when (he.manager_id = nvl(hrc_session_util.get_user_personid, - 1) ) then '&loggedInPersonRole=MANAGER&calledFrom=PERSON_SPOTLIGHT' else '&loggedInPersonRole=OTHERS&calledFrom=PERSON_SPOTLIGHT' end link_text FROM hra_evaluations he, hra_eval_roles her, hra_tmpl_periods_vl htp, hrt_review_periods_vl hrp WHERE he.evaluation_id = her.evaluation_id AND he.business_group_id = her.business_group_id AND her.role_type_code = 'WORKER' AND he.tmpl_period_id = htp.tmpl_period_id AND he.business_group_id = htp.business_group_id AND he.review_period_id = hrp.review_period_id AND he.business_group_id = hrp.business_group_id AND he.status_code = 'COMP'
```

---

[← Back to Index](../19_Performance_Management_Views_Index.md)
