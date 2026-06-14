# PAY_PER_ACT_COST_RES_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payperactcostresvl-8742.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payperactcostresvl-8742.html)

## Columns

- OBJECT_ACTION_ID
- STATUS
- DEBIT_OR_CREDIT
- COSTED_VALUE
- CURRENCY_CODE

## Query

```sql
select pra.payroll_rel_action_id OBJECT_action_id,pc.status, pc.DEBIT_OR_CREDIT,sum(pc.COSTED_VALUE) COSTED_VALUE,nvl(pet.output_currency_code, ldg.default_currency_code) currency_code from pay_costs pc, pay_run_results prr, pay_payroll_rel_actions pra, pay_payroll_actions ppa, pay_input_values_f piv, pay_element_types_vl pet, pay_ele_classifications_vl pec, per_legislative_data_groups ldg where ldg.legislative_data_group_id = ppa.legislative_data_group_id and pec.legislation_code = ldg.legislation_code and pec.PARENT_CLASSIFICATION_ID is null and pec.base_classification_id = pet.CLASSIFICATION_ID (+) and pec.costing_debit_or_credit = pc.DEBIT_OR_CREDIT (+) and pc.COSTED_VALUE is not null and pc.run_result_id = prr.run_result_id and pc.payroll_rel_action_id = pra.payroll_rel_action_id and pra.payroll_action_id = ppa.payroll_action_id and pc.input_value_id = piv.input_value_id and pc.secondary_status is null and piv.uom = 'M' and pc.STATUS in ('D', 'S') and pet.element_type_id = prr.element_type_id and ppa.date_earned between pet.effective_start_Date and pet.effective_end_Date and ppa.date_earned between piv.effective_start_Date and piv.effective_end_Date group by pc.status, nvl(pet.output_currency_code, ldg.default_currency_code) ,pra.payroll_rel_action_id,pc.STATUS, pc.DEBIT_OR_CREDIT
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
