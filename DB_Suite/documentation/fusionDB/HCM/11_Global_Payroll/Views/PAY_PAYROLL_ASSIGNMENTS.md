# PAY_PAYROLL_ASSIGNMENTS

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypayrollassignments-4401.html#paypayrollassignments-4401](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypayrollassignments-4401.html#paypayrollassignments-4401)

## Columns

- PAYROLL_ASSIGNMENT_ID
- START_DATE
- END_DATE
- PAYROLL_RELATIONSHIP_ID
- PAYROLL_TERM_ID
- HR_TERM_ID
- HR_ASSIGNMENT_ID
- LEGAL_EMPLOYER_ID
- PERSON_ID

## Query

```sql
SELECT RG.RELATIONSHIP_GROUP_ID PAYROLL_ASSIGNMENT_ID, RG.START_DATE, RG.END_DATE, RG.PAYROLL_RELATIONSHIP_ID, RG.PARENT_REL_GROUP_ID PAYROLL_TERM_ID, RG.TERM_ID HR_TERM_ID, RG.ASSIGNMENT_ID HR_ASSIGNMENT_ID, RG.LEGAL_EMPLOYER_ID, PR.PERSON_ID FROM PAY_REL_GROUPS_DN RG, PAY_PAY_RELATIONSHIPS_DN PR WHERE RG.GROUP_TYPE = 'A' AND RG.PAYROLL_RELATIONSHIP_ID = PR.PAYROLL_RELATIONSHIP_ID
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
