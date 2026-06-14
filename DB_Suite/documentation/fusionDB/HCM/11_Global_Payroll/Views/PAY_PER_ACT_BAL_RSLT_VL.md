# PAY_PER_ACT_BAL_RSLT_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payperactbalrsltvl-8060.html#payperactbalrsltvl-8060](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payperactbalrsltvl-8060.html#payperactbalrsltvl-8060)

## Columns

- OBJECT_ACTION_ID
- BASE_BALANCE_NAME
- BALANCE_NAME
- CURRENCY_CODE
- BALANCE_TYPE_ID
- BALANCE_VALUE

## Query

```sql
select Object_action_id,base_balance_name,balance_name, currency_code,balance_type_id,BALANCE_VALUE from( select pra.source_action_id Object_action_id, pbt.base_balance_name, pbt.balance_name, pbt.currency_code, rsi.sequence_num, pbt.balance_type_id, sum(balv.BALANCE_VALUE) BALANCE_VALUE from pay_bal_grp_usages_vl bgu1, per_legislative_data_groups ldg, PAY_REPORT_SORT_ITEMS rsi, pay_balance_groups pbg, pay_bal_grp_inclusions pbgi, pay_bal_att_definitions pbad, pay_balance_attributes pba, pay_defined_balances pdb, pay_balance_types_vl pbt, pay_balance_dimensions pbd, pay_payroll_actions ppa, pay_payroll_rel_actions pra, pay_run_balances balv where bgu1.base_group_usage_name = 'ORA_PAYROLL_ACTIVITY_BALANCE_GROUP_USAGE' and ppa.legislative_data_group_id=ldg.legislative_data_group_id and pbg.balance_group_id = bgu1.balance_group_id and bgu1.report_sort_type_id = rsi.report_sort_type_id and rsi.source_id = pbt.balance_type_id and ((rsi.legislation_code is null and rsi.legislative_data_group_id is null) or rsi.legislation_code = ldg.legislation_code or rsi.legislative_data_group_id = ldg.legislative_data_group_id) and ((pbg.legislation_code is null and pbg.legislative_data_group_id is null) or (pbg.legislation_code = ldg.legislation_code and pbg.legislative_data_group_id is null) or pbg.legislative_data_group_id = ldg.legislative_data_group_id) and pbg.balance_group_id = pbgi.balance_group_id and ((pbgi.legislation_code is null and pbgi.legislative_data_group_id is null) or (pbgi.legislation_code = ldg.legislation_code and pbgi.legislative_data_group_id is null) or pbgi.legislative_data_group_id = ldg.legislative_data_group_id) and pbgi.attribute_id = pbad.attribute_id and ((pbad.legislation_code is null and pbad.legislative_data_group_id is null) or (pbad.legislation_code = ldg.legislation_code and pbad.legislative_data_group_id is null) or pbad.legislative_data_group_id = ldg.legislative_data_group_id) and pbad.attribute_id = pba.attribute_id and ((pba.legislation_code is null and pba.legislative_data_group_id is null) or (pba.legislation_code = ldg.legislation_code and pba.legislative_data_group_id is null) or pba.legislative_data_group_id = ldg.legislative_data_group_id) and pdb.defined_balance_id = pba.defined_balance_id and ((pdb.legislation_code is null and pdb.legislative_data_group_id is null) or (pdb.legislation_code = ldg.legislation_code and pdb.legislative_data_group_id is null) or pdb.legislative_data_group_id = ldg.legislative_data_group_id) and pdb.balance_type_id = pbt.balance_type_id and ((pbt.legislation_code is null and pbt.legislative_data_group_id is null) or (pbt.legislation_code = ldg.legislation_code and pbt.legislative_data_group_id is null) or pbt.legislative_data_group_id = ldg.legislative_data_group_id) and pbd.balance_dimension_id = pdb.balance_dimension_id and ((pbd.legislation_code is null and pbd.legislative_data_group_id is null) or (pbd.legislation_code = ldg.legislation_code and pbd.legislative_data_group_id is null) or pbd.legislative_data_group_id = ldg.legislative_data_group_id) and pbd.period_type ='RUN' and pbd.DIMENSION_LEVEL ='REL' and ppa.action_type IN ('R','Q','B','V') and pra.payroll_action_id = ppa.payroll_action_id AND pra.source_action_id IS NOT NULL AND pra.action_status in('M','C') and balv.defined_balance_id (+) = pdb.defined_balance_id and balv.payroll_rel_action_id (+) = pra.payroll_rel_action_id and ppa.effective_date = balv.effective_Date (+) and balv.BALANCE_VALUE is not null group by pra.source_action_id, pbt.base_balance_name, pbt.balance_name, pbt.currency_code, rsi.sequence_num, pbt.balance_type_id)
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
