# HWM_ALLOCATION_RULES_DTL_X

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmallocationrulesdtlx-6206.html#hwmallocationrulesdtlx-6206](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmallocationrulesdtlx-6206.html#hwmallocationrulesdtlx-6206)

## Columns

- ALLOCATION_ID
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- OBJECT_VERSION_NUMBER
- ENTERPRISE_ID
- ALLOCATION_NAME
- DESCRIPTION
- ALLOCATION_RULE_ID
- ALLOCATION_RULE_PRIORITY
- TCAT_ID
- ALLOCATION_TYPE
- RUN_SUMMATION_LEVEL
- DATA_LEVEL

## Query

```sql
SELECT hdr.ALLOCATION_ID ,hdr.EFFECTIVE_START_DATE ,hdr.EFFECTIVE_END_DATE ,hdr.OBJECT_VERSION_NUMBER ,hdr.ENTERPRISE_ID ,hdr.ALLOCATION_NAME ,hdr.DESCRIPTION ,rul.ALLOCATION_RULE_ID ,rul.ALLOCATION_RULE_PRIORITY ,rul.TCAT_ID ,rul.ALLOCATION_TYPE ,rul.RUN_SUMMATION_LEVEL ,rul.DATA_LEVEL FROM HWM_ALLOCATIONS_HDR_vl hdr, HWM_ALLOCATION_RULES_F rul WHERE hdr.ALLOCATION_ID = rul.ALLOCATION_ID and hdr.EFFECTIVE_START_DATE = rul.EFFECTIVE_START_DATE and hdr.EFFECTIVE_END_DATE = rul.EFFECTIVE_END_DATE
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
