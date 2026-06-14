# PAY_REL_PAYMENTS_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrelpaymentsvl-3425.html#payrelpaymentsvl-3425](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrelpaymentsvl-3425.html#payrelpaymentsvl-3425)

## Columns

- PRE_PAYMENT_ID
- PAYROLL_REL_ACTION_ID
- ORG_PAYMENT_METHOD_NAME
- PRIORITY
- PAYMENT_TYPE_NAME
- SOURCE
- CURRENCY_CODE
- AMOUNT
- STATUS
- PREPAY_REL_ACTION_ID
- PREPAY_CUM_REL_ACTION_ID
- PAYROLL_ID
- CALC_BREAKDOWN_ID
- PREPAY_PAYMENT_DATE
- PREPAY_PROCESS_DATE
- PAYMENT_REL_ACTION_ID
- PAYROLL_NAME
- PAYEE_TYPE
- PAYEE
- PAYROLL_RELATIONSHIP_NUMBER
- PERSON_NUMBER
- PAYMENT_REFERENCE
- LEGISLATIVE_DATA_GROUP_ID

## Query

```sql
SELECT ppp.pre_Payment_Id, ppp.PAYROLL_REL_ACTION_ID, opmtl.Org_Payment_Method_Name, ppm.Priority, ppttl.Payment_Type_Name, Lo1.Meaning Source, opm.Currency_Code, ppp.VALUE Amount, Pay_process_flow_utils.Get_payment_status(aac1.PAYROLL_REL_ACTION_ID,ppp.pre_Payment_Id) Status, ppp.payroll_rel_action_id Prepay_rel_action_id, ppp.PAYROLL_REL_ACTION_ID Prepay_cum_rel_action_id, pac1.payroll_id, ppp.calc_breakdown_id, ppp.effective_date prepay_payment_date, pac1.effective_date prepay_process_date, paac1.PAYROLL_REL_ACTION_ID Payment_rel_action_id, ppay.payroll_name, decode(ppp.third_party_payee_id,NULL,'Person','Organization') payee_type, decode(ppp.third_party_payee_id,NULL,peo.full_name,'Organization') payee, ppr.payroll_relationship_number, pnm.person_number, paac1.serial_number payment_reference, ppr.legislative_data_group_id as legislative_data_group_id FROM pay_org_pay_methods_tl opmtl, Pay_Payment_Types_tl ppttl, pay_org_pay_methods_f opm, Pay_pre_Payments ppp, pay_person_pay_methods_f ppm, hcm_LookUps Lo1, Pay_Payment_Types ppt, pay_payroll_rel_actions aac1, Pay_Payroll_Actions Pac1, pay_payroll_rel_actions paac1, pay_all_payrolls_f ppay, pay_pay_relationships_dn ppr, per_person_names_f peo, per_all_people_f pnm WHERE opm.Org_Payment_Method_Id = opmtl.Org_Payment_Method_Id AND opmtl.Language = Userenv('LANG') AND ppt.Payment_Type_Id = ppttl.Payment_Type_Id AND ppttl.Language = Userenv('LANG') AND ppay.payroll_id = pac1.payroll_id AND ppr.payroll_relationship_id = aac1.payroll_relationship_id and ppr.person_id = pnm.person_id (+) and ppr.person_id = peo.person_id (+) AND (peo.person_id is null or pac1.effective_date between peo.effective_start_date and peo.effective_end_date) AND (pnm.person_id is null or pac1.effective_date between pnm.effective_start_date and pnm.effective_end_date) AND pac1.effective_date between ppay.effective_start_date and ppay.effective_end_date AND ppp.PAYROLL_REL_ACTION_ID = aac1.PAYROLL_REL_ACTION_ID AND Pac1.Payroll_Action_Id = aac1.Payroll_Action_Id AND Lo1.LookUp_Type = 'PAY_PAYMENT_SOURCE' AND Lo1.LookUp_Code = DECODE(Pac1.Org_Payment_Method_Id,NULL,DECODE(ppm.Personal_Payment_Method_Id,NULL,'D', 'P'), 'O') AND opm.Org_Payment_Method_Id = ppp.Org_Payment_Method_Id AND Pac1.Effective_Date BETWEEN opm.Effective_Start_Date AND opm.Effective_End_Date AND ppt.Payment_Type_Id = opm.Payment_Type_Id AND ppp.Personal_Payment_Method_Id = ppm.Personal_Payment_Method_Id (+) AND (ppp.Personal_Payment_Method_Id IS NULL OR Pac1.Effective_Date BETWEEN ppm.Effective_Start_Date AND ppm.Effective_End_Date) AND paac1.pre_payment_id (+) = ppp.pre_payment_id AND peo.name_type='GLOBAL' UNION ALL SELECT ppp.pre_Payment_Id, ppp.PAYROLL_REL_ACTION_ID, opmtl.Org_Payment_Method_Name, ppm.Priority, ppttl.Payment_Type_Name, Lo1.Meaning Source, opm.Currency_Code, ppp.VALUE Amount, Pay_process_flow_utils.Get_payment_status(aac1.PAYROLL_REL_ACTION_ID,ppp.pre_Payment_Id) Status, ppp.payroll_rel_action_id Prepay_rel_action_id, aac1.Source_Action_Id Prepay_cum_rel_action_id, pac1.payroll_id, ppp.calc_breakdown_id, ppp.effective_date prepay_payment_date, pac1.effective_date prepay_process_date, paac1.PAYROLL_REL_ACTION_ID Payment_rel_action_id, ppay.payroll_name, decode(ppp.third_party_payee_id,NULL,'Person','Organization') payee_type, decode(ppp.third_party_payee_id,NULL,peo.full_name,'Organization') payee, ppr.payroll_relationship_number, pnm.person_number, paac1.serial_number payment_reference, ppr.legislative_data_group_id as legislative_data_group_id FROM pay_org_pay_methods_tl opmtl, Pay_Payment_Types_tl ppttl, pay_org_pay_methods_f opm, Pay_pre_Payments ppp, pay_person_pay_methods_f ppm, hcm_LookUps Lo1, Pay_Payment_Types ppt, pay_payroll_rel_actions aac1, Pay_Payroll_Actions Pac1, pay_payroll_rel_actions paac1, pay_all_payrolls_f ppay, pay_pay_relationships_dn ppr, per_person_names_f peo, per_all_people_f pnm WHERE opm.Org_Payment_Method_Id = opmtl.Org_Payment_Method_Id AND opmtl.Language = Userenv('LANG') AND ppt.Payment_Type_Id = ppttl.Payment_Type_Id AND ppttl.Language = Userenv('LANG') AND ppay.payroll_id = pac1.payroll_id AND ppr.payroll_relationship_id = aac1.payroll_relationship_id and ppr.person_id = pnm.person_id (+) and ppr.person_id = peo.person_id (+) AND (peo.person_id is null or pac1.effective_date between peo.effective_start_date and peo.effective_end_date) AND (pnm.person_id is null or pac1.effective_date between pnm.effective_start_date and pnm.effective_end_date) AND pac1.effective_date between ppay.effective_start_date and ppay.effective_end_date AND ppp.PAYROLL_REL_ACTION_ID = aac1.PAYROLL_REL_ACTION_ID AND Pac1.Payroll_Action_Id = aac1.Payroll_Action_Id AND Lo1.LookUp_Type = 'PAY_PAYMENT_SOURCE' AND Lo1.LookUp_Code = DECODE(Pac1.Org_Payment_Method_Id,NULL,DECODE(ppm.Personal_Payment_Method_Id,NULL,'D', 'P'), 'O') AND opm.Org_Payment_Method_Id = ppp.Org_Payment_Method_Id AND Pac1.Effective_Date BETWEEN opm.Effective_Start_Date AND opm.Effective_End_Date AND ppt.Payment_Type_Id = opm.Payment_Type_Id AND ppp.Personal_Payment_Method_Id = ppm.Personal_Payment_Method_Id (+) AND (ppp.Personal_Payment_Method_Id IS NULL OR Pac1.Effective_Date BETWEEN ppm.Effective_Start_Date AND ppm.Effective_End_Date) AND aac1.Source_Action_Id IS NOT NULL AND aac1.Source_Action_Id <> aac1.PAYROLL_REL_ACTION_ID AND paac1.pre_payment_id (+) = ppp.pre_payment_id AND peo.name_type='GLOBAL'
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
