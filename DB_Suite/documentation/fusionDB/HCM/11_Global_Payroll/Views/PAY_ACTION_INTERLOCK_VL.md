# PAY_ACTION_INTERLOCK_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactioninterlockvl-6789.html#payactioninterlockvl-6789](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactioninterlockvl-6789.html#payactioninterlockvl-6789)

## Columns

- LOCKING_ACTION_ID
- LOCKING_ACTION_TYPE
- OBJECT_ACTION_ID
- LOCKING_PAYROLL_ACTION_ID

## Query

```sql
select distinct zzz.locking_action_id, zzz.locking_action_type, zzz.Object_action_id, Locking_payroll_Action_Id from (select locking_action_id , i_pact.action_type locking_action_type, ract.payroll_rel_action_id Object_action_id, i_ract.payroll_action_id Locking_payroll_Action_Id from pay_action_interlocks int, pay_payroll_rel_actions ract, pay_payroll_actions pact, pay_payroll_rel_actions i_ract, pay_payroll_actions i_pact where ract.payroll_rel_action_id = int.locked_action_id and pact.payroll_action_id = ract.payroll_action_id and i_ract.payroll_rel_action_id = int.locking_action_id and i_pact.payroll_action_id = i_ract.payroll_action_id and ract.source_action_id is null and exists ( select null from pay_payroll_rel_actions tlsa_ract, pay_payroll_actions tlsa_pact where tlsa_ract.payroll_rel_action_id = int.locking_action_id and tlsa_pact.payroll_action_id = tlsa_ract.payroll_action_id and tlsa_pact.action_type not in ('TV')) ) zzz
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
