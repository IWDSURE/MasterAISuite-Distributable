# HWR_SOC_MED_ROLE_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsocmedrolevl-4814.html#hwrsocmedrolevl-4814](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsocmedrolevl-4814.html#hwrsocmedrolevl-4814)

## Columns

- SOC_MED_ROLE_ID
- NAME
- URI
- IS_SEEDED
- IS_ACTIVE
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.SOC_MED_ROLE_ID SOC_MED_ROLE_ID, B.NAME NAME, B.ROLE_URI URI, B.IS_SEEDED IS_SEEDED, B.IS_ACTIVE IS_ACTIVE, B.CREATED_BY CREATED_BY, B.CREATION_DATE CREATION_DATE, B.LAST_UPDATED_BY LAST_UPDATED_BY, B.LAST_UPDATE_DATE LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN LAST_UPDATE_LOGIN FROM HWR_SOC_MED_ROLE_B B
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
