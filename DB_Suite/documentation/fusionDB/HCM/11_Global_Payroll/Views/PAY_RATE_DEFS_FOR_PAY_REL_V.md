# PAY_RATE_DEFS_FOR_PAY_REL_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payratedefsforpayrelv-7771.html#payratedefsforpayrelv-7771](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payratedefsforpayrelv-7771.html#payratedefsforpayrelv-7771)

## Columns

- PAYROLL_RELATIONSHIP_ID
- RATE_DEFINITION_ID
- START_DATE
- END_DATE
- NAME
- PAYROLL_TERM_ID
- PAYROLL_ASSIGNMENT_ID
- CREATOR_TYPE
- CREATOR_ID

## Query

```sql
select payroll_relationship_id, rate_definition_id, start_date, end_date, (select distinct prd.base_name from pay_rate_definitions_f prd where prd.rate_definition_id = B.rate_definition_id) name, payroll_term_id, payroll_assignment_id, creator_type, creator_id from ( select distinct peu.payroll_relationship_id, to_number(pri.value1) rate_definition_id, peu.date_from start_date, peu.date_to end_date, peu.payroll_term_id, peu.payroll_assignment_id, A.creator_type, A.creator_id from (select pee.element_entry_id, et.indirect_et_id, pee.creator_type, pee.creator_id from pay_element_entries_f pee, pay_rate_element_indirects et where pee.element_type_id = et.base_et_id union select pee.element_entry_id, pee.element_type_id, pee.creator_type, pee.creator_id from pay_element_entries_f pee ) A, pay_entry_usages peu, pay_calculation_units_f pcu, pay_value_defs_v pvd, pay_calc_types pct, pay_range_defs_v pri where A.element_entry_id = peu.element_entry_id and pcu.element_type_id = A.indirect_et_id and pcu.value_defn_id = pvd.value_defn_id and pvd.calc_type_id = pct.calc_type_id and pct.type = 'RD' and pri.value_defn_id = pvd.value_defn_id and pri.value1 != '-1' union select pdc.payroll_relationship_id, to_number(pri.value1), pvi.effective_start_date, pvi.effective_end_date, nvl(rg.PARENT_REL_GROUP_ID, rg.RELATIONSHIP_GROUP_ID) payroll_term_id, decode(rg.group_type, 'A', rg.RELATIONSHIP_GROUP_ID, null) payroll_assignment_id, null, null from PAY_VALUE_INSTANCES_V pvi, pay_range_inst_v pri, pay_calc_types pct, pay_dir_card_components_f pdcc, pay_dir_cards_f pdc, pay_dir_override_usages_f dou, pay_allow_overrides_f pao, pay_rel_groups_dn rg where pvi.value_defn_id = pri.value_defn_id and dou.DIR_OVERRIDE_USAGE_ID = pvi.DIR_OVERRIDE_USAGE_ID and pdcc.dir_card_comp_id = pvi.source_id and pdcc.dir_card_id = pdc.dir_card_id and nvl(pri.calc_type_id, pvi.calc_type_id) = pct.calc_type_id and pct.type = 'RD' and dou.ALLOW_OVERRIDES_ID = pao.ALLOW_OVERRIDES_ID and pao.type = 'RD' and pao.value_defn_id = pvi.parent_value_defn_id and pri.value1 != '-1' and pdc.payroll_relationship_id = rg.payroll_relationship_id and pay_payroll_run.is_REL_GROUP_LINKED_TO_COMP(pdcc.dir_card_comp_id, rg.relationship_group_id) = 'Y' union select distinct peu.payroll_relationship_id, prd.rate_definition_id, peu.date_from start_date, peu.date_to end_date, peu.payroll_term_id, peu.payroll_assignment_id, pee.creator_type, pee.creator_id from pay_rate_definitions_f prd, pay_element_entries_f pee, pay_entry_usages peu where prd.element_type_id = pee.element_type_id and peu.element_entry_id = pee.element_entry_id ) B
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
