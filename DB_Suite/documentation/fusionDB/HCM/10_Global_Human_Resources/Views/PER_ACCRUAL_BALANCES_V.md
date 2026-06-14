# PER_ACCRUAL_BALANCES_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraccrualbalancesv-5625.html#peraccrualbalancesv-5625](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraccrualbalancesv-5625.html#peraccrualbalancesv-5625)

## Columns

- LEGISLATIVE_DATA_GROUP_ID
- ACCRUAL_PLAN_ID
- ACCRUAL_PLAN_NAME
- ACCRUAL_CATEGORY
- ACCRUAL_UNITS
- ACCRUAL_FORMULA_ID
- CO_FORMULA_ID
- PERSON_ID
- PAYROLL_ASSIGNMENT_ID
- PAYROLL_ID
- HR_ASSIGNMENT_ID
- ASSIGNMENT_NUMBER
- ACCRUAL_ELEMENT_TYPE_ID
- ENROLL_START_DATE
- ENROLL_END_DATE
- CONTINUOUS_SERVICE_DATE
- ACCRUAL_START_DATE
- ACCRUAL_END_DATE
- LAST_ACCRUAL_DATE
- ACCRUAL_RATE
- CEILING
- MAX_CARRY_OVER
- ACCRUED_AMT
- ENTITLED_AMT
- ABSENCE_AMT
- CARRY_OVER_AMT
- OTHERS_AMT
- NET_ENTITLED_AMT
- LIABILITY_VALUE
- CURRENCY_CODE

## Query

```sql
SELECT pap.legislative_data_group_id, pap.accrual_plan_id, pap.accrual_plan_name, act.meaning accrual_category , aut.meaning accrual_units , pap.accrual_formula_id , pap.co_formula_id, paf.person_id, ppa.payroll_assignment_id, papd.payroll_id, paf.assignment_id hr_assignment_id, paf.assignment_number, pap.accrual_element_type_id, bal.enroll_start_date, bal.enroll_end_date, bal.continuous_service_date, bal.accrual_start_date, bal.accrual_end_date, bal.last_accrual_date, bal.accrual_rate, bal.ceiling , bal.max_carry_over, bal.accrued_amt , bal.entitled_amt , bal.absence_amt , bal.carry_over_amt , bal.others_amt , bal.net_entitled_amt , bal.liability_value , bal.currency_code FROM per_accrual_plans_vl pap ,hr_lookups act ,hr_lookups aut ,per_all_assignments_f paf ,pay_payroll_assignments ppa , pay_assigned_payrolls_dn papd ,pay_element_entries_f pee ,pay_entry_usages peu ,TABLE(per_accrual_bal_functions.get_accrual_balance(ppa.payroll_assignment_id,pap.accrual_plan_id,sysdate)) bal WHERE 1=1 AND trunc(SYSDATE) BETWEEN paf.effective_start_date AND paf.effective_end_date AND ppa.hr_assignment_id = paf.assignment_id AND trunc(SYSDATE) BETWEEN ppa.start_date AND ppa.end_date AND pee.element_type_id = pap.accrual_element_type_id AND trunc(SYSDATE) BETWEEN pee.effective_start_date AND pee.effective_end_date AND peu.element_entry_id = pee.element_entry_id AND peu.usage_level = 'PA' AND peu.payroll_assignment_id = ppa.payroll_assignment_id AND trunc(SYSDATE) BETWEEN peu.date_from AND peu.date_to AND pap.accrual_plan_id = bal.accrual_plan_id AND act.lookup_type='PER_ACCRUAL_CATEGORY' AND act.lookup_code= pap.accrual_category AND aut.lookup_type='HOURS_OR_DAYS' and aut.lookup_code= pap.accrual_units AND papd.payroll_term_id(+) = ppa.payroll_term_id
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
