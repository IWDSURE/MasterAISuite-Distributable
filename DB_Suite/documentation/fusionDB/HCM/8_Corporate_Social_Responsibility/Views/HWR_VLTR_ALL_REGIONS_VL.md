# HWR_VLTR_ALL_REGIONS_VL

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrallregionsvl-4681.html#hwrvltrallregionsvl-4681](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrallregionsvl-4681.html#hwrvltrallregionsvl-4681)

## Columns

- COUNTRY

## Query

```sql
SELECT DISTINCT(COUNTRY) FROM PER_ADDRESSES_V WHERE COUNTRY IS NOT NULL ORDER BY COUNTRY
```

---

[← Back to Index](../8_Corporate_Social_Responsibility_Views_Index.md)
