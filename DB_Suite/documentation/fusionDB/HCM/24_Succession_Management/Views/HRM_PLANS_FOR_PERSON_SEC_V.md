# HRM_PLANS_FOR_PERSON_SEC_V

## Details

**Schema:** FUSION

**Object owner:** HRM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmplansforpersonsecv-6624.html#hrmplansforpersonsecv-6624](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmplansforpersonsecv-6624.html#hrmplansforpersonsecv-6624)

## Columns

- PERSON_ID
- PLAN_ID
- ENTERPRISE_ID
- PLAN_NAME
- PLAN_TYPE
- STATUS
- ACCESS_TYPE_CODE
- JOB_ID
- POSITION_ID

## Query

```sql
SELECT PlanIncumbents.INCUMBENT_PERSON_ID PERSON_ID, Plans.PLAN_ID, Plans.ENTERPRISE_ID, Plans.PLAN_NAME, Plans.PLAN_TYPE, Plans.STATUS, Plans.ACCESS_TYPE_CODE, Plans.JOB_ID, Plans.POSITION_ID FROM HRM_PLAN_INCUMBENTS PlanIncumbents, HRM_PLANS Plans WHERE PlanIncumbents.PLAN_ID = Plans.PLAN_ID AND Plans.LATEST_RECORD_FLAG='Y'
```

---

[← Back to Index](../24_Succession_Management_Views_Index.md)
