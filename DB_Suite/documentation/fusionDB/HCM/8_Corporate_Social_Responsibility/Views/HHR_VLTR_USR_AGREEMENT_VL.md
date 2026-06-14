# HHR_VLTR_USR_AGREEMENT_VL

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrusragreementvl-3934.html#hhrvltrusragreementvl-3934](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrusragreementvl-3934.html#hhrvltrusragreementvl-3934)

## Columns

- ID
- AGREEMENT_TYPE
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- USER_AGREEMENT
- WAIVER_TITLE

## Query

```sql
SELECT A.ID ID, A.AGREEMENT_TYPE AGREEMENT_TYPE, A.CREATED_BY CREATED_BY, A.CREATION_DATE CREATION_DATE, A.LAST_UPDATED_BY LAST_UPDATED_BY, A.LAST_UPDATE_DATE LAST_UPDATE_DATE, A.LAST_UPDATE_LOGIN LAST_UPDATE_LOGIN, B.USER_AGREEMENT USER_AGREEMENT, B.WAIVER_TITLE WAIVER_TITLE FROM HHR_VLTR_USR_AGREEMENT_B A, HHR_VLTR_USR_AGREEMENT_TL B WHERE A.ID = B.ID AND B.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../8_Corporate_Social_Responsibility_Views_Index.md)
