# PAY_PAYSLIP_BALANCE_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypayslipbalancevl-8278.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypayslipbalancevl-8278.html)

## Columns

- PAYROLL_ACTION_ID
- PROCESS_DATE
- OBJECT_ACTION_ID
- PREPAY_REL_ACTION_ID
- CONTEXT
- BASE_CATEGORY_NAME
- CATEGORY_NAME
- PRIMARY_BASE_CLASS_NAME
- PRIMARY_CLASS_NAME
- BASE_BALANCE_NAME
- REPORTING_NAME
- AMOUNT

## Query

```sql
select distinct pra.PAYROLL_ACTION_ID,ppa.effective_date Process_Date, pra.payroll_rel_action_id OBJECT_ACTION_ID,val.value_10 PREPAY_REL_ACTION_ID,val.value_8 CONTEXT, val.value_1 BASE_CATEGORY_NAME,val.value_2 CATEGORY_NAME, val.value_3 PRIMARY_BASE_CLASS_NAME, val.value_4 PRIMARY_CLASS_NAME ,val.value_5 BASE_BALANCE_NAME, val.value_6 REPORTING_NAME, (val.value_7) AMOUNT from pay_payroll_actions ppa, pay_payroll_rel_actions pra, table(pay_statistics_utility_pkg.get_payslip_balance_view(pra.payroll_rel_action_id)) val where ppa.PAYROLL_ACTION_ID=pra.PAYROLL_ACTION_ID
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
