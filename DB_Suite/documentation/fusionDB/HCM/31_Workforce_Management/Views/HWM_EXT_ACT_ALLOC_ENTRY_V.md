# HWM_EXT_ACT_ALLOC_ENTRY_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmextactallocentryv-7875.html#hwmextactallocentryv-7875](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmextactallocentryv-7875.html#hwmextactallocentryv-7875)

## Columns

- RESOURCE_ID
- ALLOCATION_DATE
- ALLOCATION_ID
- ALLOC_DATA_VERSION
- ALLOCATION_DURATION
- ACTION

## Query

```sql
select alloc.resource_ID, alloc.allocation_date, alloc.TM_ACT_ALLOC_ID allocation_id, alloc.TM_ACT_ALLOC_VERSION alloc_data_version, alloc.duration/60 allocation_duration, 'ADD' as action from HWM_TM_ACT_ALLOCS alloc, HWM_TM_ACT_ALLOC_STATUSES stat where stat.TM_ACT_ALLOC_ID = alloc.TM_ACT_ALLOC_ID and stat.TM_ACT_ALLOC_VERSION = alloc.TM_ACT_ALLOC_VERSION and systimestamp between stat.date_from and stat.date_to and alloc.latest_version='Y' and stat.allocation_status='ORA_HWM_AA_VALID' and stat.TRANSFER_STATUS='ORA_HWM_AA_STAT_NOT_TRANS' and alloc.delete_flag='N' union all select alloc.resource_ID, alloc.allocation_date, alloc.TM_ACT_ALLOC_ID allocation_id, alloc.TM_ACT_ALLOC_VERSION alloc_data_version, -1 * (alloc.duration/60) as allocation_duration, 'REMOVE' as action from HWM_TM_ACT_ALLOCS alloc, HWM_TM_ACT_ALLOC_STATUSES stat where stat.TM_ACT_ALLOC_ID = alloc.TM_ACT_ALLOC_ID and stat.TM_ACT_ALLOC_VERSION = alloc.TM_ACT_ALLOC_VERSION and systimestamp between stat.date_from and stat.date_to and alloc.latest_version='N' and stat.TRANSFER_STATUS='ORA_HWM_AA_STAT_TRANS' and alloc.TM_ACT_ALLOC_VERSION in (select max(aatab.TM_ACT_ALLOC_VERSION) from HWM_TM_ACT_ALLOCS aatab, HWM_TM_ACT_ALLOC_STATUSES stattab where alloc.TM_ACT_ALLOC_ID = aatab.TM_ACT_ALLOC_ID and aatab.TM_ACT_ALLOC_ID = stattab.TM_ACT_ALLOC_ID and aatab.TM_ACT_ALLOC_VERSION = stattab.TM_ACT_ALLOC_VERSION and systimestamp between stat.date_from and stat.date_to and stattab.transfer_status='ORA_HWM_AA_STAT_TRANS' and aatab.latest_version='N')
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
