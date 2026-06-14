# ANC_ACCRUAL_BALANCES_V

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancaccrualbalancesv-7986.html#ancaccrualbalancesv-7986](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancaccrualbalancesv-7986.html#ancaccrualbalancesv-7986)

## Columns

- ABSENCE_TYPE
- PLAN_NAME
- PER_ACCRUAL_ENTRY_ID
- ACCRUAL_PERIOD
- WORK_TERM_ASG_ID
- PERIOD_OF_SERVICE_ID
- PLAN_ID
- BEGINING_BALANCE
- ACCRUED
- USED_AMT
- ENDING_BALANCE
- PERSON_ID
- PER_PLAN_ENRT_ID
- ENROLLMENT_START_DATE
- ENROLLMENT_END_DATE
- CATEGRRY_NAME
- LEGISLATION_CODE
- LEGISLATIVE_DATA_GROUP_ID
- LEGAL_ENTITY_ID

## Query

```sql
SELECT aatp.name absence_type ,aapt.name Plan_Name ,acc.per_accrual_entry_id , acc.accrual_period ,acc.work_term_asg_id ,acc.prd_of_svc_id Period_of_service_id ,acc.plan_id ,acc.begin_bal begining_balance ,acc.accrued,acc.used used_amt ,acc.end_bal ending_balance ,acc.person_id ,acc.per_plan_enrt_id , app.enrt_st_dt enrollment_start_date ,app.enrt_end_dt enrollment_end_date ,aatc.CategoryName Categrry_name ,aap.legislation_code ,aap.legislative_data_group_id ,pps.legal_entity_id FROM anc_per_accrual_entries acc, anc_absence_plans_f aap, anc_absence_plans_f_tl aapt ,per_periods_of_service pps , per_all_assignments_f paaf ,anc_per_plan_enrollment app ,anc_absence_type_plans_f atp ,anc_absence_types_f aat ,anc_absence_types_f_tl aatp ,(SELECT c.absence_type_id absType,t.absence_category_id absCat , t.name CategoryName FROM anc_absence_type_cate_f c, anc_absence_categories_f_tl t WHERE t.absence_category_id=c.absence_category_id(+) and t.absence_category_id=t.absence_category_id and trunc(sysdate) between c.effective_start_date and c.effective_end_date and t.language='US' and t.source_lang='US' /*union SELECT b.absence_type_id absType,d.absence_category_id absCat , null FROM anc_absence_type_cate_f d ,anc_absence_types_f b WHERE b.absence_type_id=d.absence_type_id(+) and b.legislation_code='US' and trunc(sysdate) between b.effective_start_date and b.effective_end_date(+) d.effective_end_date(+)*/ ) aatc WHERE acc.plan_id=aap.absence_plan_id and aap.legislation_code='US' and aapt.absence_plan_id=aap.absence_plan_id and aapt.source_lang='US' and aapt.language='US' and trunc(sysdate) between aap.effective_start_date and aap.effective_end_date and trunc(sysdate) between aapt.effective_start_date and aapt.effective_end_date and acc.person_id=pps.person_id and paaf.person_id=pps.person_id and acc.prd_of_svc_id=pps.period_of_service_id and paaf.assignment_id=acc.work_term_asg_id and paaf.work_terms_assignment_id is null and trunc(sysdate) between paaf.effective_start_date and paaf.effective_end_date and app.per_plan_enrt_id=acc.per_plan_enrt_id and app.work_term_asg_id=acc.work_term_asg_id and app.person_id=acc.person_id and aap.legislation_code='US' and atp.absence_plan_id=aap.absence_plan_id and atp.absence_type_id=aat.absence_type_id and aatp.absence_type_id=aat.absence_type_id and trunc(sysdate) between atp.effective_start_date and atp.effective_end_date and trunc(sysdate) between aat.effective_start_date and aat.effective_end_date and trunc(sysdate) between aatp.effective_start_date and aatp.effective_end_date and aatp.source_lang='US' and aatp.language='US' and aat.absence_type_id = aatc.absType
```

---

[← Back to Index](../3_Absence_Management_Views_Index.md)
