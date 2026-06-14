# PAY_RELATIONSHIP_TYPES_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrelationshiptypesvl-5136.html#payrelationshiptypesvl-5136](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrelationshiptypesvl-5136.html#payrelationshiptypesvl-5136)

## Columns

- RELATIONSHIP_TYPE_ID
- BASE_REL_TYPE_NAME
- PROCESS_IN_RUN
- LEGISLATION_CODE
- ENTERPRISE_ID
- MODULE_ID
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- LAST_UPDATED_BY
- RELATIONSHIP_TYPE_NAME
- DESCRIPTION

## Query

```sql
SELECT payreltypes.RELATIONSHIP_TYPE_ID RELATIONSHIP_TYPE_ID, payreltypes.BASE_REL_TYPE_NAME BASE_REL_TYPE_NAME, payreltypes.PROCESS_IN_RUN PROCESS_IN_RUN, payreltypes.LEGISLATION_CODE LEGISLATION_CODE, payreltypes.ENTERPRISE_ID ENTERPRISE_ID, payreltypes.MODULE_ID MODULE_ID, payreltypes.OBJECT_VERSION_NUMBER OBJECT_VERSION_NUMBER, payreltypes.CREATED_BY CREATED_BY, payreltypes.CREATION_DATE CREATION_DATE, payreltypes.LAST_UPDATE_DATE LAST_UPDATE_DATE, payreltypes.LAST_UPDATE_LOGIN LAST_UPDATE_LOGIN, payreltypes.LAST_UPDATED_BY LAST_UPDATED_BY, payreltypestl.RELATIONSHIP_TYPE_NAME RELATIONSHIP_TYPE_NAME, payreltypestl.DESCRIPTION DESCRIPTION FROM PAY_RELATIONSHIP_TYPES payreltypes, PAY_RELATIONSHIP_TYPES_TL payreltypestl WHERE payreltypestl.RELATIONSHIP_TYPE_ID = payreltypes.RELATIONSHIP_TYPE_ID AND payreltypestl.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
