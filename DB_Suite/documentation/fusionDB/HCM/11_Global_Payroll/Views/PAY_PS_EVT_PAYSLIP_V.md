# PAY_PS_EVT_PAYSLIP_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypsevtpayslipv-7818.html#paypsevtpayslipv-7818](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypsevtpayslipv-7818.html#paypsevtpayslipv-7818)

## Columns

- PERSON_ID
- ASSIGNMENT_ID
- EVENT_YEAR
- EVENT_DATE
- EVENT_DAYS
- EVENT_TITLE
- EVENT_DETAILS
- LINK_TEXT

## Query

```sql
SELECT ps.person_id person_id, prgn.assignment_id assignment_id, to_char(ps.payment_date, 'YYYY') event_year, ps.payment_date event_date, 0 event_days, '{"strKey":"HdrSPayslip"}' event_title, hrl_df_util.number_to_char((ps.amount)) || ' ' || ps.currency_code event_details, '' link_text FROM pay_payslip_vl ps, pay_rel_groups_dn prgn WHERE ps.payroll_relationship_id = prgn.payroll_relationship_id AND group_type = 'A' AND payslip_view_date <= sysdate AND ps.payment_date <= trunc(sysdate)
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
