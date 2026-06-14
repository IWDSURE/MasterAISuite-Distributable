# PAY_PER_PAYMENT_ANA_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payperpaymentanavl-6176.html#payperpaymentanavl-6176](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payperpaymentanavl-6176.html#payperpaymentanavl-6176)

## Columns

- ACTION_TYPE
- OBJECT_ACTION_ID
- PAYMENT_STATUS_CODE
- PAYMENT_STATUS
- AMOUNT
- CURRENCY_CODE
- ORG_PAYMENT_METHOD_NAME

## Query

```sql
select payRes.ACTION_TYPE, payRes.OBJECT_ACTION_ID, payRes.payment_status_code, (select meaning from HCM_LOOKUPS LK where LK.LOOKUP_TYPE= 'PAY_STATUS' and LK.LOOKUP_CODE =payRes.payment_status_code) payment_status, payRes.Amount, payRes.CURRENCY_CODE, payRes.ORG_PAYMENT_METHOD_NAME from ( select pay.ACTION_TYPE,pay.OBJECT_ACTION_ID, (case when pay.payment_status_code= 'V' then decode((select max(PAYMENT_REASON) from PAY_PAYROLL_REL_ACTIONS emp, pay_payroll_actions eppa where emp.pre_payment_id=pay.pre_payment_id and eppa.PAYROLL_ACTION_ID=emp.PAYROLL_ACTION_ID and eppa.action_type='E' and exists(select max(1) from pay_action_interlocks lk where lk.locked_action_id=pay.PREPAY_REL_ACTION_ID)),'ORA_EXTERNAL_PAYMENT','MR','ORA_PREVENT_PAYMENT','C',pay.payment_status_code) else pay.payment_status_code end) payment_status_code, pay.Amount, pay.CURRENCY_CODE, pay.ORG_PAYMENT_METHOD_NAME from ( select PPAC1.ACTION_TYPE,PYAAC1.PAYROLL_REL_ACTION_ID OBJECT_ACTION_ID,PPP.pre_payment_id,PPP.PAYROLL_REL_ACTION_ID PREPAY_REL_ACTION_ID, (PPP.BASE_CURRENCY_VALUE) Amount, hr_pre_pay.payment_status(PYAAC1.PAYROLL_REL_ACTION_ID,PPAC1.action_type) payment_status_code, (case when PPP.ORG_PAYMENT_METHOD_ID is not null then (select max(OPM.CURRENCY_CODE) from PAY_ORG_PAY_METHODS_F OPM where OPM.ORG_PAYMENT_METHOD_ID = PPP.ORG_PAYMENT_METHOD_ID) else (select max(ldg.DEFAULT_CURRENCY_CODE) from PER_LEGISLATIVE_DATA_GROUPS ldg where ldg.legislative_data_group_id = PPAC1.legislative_data_group_id) end) CURRENCY_CODE, opm.ORG_PAYMENT_METHOD_NAME from PAY_PRE_PAYMENTS PPP, PAY_PAYROLL_ACTIONS PPAC1, PAY_PAYROLL_REL_ACTIONS PYAAC1, pay_org_pay_methods_vl opm where PYAAC1.PAYROLL_ACTION_ID= PPAC1.PAYROLL_ACTION_ID and PYAAC1.pre_payment_id=PPP.pre_payment_id and PPP.THIRD_PARTY_PAYEE_ID is null and opm.ORG_PAYMENT_METHOD_ID=ppp.ORG_PAYMENT_METHOD_ID and PPAC1.effective_date between EFFECTIVE_START_DATE and EFFECTIVE_END_DATE and not exists(select 1 from PAY_PAYROLL_ACTIONS EPAC1, PAY_PAYROLL_REL_ACTIONS EYAAC1 where EYAAC1.PAYROLL_ACTION_ID= EPAC1.PAYROLL_ACTION_ID and EPAC1.action_type='E' and PYAAC1.PAYROLL_REL_ACTION_ID= EYAAC1.PAYROLL_REL_ACTION_ID) )pay) payRes
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
