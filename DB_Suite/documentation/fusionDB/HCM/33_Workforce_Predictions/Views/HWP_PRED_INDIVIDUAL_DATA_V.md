# HWP_PRED_INDIVIDUAL_DATA_V

## Details

**Schema:** FUSION

**Object owner:** HWP

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwppredindividualdatav-4966.html#hwppredindividualdatav-4966](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwppredindividualdatav-4966.html#hwppredindividualdatav-4966)

## Columns

- PERSON_ID
- ASSIGNMENT_ID
- ASSIGNMENT_NAME
- PRIMARY_FLAG
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- EFFECTIVE_SEQUENCE
- EFFECTIVE_LATEST_CHANGE
- JOB_ID
- GRADE_ID
- POSITION_ID
- LOCATION_ID
- ORGANIZATION_ID
- INDV_PREDICTED_PERFORMANCE
- INDV_POTENTIAL
- INDV_PREDICTED_RISK

## Query

```sql
SELECT paam.person_id, paam.assignment_id, paam.assignment_name, paam.primary_flag, paam.effective_start_date, paam.effective_end_date, paam.Effective_Sequence, paam.Effective_Latest_change, paam.job_id, paam.grade_id, paam.position_id, paam.location_id, paam.organization_id, pred.worker_pred_perf indv_predicted_performance, ((pred.worker_pred_perf * 0.1 + .4) * .80) indv_potential, risk.is_emp_prob indv_predicted_risk FROM per_all_assignments_m paam, hwp_pred_perf_results_v pred, hwp_pred_attr_results_v risk WHERE paam.person_id = pred.person_id(+) and paam.assignment_id = pred.assignment_id(+) AND paam.person_id = risk.person_id(+) and paam.assignment_id = risk.assignment_id(+) AND TRUNC(sysdate) BETWEEN paam.effective_start_date AND paam.effective_end_date AND paam.assignment_type IN ('E' , 'C', 'N') AND paam.Effective_Latest_change = 'Y'
```

---

[← Back to Index](../33_Workforce_Predictions_Views_Index.md)
