# HWR_EDUCATION_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwreducationvl-3370.html#hwreducationvl-3370](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwreducationvl-3370.html#hwreducationvl-3370)

## Columns

- EDUCATION_ID
- SOURCE_ID
- ACTIVITIES
- DEGREE
- DESCRIPTION
- END_DATE
- FIELD_OF_STUDY
- SCHOOL_INSTITUTION_NAME
- START_DATE
- EDUCATION_TYPE
- PRFL_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.EDUCATION_ID , B.SOURCE_ID , B.ACTIVITIES , B.DEGREE , B.DESCRIPTION , B.END_DATE , B.FIELD_OF_STUDY , B.SCHOOL_INSTITUTION_NAME , B.START_DATE , B.EDUCATION_TYPE , X.PRFL_ID , B.CREATED_BY , B.CREATION_DATE , B.LAST_UPDATED_BY , B.LAST_UPDATE_DATE , B.LAST_UPDATE_LOGIN FROM HWR_EDUCATION_B B LEFT JOIN HWR_EDUCATION_PRFL_X X ON (B.EDUCATION_ID = X.EDUCATION_ID AND B.SOURCE_ID = X.SOURCE_ID)
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
