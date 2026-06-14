# PAY_OBJ_RESULTS_SEARCH_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payobjresultssearchvl-6293.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payobjresultssearchvl-6293.html)

## Columns

- OBJECT_TYPE
- OBJECT_TYPE_ID
- OBJECT_ID
- OBJECT_NAME
- OBJECT_ACTION_ID
- SOURCE_ACTION_ID
- CHILD_OBJECT_ACTION_ID
- OBJECT_TYPE_CODE
- STATUS
- ACTION_STATUS_CODE
- ACTION_STATUS_LOOKUP_TYPE
- ACTION_TYPE
- ACTION_TYPE_CODE
- PAYROLL_ACTION_ID
- PROCESS_DATE
- PROCESS_START_DATE
- PROCESS_END_DATE
- FLOW_NAME
- FLOW_INSTANCE_NAME
- SUBMISSION_DATE
- SUBMITTED_BY
- TASK_NAME
- OBJECT_REFERENCE
- PERSON_ID
- PERSON_NUMBER
- RELATIONSHIP_NUMBER
- PAYROLL
- PAYROLL_ID
- CONSOLIDATION_SET_NAME
- CONSOLIDATION_SET_ID
- PAYROLL_PERIOD_NAME
- PAYROLL_PERIOD_NUMBER
- DATE_EARNED
- ASSIGNMENT_NUMBER
- ASSIGNMENT_ID
- LEGISLATIVE_DATA_GROUP_ID
- LEGISLATIVE_DATA_GROUP_NAME
- LEGISLATION_CODE
- TASK_INSTANCE_ID
- PAY_REQUEST_ID
- FLOW_INSTANCE_ID
- TASK_ID
- BASE_FLOW_ID
- RUN_TYPE_NAME
- RUN_TYPE_ID
- RETRO_RUN_ID
- PRIMARY_RESULTS
- ADDITIONAL_RESULTS
- EARN_START_DATE
- EARN_END_DATE
- PRORATION_DATES
- EARN_TIME_PERIOD_ID
- PAYMENT_REASON
- PAYROLL_ACTION_STATUS
- DEF_CATEGORY_TYPE
- DEF_SUB_CATEGORY_TYPE
- MARK_FOR_RETRY_ALLOWED
- ROLLBACK_ALLOWED
- REVERSAL_ALLOWED

## Query

