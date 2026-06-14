# HWM_EXT_ACT_ALLOC_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmextactallocv-3664.html#hwmextactallocv-3664](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmextactallocv-3664.html#hwmextactallocv-3664)

## Columns

- RESOURCE_ID
- ALLOCATION_DATE
- ALLOCATION_ID
- ALLOCATION_VERSION

## Query

```sql
select alloc.resource_ID, alloc.allocation_date, alloc.TM_ACT_ALLOC_ID allocation_id, alloc.TM_ACT_ALLOC_VERSION allocation_version from HWM_TM_ACT_ALLOCS alloc,HWM_TM_ACT_ALLOC_STATUSES stat, PER_ALL_PEOPLE_F pap where alloc.resource_id = pap.person_id and pap.person_number = nvl(pay_report_utils.get_parameter_value('PERSON_NUMBER'),pap.person_number) and alloc.allocation_date between nvl(trunc(pay_report_utils.get_parameter_value_date('START_DATE')), to_date('1952-01-01','YYYY-MM-DD')) and nvl(trunc(pay_report_utils.get_parameter_value_date('EFFECTIVE_DATE')), to_date('4712-12-31','YYYY-MM-DD')) and stat.TM_ACT_ALLOC_ID = alloc.TM_ACT_ALLOC_ID and stat.TM_ACT_ALLOC_VERSION = alloc.TM_ACT_ALLOC_VERSION and systimestamp between stat.date_from and stat.date_to and alloc.latest_version='Y' and stat.allocation_status='ORA_HWM_AA_VALID' and stat.TRANSFER_STATUS='ORA_HWM_AA_STAT_NOT_TRANS'
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
