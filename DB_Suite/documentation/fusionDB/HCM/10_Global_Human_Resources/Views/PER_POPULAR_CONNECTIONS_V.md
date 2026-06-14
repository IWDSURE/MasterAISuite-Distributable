# PER_POPULAR_CONNECTIONS_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpopularconnectionsv-8414.html#perpopularconnectionsv-8414](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpopularconnectionsv-8414.html#perpopularconnectionsv-8414)

## Columns

- CONNECT_PERSON_ID
- CONNECT_ASSIGNMENT_ID
- CONNECT_TYPE
- JOB_ID
- CONNECT_COUNT

## Query

```sql
SELECT CONNECT_PERSON_ID, CONNECT_ASSIGNMENT_ID, CONNECT_TYPE, JOB_ID, COUNT(1) CONNECT_COUNT FROM PER_CONNECTION_LINKS PCL, PER_ALL_ASSIGNMENTS_M PAAM WHERE PCL.PERSON_ID = PAAM.PERSON_ID AND PCL.ASSIGNMENT_ID = PAAM.ASSIGNMENT_ID AND PAAM.ASSIGNMENT_STATUS_TYPE IN ('ACTIVE', 'SUSPENDED') AND TRUNC(SYSDATE) BETWEEN PAAM.EFFECTIVE_START_DATE AND PAAM.EFFECTIVE_END_DATE AND PAAM.EFFECTIVE_LATEST_CHANGE = 'Y' GROUP BY CONNECT_PERSON_ID, CONNECT_ASSIGNMENT_ID, CONNECT_TYPE, JOB_ID ORDER BY COUNT(1) DESC
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
