# PAY_BALANCE_GTN_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalancegtnvl-5785.html#paybalancegtnvl-5785](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalancegtnvl-5785.html#paybalancegtnvl-5785)

## Columns

- BALANCE_NAME
- BALANCE_VALUE
- EFFECTIVE_DATE
- BASE_GROUP_USAGE_NAME
- SOURCE_ACTION_ID
- END_DATE

## Query

```sql
SELECT pbt.balance_name AS balance_name , balv.balance_value1 AS balance_value , ppa.effective_date , pbg.base_group_usage_name , pra.source_action_id , ptp_past.end_date FROM fusion.pay_bal_grp_usages pbg , fusion.pay_payroll_rel_actions pra , fusion.pay_payroll_rel_actions pra_target , fusion.pay_payroll_actions ppa , fusion.pay_payroll_actions ppa_current , fusion.pay_time_periods ptp_past , fusion.pay_time_periods ptp_current , TABLE(fusion.pay_balance_utility.get_bal_grp_values_matrix (pra_target.payroll_rel_action_id ,NULL ,NULL ,pbg.bal_grp_usage_id , ppa.effective_date )) balv , fusion.pay_defined_balances pdb , fusion.pay_balance_types_vl pbt WHERE balv.defined_balance_id1 = pdb.defined_balance_id AND ppa_current.payroll_action_id = pra.payroll_action_id AND ppa_current.dedn_time_period_id = ptp_current.time_period_id AND ptp_past.period_category='S' AND pdb.balance_type_id = pbt.balance_type_id AND pra.payroll_relationship_id = pra_target.payroll_relationship_id AND ppa.payroll_action_id = pra_target.payroll_action_id AND ppa.action_type IN ('R','Q','B') AND ppa.payroll_id = ptp_past.payroll_id AND pra_target.source_action_id IS NOT NULL AND ppa.effective_date BETWEEN ptp_past.start_date AND ptp_past.end_date AND pra_target.action_status = 'C' AND ptp_past.end_date BETWEEN (ptp_current.end_date-(ptp_current.end_date-ptp_current.start_date)*6) AND ptp_current.end_date AND balv.context_rec.payroll_term_id is null and balv.context_rec.payroll_assignment_id is null
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
