# PAY_PAYROLL_ACTION_LOCKS_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypayrollactionlocksv-5205.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypayrollactionlocksv-5205.html)

## Columns

- PAYROLL_ACTION_ID
- <column 2>

## Query

```sql
select payroll_action_id, decode (pay_action_status.get_action_count(payroll_action_id), 0, 'N', pay_action_status.get_locked_action_count(payroll_action_id), 'Y', 'N' ) from pay_payroll_actions
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
