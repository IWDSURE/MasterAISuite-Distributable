# CMP_TCS_PER_PRD_FEEDBACK_SEC_V

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsperprdfeedbacksecv-6835.html#cmptcsperprdfeedbacksecv-6835](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsperprdfeedbacksecv-6835.html#cmptcsperprdfeedbacksecv-6835)

## Columns

- PER_PERD_FEEDBACK_ID
- PER_PERD_ID
- PERD_RUN_ID
- STMT_ID
- STMT_PERD_ID
- PERSON_ID
- RATING_CODE
- FEEDBACK1
- FEEDBACK2
- FEEDBACK3
- FEEDBACK4
- FEEDBACK5
- CONFIRMED_FLAG
- REQUEST_ID
- JOB_DEFINITION_NAME
- JOB_DEFINITION_PACKAGE
- CREATED_BY
- CREATION_DATE
- LAST_UPDATE_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_LOGIN
- OBJECT_VERSION_NUMBER

## Query

```sql
SELECT per_perd_feedback_id, per_perd_id, perd_run_id, stmt_id, stmt_perd_id, person_id, rating_code, feedback1, feedback2, feedback3, feedback4, feedback5, confirmed_flag, request_id, job_definition_name, job_definition_package, created_by, creation_date, last_update_date, last_updated_by, last_update_login, object_version_number FROM cmp_tcs_per_perd_feedbacks
```

---

[← Back to Index](../7_Compensation_Views_Index.md)
