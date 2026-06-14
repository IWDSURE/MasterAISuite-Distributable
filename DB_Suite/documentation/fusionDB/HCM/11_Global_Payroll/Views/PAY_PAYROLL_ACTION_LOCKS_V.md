# PAY_PAYROLL_ACTION_LOCKS_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypayrollactionlocksv-5219.html#paypayrollactionlocksv-5219](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypayrollactionlocksv-5219.html#paypayrollactionlocksv-5219)

## Columns

- PAYROLL_ACTION_ID
- <column 2>

## Query

```sql
select payroll_action_id, decode (pay_action_status.get_action_count(payroll_action_id), 0, 'N', pay_action_status.get_locked_action_count(payroll_action_id), 'Y', 'N' ) from pay_payroll_actions
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
