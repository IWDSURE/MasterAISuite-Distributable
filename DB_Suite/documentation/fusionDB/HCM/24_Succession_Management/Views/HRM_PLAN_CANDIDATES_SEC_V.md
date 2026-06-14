# HRM_PLAN_CANDIDATES_SEC_V

## Details

**Schema:** FUSION

**Object owner:** HRM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmplancandidatessecv-4361.html#hrmplancandidatessecv-4361](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmplancandidatessecv-4361.html#hrmplancandidatessecv-4361)

## Columns

- PLAN_CANDIDATE_ID
- ENTERPRISE_ID
- PLAN_ID
- PERSON_ID
- STATUS
- SUCCESSION_STATUS
- SHOW_SUCCESSION_STATUS_FLAG
- CANDIDATE_TYPE
- EXTERNAL_CANDIDATE_ID
- READINESS_CODE
- CANDIDATE_RANKING
- EMERGENCY_SUCCESSOR

## Query

```sql
SELECT PlanCandidateEO.PLAN_CANDIDATE_ID, PlanCandidateEO.ENTERPRISE_ID, PlanCandidateEO.PLAN_ID, PlanCandidateEO.PERSON_ID, PlanCandidateEO.STATUS, PlanCandidateEO.SUCCESSION_STATUS, PlanCandidateEO.SHOW_SUCCESSION_STATUS_FLAG, PlanCandidateEO.CANDIDATE_TYPE, PlanCandidateEO.EXTERNAL_CANDIDATE_ID, PlanCandidateEO.READINESS_CODE, PlanCandidateEO.CANDIDATE_RANKING, PlanCandidateEO.EMERGENCY_SUCCESSOR FROM HRM_PLAN_CANDIDATES PlanCandidateEO WHERE PlanCandidateEO.LATEST_RECORD_FLAG='Y'
```

---

[← Back to Index](../24_Succession_Management_Views_Index.md)
