# PAY_RATES_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payratesv-8219.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payratesv-8219.html)

## Columns

- RATE_ID
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- RATE_DEFINITION_ID
- PAYROLL_RELATIONSHIP_ID
- PAYROLL_TERM_ID
- PAYROLL_ASSIGNMENT_ID
- NAME
- BASE_NAME
- SHORT_NAME
- LEGISLATIVE_DATA_GROUP_ID
- LEGISLATION_CODE
- ASSIGNMENT_ID
- TERM_ID
- MIN_VALUE
- MAX_VALUE
- BASE_SALARY_FLAG
- ELEMENT_TYPE_ID
- DIR_CARD_COMP_DEF_ID
- FTE_FLAG
- OVERALL_SALARY_FLAG
- AMOUNT_ENTERABLE
- FACTOR_ENTERABLE
- RATETYPE
- RETURN_PRECISION

## Query

```sql
select distinct pee.element_entry_id rate_id, pee.effective_start_date, pee.effective_end_date, prd.rate_definition_id, peu.payroll_relationship_id, peu.payroll_term_id, peu.payroll_assignment_id, prd.name, prd.base_name, prd.short_name, prd.legislative_data_group_id, prd.legislation_code, prg_asg.assignment_id, prg_term.term_id, to_number(decode(prd.MIN_TYPE,null,null, prd.MIN_VALUE)) min_value, to_number(decode(prd.max_type,null,null, prd.max_value)) max_value, nvl(prd.BASE_SALARY_FLAG, 'N') Base_salary_flag, prd.ELEMENT_TYPE_ID, prd.DIR_CARD_COMP_DEF_ID, decode (prd.type, 'RBC', 'Y', nvl(prd.FTE_FLAG, 'N')) fte_flag, nvl(prd.OVERALL_SALARY_FLAG, 'N') overall_salary_flag, nvl(prd.AMOUNT_ENTERABLE, 'N') amount_enterable, nvl(prd.FACTOR_ENTERABLE, 'N') factor_enterable, prd.type ratetype, decode(prd.type,'RBC',2,prd.RETURN_PRECISION) RETURN_PRECISION from pay_element_entries_f pee, pay_element_types_f pet, pay_entry_usages peu, pay_rate_definitions_f_vl prd, pay_rel_groups_dn prg_term, pay_rel_groups_dn prg_asg where pee.element_entry_id = peu.element_entry_id and prd.element_type_id = pet.element_type_id and pee.element_type_id = pet.element_type_id and prd.element_type_id is not null and prg_term.group_type (+) = 'T' and pee.effective_start_date between prd.effective_start_date and prd.effective_end_date and peu.payroll_term_id = prg_term.relationship_group_id (+) and prg_asg.group_type (+) = 'A' and peu.payroll_assignment_id = prg_asg.relationship_group_id (+) union all select pdcc.dir_card_comp_id rate_id, pdcc.effective_start_date, pdcc.effective_end_date, prd.rate_definition_id, nvl(prg_term.payroll_relationship_id, pdc.payroll_relationship_id), decode(prg_term.group_type, 'T', prg_term.relationship_group_id, prg_term.parent_rel_group_id), decode(prg_term.group_type, 'A', prg_term.relationship_group_id, null), prd.name, prd.base_name, prd.short_name, prd.legislative_data_group_id, prd.legislation_code, decode (prg_term.group_type, 'A', prg_term.assignment_id, null), decode (prg_term.group_type, 'T', prg_term.term_id, (select prg.term_id from pay_rel_groups_dn prg where prg.relationship_group_id = prg_term.parent_rel_group_id) ), to_number(decode(prd.MIN_TYPE,null,null, prd.MIN_VALUE)) min_value, to_number(decode(prd.max_type,null,null, prd.max_value)) max_value, nvl(prd.BASE_SALARY_FLAG, 'N') Base_salary_flag, prd.ELEMENT_TYPE_ID, prd.DIR_CARD_COMP_DEF_ID, decode (prd.type, 'RBC', 'Y', nvl(prd.FTE_FLAG, 'N')) fte_flag, nvl(prd.OVERALL_SALARY_FLAG, 'N') overall_salary_flag, nvl(prd.AMOUNT_ENTERABLE, 'N') amount_enterable, nvl(prd.FACTOR_ENTERABLE, 'N') factor_enterable, prd.type ratetype, decode(prd.type,'RBC',2,prd.RETURN_PRECISION) RETURN_PRECISION from pay_dir_card_components_f pdcc, pay_dir_card_comp_defs_f pdccd, pay_dir_rep_card_usages_f pdrcu, pay_rate_definitions_f_vl prd, pay_rel_groups_dn prg_term, pay_dir_cards_f pdc where pdcc.dir_card_id = pdc.dir_card_id and pdcc.dir_card_comp_id = pdrcu.dir_card_comp_id (+) and prd.dir_card_comp_def_id = pdccd.dir_card_comp_def_id and pdcc.dir_card_comp_def_id = pdccd.dir_card_comp_def_id and prd.dir_card_comp_def_id is not null and pdcc.effective_start_date between prd.effective_start_date and prd.effective_end_date and pdrcu.relationship_group_id = prg_term.relationship_group_id (+) and pdc.payroll_relationship_id = prg_term.payroll_relationship_id (+) union all select decode(ppa.dimension_level, 'REL', ppa.payroll_relationship_id, 'TRM', ppa.payroll_term_id, 'ASG', ppa.payroll_assignment_id) rate_id, greatest(prd.effective_start_date, ppa.start_date) effective_start_date, least(prd.effective_end_date, ppa.end_date) effective_end_date, prd.rate_definition_id, ppa.payroll_relationship_id, ppa.payroll_term_id, ppa.payroll_assignment_id, prd.name, prd.base_name, prd.short_name, prd.legislative_data_group_id, prd.legislation_code, prg_asg.assignment_id assignment_id, prg_term.term_id, to_number(decode(prd.MIN_TYPE,null,null, prd.MIN_VALUE)) min_value, to_number(decode(prd.max_type,null,null, prd.max_value)) max_value, nvl(prd.BASE_SALARY_FLAG, 'N') Base_salary_flag, prd.ELEMENT_TYPE_ID, prd.DIR_CARD_COMP_DEF_ID, decode(prd.type, 'RBC', 'Y', nvl(prd.FTE_FLAG, 'N')) fte_flag, nvl(prd.OVERALL_SALARY_FLAG, 'N') overall_salary_flag, nvl(prd.AMOUNT_ENTERABLE, 'N') amount_enterable, nvl(prd.FACTOR_ENTERABLE, 'N') factor_enterable, prd.type ratetype, decode(prd.type,'RBC',2,prd.RETURN_PRECISION) RETURN_PRECISION from pay_rate_definitions_f_vl prd, pay_balance_dimensions pbd, (select distinct 'REL' dimension_level, payroll_relationship_id, null payroll_term_id, null payroll_assignment_id, null term_id, null assignment_id, start_date, end_date from pay_payroll_assignments union all select distinct 'TRM', payroll_relationship_id, payroll_term_id payroll_term_id, null payroll_assignment_id, hr_term_id term_id, null assignment_id, start_date, end_date from pay_payroll_assignments union all select distinct 'ASG', payroll_relationship_id, payroll_term_id payroll_term_id, payroll_assignment_id payroll_assignment_id, hr_term_id term_id, hr_assignment_id assignment_id, start_date, end_date from pay_payroll_assignments ) ppa, pay_rel_groups_dn prg_term, pay_rel_groups_dn prg_asg where prd.default_bal_dimension_id = pbd.balance_dimension_id and ppa.dimension_level = pbd.dimension_level and prd.type in ('RBC', 'DRT', 'FORMULA', 'GRADE' ) and prd.element_type_id is null and greatest(prd.effective_start_date, ppa.start_date) <= least(prd.effective_end_date, ppa.end_date) and prg_term.group_type (+) = 'T' and ppa.payroll_term_id = prg_term.relationship_group_id (+) and prg_asg.group_type (+) = 'A' and ppa.payroll_relationship_id = prg_asg.payroll_relationship_id (+) and ppa.payroll_assignment_id = prg_asg.relationship_group_id (+) and ppa.payroll_assignment_id = prg_asg.relationship_group_id (+)
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
