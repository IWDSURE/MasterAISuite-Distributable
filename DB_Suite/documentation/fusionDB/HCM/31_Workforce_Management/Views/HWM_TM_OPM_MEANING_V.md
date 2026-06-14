# HWM_TM_OPM_MEANING_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmopmmeaningv-8859.html#hwmtmopmmeaningv-8859](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmopmmeaningv-8859.html#hwmtmopmmeaningv-8859)

## Columns

- CODE
- MEANING

## Query

```sql
SELECT to_char(org_payment_method_id) Code, org_payment_method_name Meaning FROM pay_org_pay_methods_vl opm where opm.org_payment_method_id IN( SELECT opm_use.org_payment_method_id FROM pay_org_pay_method_usages_f opm_use, pay_rel_groups_dn asg, pay_assigned_payrolls_dn pap, pay_all_payrolls_f ppp, pay_assigned_payrolls_f papf, pay_pay_relationships_dn ppr /* payroll relationship */ WHERE opm_use.payroll_id = pap.payroll_id and asg.parent_rel_group_id = pap.payroll_term_id and pap.payroll_id = ppp.payroll_id and pap.start_date between ppp.effective_start_date and ppp.effective_end_date and papf.assigned_payroll_id=pap.assigned_payroll_id and asg.PAYROLL_RELATIONSHIP_ID= ppr.PAYROLL_RELATIONSHIP_ID) order by org_payment_method_name
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
