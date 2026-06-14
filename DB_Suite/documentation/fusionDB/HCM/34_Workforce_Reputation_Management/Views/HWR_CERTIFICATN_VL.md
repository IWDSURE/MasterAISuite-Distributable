# HWR_CERTIFICATN_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcertificatnvl-4931.html#hwrcertificatnvl-4931](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcertificatnvl-4931.html#hwrcertificatnvl-4931)

## Columns

- CERTIFICATION_ID
- SOURCE_ID
- NAME
- TITLE
- COUNTRY
- STATE
- ORGANIZATION
- START_DATE
- END_DATE
- CERTIFICATION_LEVEL
- CERTIFICATION_TYPE
- PRFL_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.CERTIFICATION_ID , B.SOURCE_ID , B.NAME , B.TITLE , B.COUNTRY , B.STATE , B.ORGANIZATION , B.START_DATE , B.END_DATE , B.CERTIFICATION_LEVEL , B.CERTIFICATION_TYPE , X.PRFL_ID , B.CREATED_BY , B.CREATION_DATE , B.LAST_UPDATED_BY , B.LAST_UPDATE_DATE , B.LAST_UPDATE_LOGIN FROM HWR_CERTIFICATN_B B LEFT JOIN HWR_CERTIFICATN_PRFL_X X ON (B.CERTIFICATION_ID = X.CERTIFICATION_ID AND B.SOURCE_ID = X.SOURCE_ID)
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
