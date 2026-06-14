# PAY_ASS_STATUS_TYPES_STD_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payassstatustypesstdv-7356.html#payassstatustypesstdv-7356](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payassstatustypesstdv-7356.html#payassstatustypesstdv-7356)

## Columns

- USER_STATUS
- ASSIGNMENT_STATUS_TYPE_ID
- BUSINESS_GROUP_ID
- LEGISLATION_CODE
- LOOKUP_CODE

## Query

```sql
SELECT PASTL.USER_STATUS , PAS.ASSIGNMENT_STATUS_TYPE_ID , PAS.BUSINESS_GROUP_ID , PAS.LEGISLATION_CODE , to_char(NULL) lookup_code FROM PER_ASSIGNMENT_STATUS_TYPES_TL PASTL, PER_ASSIGNMENT_STATUS_TYPES PAS WHERE PAS.ASSIGNMENT_STATUS_TYPE_ID = PASTL.ASSIGNMENT_STATUS_TYPE_ID AND PASTL.LANGUAGE = USERENV('LANG') UNION SELECT HRL.MEANING , fnd_number.canonical_to_number(NULL) , fnd_number.canonical_to_number(NULL) , TO_CHAR(NULL),hrl.lookup_code FROM HR_LOOKUPS HRL WHERE HRL.APPLICATION_ID IN (800, 801) AND HRL.LOOKUP_TYPE = 'NAME_TRANSLATIONS' AND HRL.LOOKUP_CODE in ( 'STANDARD' ,'BAL_ADJUST')
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
