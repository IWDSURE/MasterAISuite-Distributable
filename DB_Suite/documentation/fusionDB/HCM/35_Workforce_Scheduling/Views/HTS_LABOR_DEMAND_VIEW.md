# HTS_LABOR_DEMAND_VIEW

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htslabordemandview-5603.html#htslabordemandview-5603](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htslabordemandview-5603.html#htslabordemandview-5603)

## Columns

- DEMAND_DATE
- SCHEDULER_PROFILE_ID
- RESOURCES_REQUIRED

## Query

```sql
select prfl.demand_date, prfl.scheduler_profile_id, nvl(dated.value, prfl.resources_required) resources_required from hts_labor_demand_prfl_dated_v prfl left outer join hts_labor_demand_vals dated on trunc(dated.from_date) = prfl.demand_date and prfl.scheduler_profile_id = dated.sched_profile_id
```

---

[← Back to Index](../35_Workforce_Scheduling_Views_Index.md)