```sql
SELECT zzz.OBJECT_TYPE, zzz.OBJECT_TYPE_ID, zzz.OBJECT_ID , substrb(zzz.person_number,instrb(zzz.person_number,'#')+2, length(zzz.person_number)) object_name, zzz.OBJECT_ACTION_ID , zzz.SOURCE_ACTION_ID, zzz.CHILD_OBJECT_ACTION_ID, zzz.OBJECT_TYPE_CODE, zzz.STATUS , zzz.ACTION_STATUS_CODE , zzz.ACTION_STATUS_LOOKUP_TYPE , zzz.ACTION_TYPE , zzz.ACTION_TYPE_CODE , zzz.PAYROLL_ACTION_ID , zzz.PROCESS_DATE, zzz.process_start_date, zzz.process_end_date, zzz.flow_name, zzz.flow_name FLOW_INSTANCE_NAME, zzz.submission_date, zzz.SUBMITTED_BY, zzz.TASK_NAME, zzz.object_reference, zzz.person_id, substrb(zzz.person_number,1,instrb(zzz.person_number,'[#]')-1) person_number, zzz.relationship_number, zzz.payroll, zzz.PAYROLL_ID, zzz.CONSOLIDATION_SET_NAME, zzz.CONSOLIDATION_SET_ID, zzz.payroll_period_name, zzz.payroll_period_number, zzz.date_earned, substrb(zzz.assignment_id,instrb(zzz.assignment_id,'#')+2, length(zzz.assignment_id)) assignment_number, substrb(zzz.assignment_id,1,instrb(zzz.assignment_id,'[#]')-1) ASSIGNMENT_ID, zzz.legislative_data_group_id, zzz.legislative_data_group_name, zzz.LEGISLATION_CODE, zzz.task_instance_id, zzz.pay_request_id, zzz.flow_instance_id, zzz.task_id, zzz.base_flow_id, zzz.RUN_TYPE_NAME, zzz.RUN_TYPE_ID, zzz.retro_run_id, DECODE(zzz.action_status_code,'U','NONE','E','MESSAGES', decode(base_task_name,'PAYSLIP','ATTACHMENT', case (select CLASSIFICATION_NAME from pay_action_classifications cls where cls.ACTION_TYPE=zzz.ACTION_TYPE_CODE and CLASSIFICATION_NAME like '%DEFAULT') when 'SOE_RESULTS_DEFAULT' then 'SOE_RESULTS' when 'RETRO_RESULTS_DEFAULT' then 'RETRO_RESULTS' when 'RUN_RESULTS_DEFAULT' then 'RUN_RESULTS' when 'PREPAY_RESULTS_DEFAULT' then 'PREPAY_RESULTS' when 'PAYMENT_RESULTS_DEFAULT' then 'PAYMENT_RESULTS' when 'COST_RESULTS_DEFAULT' then 'COST_RESULTS' when 'COST_PAY_RESULTS_DEFAULT' then 'COST_PAY_RESULTS' when 'BAL_ADJ_RESULTS_DEFAULT' then 'BAL_ADJ_RESULTS' when 'BAL_RESULTS_DEFAULT' then 'BAL_RESULTS' when 'ARCHIVE_RESULTS_DEFAULT' then 'ARCHIVE_RESULTS' else 'MESSAGES' end )) PRIMARY_RESULTS, DECODE( zzz.action_status_code, 'E', NULL, ( SELECT LISTAGG(CLASSIFICATION_NAME, '|') FROM pay_action_classifications cls WHERE cls.ACTION_TYPE = zzz.ACTION_TYPE_CODE AND CLASSIFICATION_NAME LIKE '%RESULTS' ) || CASE WHEN ( SELECT RULE_MODE FROM PAY_LEGISLATION_RULES WHERE RULE_TYPE = 'ORA_TAX_CALC_STMT' AND LEGISLATION_CODE = zzz.LEGISLATION_CODE ) = 'Y' THEN '|TAX_CALCULATION_STATEMENT' ELSE '' END ) AS ADDITIONAL_RESULTS, Earn_start_date, Earn_end_date, proration_dates, earn_time_period_id, PAYMENT_REASON, PAYROLL_ACTION_STATUS, zzz.def_category_type, zzz.def_sub_category_type, MARK_FOR_RETRY_ALLOWED, ROLLBACK_ALLOWED, Reversal_Allowed FROM ( SELECT pay_obj_act.object_type OBJECT_TYPE, prl.payroll_relationship_id as OBJECT_ID, pay_obj_act.OBJECT_ID OBJECT_TYPE_ID, pay_obj_act.object_ACTION_ID OBJECT_ACTION_ID, DECODE(actionstatuslookup.lookup_code,'E',pay_obj_act.object_ACTION_ID, nvl(decode(actiontypelookup.lookup_code, 'Q',(SELECT MIN(nvl(ch_pro.payroll_rel_action_id,ch.payroll_rel_action_id)) FROM pay_payroll_rel_actions ch,pay_payroll_rel_actions ch_pro WHERE ch.payroll_action_id = payrollactioneo.payroll_action_id and ch_pro.payroll_action_id(+) = payrollactioneo.payroll_action_id and ch_pro.source_action_id(+) = ch.payroll_rel_action_id AND ch.source_action_id = pay_obj_act.object_ACTION_ID AND ch.RETRO_COMPONENT_ID IS NULL ), 'R', (SELECT MIN(nvl(ch_pro.payroll_rel_action_id,ch.payroll_rel_action_id)) FROM pay_payroll_rel_actions ch,pay_payroll_rel_actions ch_pro WHERE ch.payroll_action_id = payrollactioneo.payroll_action_id and ch_pro.payroll_action_id(+) = payrollactioneo.payroll_action_id and ch_pro.source_action_id(+) = ch.payroll_rel_action_id AND ch.source_action_id = pay_obj_act.object_ACTION_ID AND ch.RETRO_COMPONENT_ID IS NULL ), 'V', (SELECT MIN(ch.payroll_rel_action_id) FROM pay_payroll_rel_actions ch WHERE ch.payroll_action_id = payrollactioneo.payroll_action_id AND ch.source_action_id = pay_obj_act.object_ACTION_ID AND ch.RETRO_COMPONENT_ID IS NULL ),pay_obj_act.object_ACTION_ID),pay_obj_act.object_ACTION_ID)) AS child_object_Action_id, pay_obj_act.SOURCE_ACTION_ID, decode(payrollactioneo.action_type,'L',pay_obj_act.object_ACTION_ID,pay_obj_act.source_id) retro_run_id, pay_obj_act.ACTION_TYPE OBJECT_TYPE_CODE, actionstatuslookup.meaning status, actionstatuslookup.lookup_code action_status_code, actionstatuslookup.lookup_type action_status_lookup_type, actiontypelookup.meaning action_type, actiontypelookup.lookup_code action_type_code, pay_obj_act.PAYROLL_ACTION_ID AS payroll_action_id, payrollactioneo.effective_date AS process_date, payrollactioneo.start_date process_start_date, payrollactioneo.end_date process_end_date, NVL(pt.task_name,actiontypelookup.meaning) AS task_name, pt.base_task_name, (select peo.person_number||'[#]'||pname.DISPLAY_NAME from per_all_people_f peo,per_person_names_f pname where peo.person_id = prl.person_id and peo.person_id = pname.person_id and pname.name_type= 'GLOBAL' and peo.effective_start_Date = (Select max(effective_start_Date) from per_all_people_f papf where papf.person_id = prl.person_id) and pname.effective_start_Date = (Select max(effective_start_Date) from per_person_names_f papf where papf.person_id = prl.person_id)) person_number, ppp.payroll_name object_reference, prl.person_id, prl.payroll_relationship_number relationship_number, ppp.payroll_name payroll, ppp.PAYROLL_ID, pcs.CONSOLIDATION_SET_NAME, pcs.CONSOLIDATION_SET_ID, TimePeriodPEOEarn.period_name payroll_period_name, paytimeperiodseo.PERIOD_NUM payroll_period_number, payrollactioneo.date_earned date_earned, (SELECT MAX(asg.assignment_id)||'[#]'||max(asg.assignment_NUMBER) FROM pay_rel_groups_dn asg WHERE asg.payroll_relationship_id = prl.payroll_relationship_id and asg.group_type='A' ) AS assignment_id, ldg.legislative_data_group_id legislative_data_group_id, ldg.name legislative_data_group_name, ldg.LEGISLATION_CODE, prq.flow_task_instance_id task_instance_id, RunTypeDPEO.RUN_TYPE_NAME, RunTypeDPEO.RUN_TYPE_ID, pfi.instance_name as flow_name, pfi.base_flow_id as base_flow_id, (pfi.creation_date) submission_date, (pfi.CREATED_BY) SUBMITTED_BY, payrollactioneo.pay_request_id, pfi.flow_instance_id, TimePeriodPEOEarn.START_DATE Earn_start_date, TimePeriodPEOEarn.END_DATE Earn_end_date, (select listagg(DISTINCT(to_char(pro.start_date,'YYYY-MM-DD')||'||'||to_char(pro.end_date,'YYYY-MM-DD')), ',') from pay_payroll_rel_actions pro where pro.SOURCE_ACTION_ID =pay_obj_act.object_action_id and pro.start_date is not null and pro.run_type_id is null) proration_dates, pt.task_id, payrollactioneo.earn_time_period_id, payrollactioneo.PAYMENT_REASON, payrollactioneo.ACTION_STATUS PAYROLL_ACTION_STATUS, pt.def_category_type, pt.def_sub_category_type, decode(pt.task_id,null,'Y',nvl((select 'Y' from pay_task_actions ppta where ppta.base_task_id=pt.task_id and EXECUTION_MODE='ROLLBACK' and not exists(select 1 from pay_task_properties pptp where pptp.base_task_action_id=ppta.task_action_id and pptp.BASE_TASK_PROPERTY_NAME='OBJ_LEVEL_ACTION_DISABLED' and pptp.TASK_PROPERTY_VALUE='Y') and rownum=1),'N')) ROLLBACK_ALLOWED, decode(pt.task_id,null,'Y',nvl((select 'Y' from pay_task_actions ppta where ppta.base_task_id=pt.task_id and EXECUTION_MODE='MARK_FOR_RETRY' and not exists(select 1 from pay_task_properties pptp where pptp.base_task_action_id=ppta.task_action_id and pptp.BASE_TASK_PROPERTY_NAME='OBJ_LEVEL_ACTION_DISABLED' and pptp.TASK_PROPERTY_VALUE='Y') and rownum=1),'N')) MARK_FOR_RETRY_ALLOWED, DECODE(( select max(1) from pay_action_interlocks lk, pay_payroll_rel_actions lk_pra,pay_payroll_actions lk_ppa where lk_ppa.payroll_action_id= lk_pra.payroll_action_id and lk.locking_action_id =lk_pra.payroll_rel_action_id and lk.locked_action_id =pay_obj_act.object_action_id and lk_ppa.ACTION_TYPE='V' and payrollactioneo.action_type in('R','Q')),NULL,DECODE(pay_obj_act.ACTION_STATUS,'C',DECODE(payrollactioneo.ACTION_TYPE,'R','Y','Q','Y','N'),'N'),'N') AS Reversal_Allowed FROM hcm_lookups actiontypelookup, hcm_lookups actionstatuslookup, pay_all_actions pay_obj_act, pay_payroll_actions payrollactioneo, pay_requests prq, FUSION.pay_task_actions pta, pay_tasks_vl pt, per_legislative_data_groups_vl ldg, pay_pay_relationships_dn prl, pay_all_payrolls_f ppp, pay_consolidation_sets pcs, PAY_TIME_PERIODS TimePeriodPEOEarn, pay_time_periods paytimeperiodseo, PAY_RUN_TYPES_VL RunTypeDPEO, pay_flow_instances pfi WHERE pfi.flow_instance_id(+)=prq.flow_instance_id and actiontypelookup.lookup_type = 'ACTION_TYPE' AND actiontypelookup.lookup_code = payrollactioneo.action_type AND actionstatuslookup.lookup_type = 'ORA_PAY_WU_ACTION_STATUS' AND actionstatuslookup.lookup_code = pay_obj_act.ACTION_STATUS AND payrollactioneo.payroll_action_id =pay_obj_act.payroll_action_id AND payrollactioneo.dedn_time_period_id = paytimeperiodseo.time_period_id (+) AND payrollactioneo.earn_time_period_id =TimePeriodPEOEarn.TIME_PERIOD_ID (+) AND pay_obj_act.RUN_TYPE_ID = RunTypeDPEO.RUN_TYPE_ID (+) and pay_obj_act.SOURCE_ACTION_ID is null AND prq.pay_request_id (+) = payrollactioneo.pay_request_id AND prq.pay_task_action_id = pta.task_action_id (+) AND pta.base_task_id = pt.task_id (+) AND payrollactioneo.legislative_data_group_id = ldg.legislative_data_group_id (+) AND payrollactioneo.action_type <> 'XRD' AND ((pt.legislative_data_group_id IS NOT NULL AND pt.legislation_code IS NULL AND pt.legislative_data_group_id = ldg.legislative_data_group_id) OR (pt.legislation_code IS NOT NULL AND pt.legislative_data_group_id IS NULL AND pt.legislation_code =ldg.legislation_code AND ( NOT EXISTS (SELECT TASK_ID FROM FUSION.PAY_TASK_ACTIONS_VL c1 WHERE pt.BASE_TASK_ID = c1.BASE_TASK_ID AND (c1.legislative_data_group_id IS NOT NULL AND c1.legislation_code IS NULL AND c1.legislative_data_group_id = ldg.legislative_data_group_id ) ))) OR ( pt.legislative_data_group_id IS NULL AND pt.legislation_code IS NULL AND ( NOT EXISTS (SELECT TASK_ID FROM FUSION.PAY_TASK_ACTIONS_VL c2 WHERE pt.BASE_TASK_ID = c2.BASE_TASK_ID AND (( c2.legislative_data_group_id IS NOT NULL AND c2.legislation_code IS NULL AND c2.legislative_data_group_id = ldg.legislative_data_group_id) OR ( c2.legislation_code IS NOT NULL AND c2.legislative_data_group_id IS NULL AND c2.legislation_code = ldg.legislation_code )) )))) and ( (prl.payroll_relationship_id = pay_obj_act.payroll_relationship_id) ) and payrollactioneo.payroll_id=ppp.payroll_id (+) and pcs.CONSOLIDATION_SET_ID(+)=payrollactioneo.CONSOLIDATION_SET_ID and payrollactioneo.effective_date between ppp.effective_start_Date (+) and ppp.effective_end_date (+) AND (payrollactioneo.EFFECTIVE_DATE BETWEEN RunTypeDPEO.EFFECTIVE_START_DATE (+) AND RunTypeDPEO.EFFECTIVE_END_DATE (+) ) ) zzz
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
