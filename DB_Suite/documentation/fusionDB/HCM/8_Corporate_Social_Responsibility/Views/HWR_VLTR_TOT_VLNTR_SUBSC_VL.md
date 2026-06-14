# HWR_VLTR_TOT_VLNTR_SUBSC_VL

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrtotvlntrsubscvl-6284.html#hwrvltrtotvlntrsubscvl-6284](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrtotvlntrsubscvl-6284.html#hwrvltrtotvlntrsubscvl-6284)

## Columns

- TOTALVOLUNTEERSUBSCRIBED

## Query

```sql
SELECT COUNT(DISTINCT(HCM_PERSON_ID)) TotalVolunteerSubscribed FROM HWR_VLTR_PER_PROFILE_VL
```

---

[← Back to Index](../8_Corporate_Social_Responsibility_Views_Index.md)
