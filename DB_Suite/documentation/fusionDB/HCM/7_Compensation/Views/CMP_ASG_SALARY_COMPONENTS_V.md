# CMP_ASG_SALARY_COMPONENTS_V

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpasgsalarycomponentsv-5297.html#cmpasgsalarycomponentsv-5297](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpasgsalarycomponentsv-5297.html#cmpasgsalarycomponentsv-5297)

## Columns

- SALARY_ID
- SALARY_COMPONENT_ID
- SALARY_BASIS_ID
- CURRENCY_CODE
- SALARY_BASIS_NAME
- ASSIGNMENT_ID
- DATE_FROM
- DATE_TO
- DISPLAY_SEQUENCE
- COMPONENT_REASON_CODE
- COMPONENT_NAME
- COMPONENT_AMOUNT
- COMPONENT_PERCENTAGE

## Query

```sql
select csc.salary_id, csc.salary_component_id, csa.salary_basis_id, csa.currency_code, csb.name "SALARY_BASIS_NAME", csa.assignment_id, csa.date_from, csa.date_to, hlk.display_sequence, csc.component_reason_code, hlk.meaning as component_name, csc.change_amount as component_amount, csc.change_percentage as component_percentage from cmp_salary_components csc, cmp_salary csa, hcm_lookups hlk, cmp_salary_bases csb where csc.salary_id = csa.salary_id and hlk.lookup_type ='CMP_SALARY_COMPONENTS' and csa.salary_basis_id = csb.salary_basis_id and hlk.lookup_code = csc.component_reason_code
```

---

[← Back to Index](../7_Compensation_Views_Index.md)
