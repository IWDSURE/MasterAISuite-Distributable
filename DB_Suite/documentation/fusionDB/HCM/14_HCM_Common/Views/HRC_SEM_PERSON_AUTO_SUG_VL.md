# HRC_SEM_PERSON_AUTO_SUG_VL

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsempersonautosugvl-8603.html#hrcsempersonautosugvl-8603](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsempersonautosugvl-8603.html#hrcsempersonautosugvl-8603)

## Columns

- LOV
- CREATION_DATE
- LAST_UPDATE_DATE
- OBJECT_VERSION_NUMBER

## Query

```sql
select LOCATION_FQN as LOV, CREATION_DATE, LAST_UPDATE_DATE, OBJECT_VERSION_NUMBER from HRC_SEM_PERSONS where LOCATION_FQN is not null
```

---

[← Back to Index](../14_HCM_Common_Views_Index.md)
