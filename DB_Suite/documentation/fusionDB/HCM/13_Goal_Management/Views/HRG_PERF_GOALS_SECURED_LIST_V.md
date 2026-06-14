# HRG_PERF_GOALS_SECURED_LIST_V

## Details

**Schema:** FUSION

**Object owner:** HRG

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgperfgoalssecuredlistv-3079.html#hrgperfgoalssecuredlistv-3079](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgperfgoalssecuredlistv-3079.html#hrgperfgoalssecuredlistv-3079)

## Columns

- PERSON_ID

## Query

```sql
SELECT PersonDPEO.PERSON_ID FROM PER_ALL_PEOPLE_F PersonDPEO WHERE TRUNC(SYSDATE) BETWEEN PersonDPEO.EFFECTIVE_START_DATE AND PersonDPEO.EFFECTIVE_END_DATE
```

---

[← Back to Index](../13_Goal_Management_Views_Index.md)
