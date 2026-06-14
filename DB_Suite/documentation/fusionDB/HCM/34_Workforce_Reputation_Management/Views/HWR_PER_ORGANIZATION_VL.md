# HWR_PER_ORGANIZATION_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrperorganizationvl-7585.html#hwrperorganizationvl-7585](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrperorganizationvl-7585.html#hwrperorganizationvl-7585)

## Columns

- HWR_ORG_ID
- ORG_SIZE
- NAME
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.HWR_ORG_ID, B.ORG_SIZE, T.NAME, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM HWR_PER_ORGANIZATION_B B, HWR_PER_ORGANIZATION_TL T WHERE B.HWR_ORG_ID = T.HWR_ORG_ID AND T.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
