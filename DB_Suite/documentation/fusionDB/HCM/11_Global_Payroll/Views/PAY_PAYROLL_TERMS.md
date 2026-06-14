# PAY_PAYROLL_TERMS

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypayrollterms-6966.html#paypayrollterms-6966](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypayrollterms-6966.html#paypayrollterms-6966)

## Columns

- PAYROLL_TERM_ID
- START_DATE
- END_DATE
- PAYROLL_RELATIONSHIP_ID
- HR_TERM_ID
- LEGAL_EMPLOYER_ID

## Query

```sql
SELECT PR.RELATIONSHIP_GROUP_ID PAYROLL_TERM_ID, PR.START_DATE, PR.END_DATE, PR.PAYROLL_RELATIONSHIP_ID, PR.TERM_ID HR_TERM_ID, PR.LEGAL_EMPLOYER_ID FROM PAY_REL_GROUPS_DN PR WHERE PR.GROUP_TYPE = 'T'
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
