# HRC_SEM_LOCATION_AUTO_SUG_VL

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemlocationautosugvl-7476.html#hrcsemlocationautosugvl-7476](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemlocationautosugvl-7476.html#hrcsemlocationautosugvl-7476)

## Columns

- LOV
- CREATION_DATE
- LAST_UPDATE_DATE
- OBJECT_VERSION_NUMBER

## Query

```sql
select FQN as LOV, CREATION_DATE, LAST_UPDATE_DATE, OBJECT_VERSION_NUMBER from HRC_SEM_LOCATIONS where FQN is not null
```

---

[← Back to Index](../14_HCM_Common_Views_Index.md)
