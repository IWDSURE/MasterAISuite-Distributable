# PAY_PS_ANA_LATEST_PAYSLIP_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypsanalatestpayslipv-3018.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypsanalatestpayslipv-3018.html)

## Columns

- PERSON_ID
- ASSIGNMENT_ID
- TEXT_TITLE
- TEXT_METRIC
- TEXT_META
- BADGE_TEXT
- BADGE_STATUS
- PERIOD_CHN_IND_VAL
- PERIOD_CHN_IND_CMP
- CHART_TYPE
- CHART_COLOR
- CHART_DATA
- LINK_TEXT

## Query

```sql
SELECT asg.person_id person_id, asg.assignment_id assignment_id, '{"strKey":"HdrSPayslip"}' text_title, '{"strKey":"PgHINetpayNETPAYCURRENCYCODE", "tokens":{"NET_PAY":"'|| hrl_df_util.number_to_char(ps.amount)|| '","CURRENCY_CODE":"'|| ps.currency_code|| '"}}' text_metric, '{"strKey":"PgHIPaidonDATE", "tokens":{"DATE":"'|| hrl_df_util.date_to_char(ps.payment_date)|| '"}}' text_meta, decode(sign((sysdate -(ps.payment_date)) - 7), - 1, '{"strKey":"BdgNew3"}', NULL) badge_text, decode(sign((sysdate -(ps.payment_date)) - 7), - 1, 'info', NULL) badge_status, NULL period_chn_ind_val, NULL period_chn_ind_cmp, NULL chart_type, NULL chart_color, NULL chart_data, '?pPersonId=' || asg.person_id link_text FROM per_all_assignments_f asg, pay_rel_groups_dn prgn, pay_payslip_vl ps WHERE asg.person_id = ps.person_id and asg.assignment_id = prgn.assignment_id and trunc(sysdate) between effective_start_date and effective_end_date and ps.payroll_relationship_id = prgn.payroll_relationship_id AND group_type = 'A' AND payslip_view_date <= sysdate AND payslip_view_date = ( SELECT MAX(payslip_view_date) FROM pay_payslip_vl x WHERE x.person_id = asg.person_id AND payslip_view_date <= trunc(sysdate) )
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
