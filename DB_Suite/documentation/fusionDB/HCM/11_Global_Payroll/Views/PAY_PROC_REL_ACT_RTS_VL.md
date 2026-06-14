# PAY_PROC_REL_ACT_RTS_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payprocrelactrtsvl-7827.html#payprocrelactrtsvl-7827](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payprocrelactrtsvl-7827.html#payprocrelactrtsvl-7827)

## Columns

- OBJECT_TYPE
- OBJECT_ID
- OBJECT_NAME
- OBJECT_ACTION_ID
- CHILD_OBJECT_ACTION_ID
- PREPAY_REL_ACTION_ID
- ACTION_CODE
- STATUS
- ACTION_STATUS_CODE
- ACTION_TYPE
- ACTION_TYPE_CODE
- PAYROLL_ACTION_ID
- PROCESS_DATE
- ACCOUNTING_START_DATE
- ACCOUNTING_END_DATE
- LOCKINGFLAG
- LOCKINGSTATUS
- FLOW_NAME
- TASK_NAME
- OBJECT_REFERENCE
- PERSON_ID
- PERSON_NUMBER
- RELATIONSHIP_NUMBER
- PAYROLL
- PAYROLL_PERIOD_NAME
- PAYROLL_PERIOD_NUMBER
- DATE_EARNED
- ASSIGNMENT_NUMBER
- LOCATION_NAME
- JOB_NAME
- ASSIGNMENT_ID
- RELATIONSHIP_TYPE
- KEYWORDS
- LEGISLATIVE_DATA_GROUP_ID
- LEGISLATIVE_DATA_GROUP_NAME
- ASSIGNMENT_STATUS
- TASK_INSTANCE_ID
- PAY_REQUEST_ID
- RUN_TYPE_NAME
- ROLLBACK_ALLOWED_FLAG
- REVERSAL_ALLOWED_FLAG
- MARKFORRETRY_ALLOWED_FLAG
- SOE_DISPLAY_FLAG
- RUN_RESULTS_DISPLAY_FLAG
- BAL_RESULTS_DISPLAY_FLAG
- COST_RESULTS_DISPLAY_FLAG
- COST_PAY_RESULTS_DISPLAY_FLAG
- PREPAY_RESULTS_DISPLAY_FLAG
- PAYMT_RESULTS_DISPLAY_FLAG
- ARCH_RESULTS_DISPLAY_FLAG
- MESSAGES_DISPLAY_FLAG
- PRIMARY_RESULTS
- KEY_INFO
- EARN_START_DATE
- EARN_END_DATE

## Query

```sql
SELECT zzz.OBJECT_TYPE, zzz.OBJECT_ID , zzz.object_name object_name, zzz.OBJECT_ACTION_ID , zzz.CHILD_OBJECT_ACTION_ID, zzz.prepay_rel_Action_id, zzz.ACTION_CODE, zzz.STATUS , zzz.ACTION_STATUS_CODE , zzz.ACTION_TYPE , zzz.ACTION_TYPE_CODE , zzz.PAYROLL_ACTION_ID , zzz.PROCESS_DATE, zzz.Accounting_Start_Date, zzz.Accounting_End_Date, zzz.LOCKINGFLAG , zzz.LOCKINGSTATUS , zzz.flow_name, zzz.TASK_NAME, zzz.object_reference, zzz.person_id, zzz.person_number, zzz.relationship_number, zzz.payroll, zzz.payroll_period_name, zzz.payroll_period_number, zzz.date_earned, substrb(zzz.assignment_id,instrb(zzz.assignment_id,'#')+2, length(zzz.assignment_id)) assignment_number, zzz.LOCATION_NAME, zzz.JOB_NAME, substrb(zzz.assignment_id,1,instrb(zzz.assignment_id,'[#]')-1) ASSIGNMENT_ID, zzz.Relationship_type, zzz.keywords, zzz.legislative_data_group_id, zzz.legislative_data_group_name, zzz.assignment_status, zzz.task_instance_id, zzz.pay_request_id, zzz.RUN_TYPE_NAME, DECODE(ACT_FLAG_ACTION_TYPE,'1',DECODE(LOCKINGFLAG,'-1','Y','N'),'N' ) AS Rollback_Allowed_FLAG, DECODE(( select max(1) from pay_payroll_actions paac2, pay_payroll_rel_actions paac where paac.payroll_rel_action_id =LOCKINGFLAG and paac2.payroll_action_id= paac.payroll_action_id and paac2.ACTION_TYPE='V'),NULL,DECODE(zzz.ACTION_STATUS_CODE,'C',DECODE(zzz.ACTION_TYPE_CODE,'R','Y','Q','Y','N'),'N'),'N') AS Reversal_Allowed_FLAG, DECODE(zzz.ACT_FLAG_ACTION_TYPE,'1',DECODE(zzz.ACTION_STATUS_CODE,'C',DECODE(zzz.LOCKINGFLAG,'-1',DECODE(zzz.ACTION_TYPE_CODE,'D',decode(( select max(1) from pay_payroll_rel_actions paac2, pay_payroll_rel_actions paac, pay_action_interlocks pai where pai.locking_action_id =zzz.OBJECT_ACTION_ID and pai.locked_action_id = paac.payroll_rel_action_id and paac.pre_payment_id = paac2.pre_payment_id and paac2.action_sequence > paac.action_sequence),null,'Y','N'),'Y'),DECODE(zzz.LOCKINGSTATUS,'M','Y','N')),'N'),'N') AS MarkForRetry_Allowed_FLAG, DECODE(zzz.action_status_code,'E','N',DECODE(zzz.ACTION_TYPE_CODE,'R','Y','Q','Y','V','Y','B','Y','I','Y','CTG','Y','CQ','Y','N')) AS SOE_DISPLAY_FLAG, DECODE(zzz.action_status_code,'E','N',DECODE(zzz.ACTION_TYPE_CODE,'R','Y','Q','Y','V','Y','B','Y','I','Y','CTG','Y','CQ','Y','L','Y','N')) as RUN_RESULTS_DISPLAY_FLAG, DECODE(zzz.action_status_code,'E','N',DECODE(zzz.ACTION_TYPE_CODE,'R','Y','Q','Y','V','Y','B','Y','I','Y','CTG','Y','CQ','Y','N')) AS BAL_RESULTS_DISPLAY_FLAG, DECODE(zzz.action_status_code,'E','N',DECODE(zzz.ACTION_TYPE_CODE,'R','Y','Q','Y','V','Y','CTG','Y','CQ','Y','C','Y','CA','Y','S','Y','CR','Y','EC','Y','N')) AS COST_RESULTS_DISPLAY_FLAG, DECODE(zzz.action_status_code,'E','N',DECODE(zzz.ACTION_TYPE_CODE,'CP','Y','N')) AS COST_PAY_RESULTS_DISPLAY_FLAG, DECODE(zzz.action_status_code,'E','N',DECODE(zzz.ACTION_TYPE_CODE,'P','Y','U','Y','PRU','Y','CTG','Y','N')) AS PREPAY_RESULTS_DISPLAY_FLAG, DECODE(zzz.action_status_code,'E','N',DECODE(zzz.ACTION_TYPE_CODE,'H','Y','PP','Y','M','Y','E','Y','D','Y','CTG','Y','N')) AS PAYMT_RESULTS_DISPLAY_FLAG, DECODE(zzz.action_status_code,'E','N',DECODE(zzz.ACTION_TYPE_CODE,'CTG','Y','X','Y','PS','Y','XWr','Y','Wr','Y','N')) AS ARCH_RESULTS_DISPLAY_FLAG, 'Y' MESSAGES_DISPLAY_FLAG, DECODE(zzz.action_status_code,'U','NONE','E','Messages',DECODE(zzz.ACTION_TYPE_CODE,'R','Statement of Earnings','Q','Statement of Earnings','V','Statement of Earnings','CTG','Statement of Earnings','L','Run Results','P','Prepayment Results','U','Prepayment Results','PRU','Prepayment Results','H','Payment Results','M','Payment Results','E','Payment Results','PP','Payment Results','D','Payment Results','C','Costing Results','CA','Costing Results','EC','Costing Results','CP','Costing of payment','B','Balances Results','I','Balances Results','X','Archive Results','PS','Archive Results','Wr','Archive Results','XWr','Archive Results','Messages')) PRIMARY_RESULTS, DECODE(DECODE(zzz.action_type_code,'P','PrePayment_Amount','U','PrePayment_Amount','H','Payment_Amount','PP','Payment_Amount','M','Payment_Amount','E','Payment_Amount','D','Payment_Amount' ,'R','Gross_Pay','Q','Gross_Pay','V','Gross_Pay','CTG','Gross_Pay','L','Retro_Gross_Pay','B','Gross_Pay','I','Gross_Pay' ,'CQ','CTRS','C','CTRS','CA','CTRS','CP','CTPY','S','CTRS','CR','CTRS','EC','CTRS' ,'G','Archived Information','GI','Archived Information','PS','Archived Information','X','Archived Information','XWr','Archived Information','Wr','Archived Information' ,NULL) ,'PrePayment_Amount',(SELECT 'Amount='||to_char(SUM(PPP.BASE_CURRENCY_VALUE))||','||max(ldg.default_currency_code)||'|' FROM PAY_PRE_PAYMENTS PPP, PAY_ORG_PAY_METHODS_F opm, pay_legislative_data_groups ldg WHERE PPP.PAYROLL_REL_ACTION_ID = object_action_id and ppp.ORG_PAYMENT_METHOD_ID=opm.ORG_PAYMENT_METHOD_ID and opm.legislative_Data_group_id=ldg.legislative_Data_group_id and PROCESS_DATE between opm.effective_start_date and opm.effective_end_date GROUP BY PPP.PAYROLL_REL_ACTION_ID) ,'Payment_Amount',(SELECT (SELECT MEANING FROM HCM_LOOKUPS LK1 WHERE LK1.LOOKUP_TYPE= 'PAY_STATUS' AND LK1.LOOKUP_CODE=HR_PRE_PAY.PAYMENT_STATUS(object_action_id,action_type_code)) ||'='||to_char(ppp.value)||','||opm.CURRENCY_CODE||'|' FROM PAY_PRE_PAYMENTS PPP, pay_payroll_rel_actions pra , PAY_ORG_PAY_METHODS_F opm where pra.PRE_PAYMENT_ID = PPP.PRE_PAYMENT_ID and pra.PAYROLL_REL_ACTION_ID =object_action_id and ppp.ORG_PAYMENT_METHOD_ID=opm.ORG_PAYMENT_METHOD_ID and PROCESS_DATE between opm.effective_start_date and opm.effective_end_date) ,'CTPY',(select 'Amount Debited='||sum(decode(ppc.debit_or_credit,'D',ppc.value))||','||ppc.currency_code|| '|Amount Credited='||sum(decode(ppc.debit_or_credit,'C',ppc.value))||','||ppc.currency_code from pay_payment_costs ppc where ppc.payroll_rel_action_id=CHILD_OBJECT_ACTION_ID group by ppc.payroll_rel_action_id , ppc.currency_code) ,'CTRS',(select 'Amount Debited='||sum(decode(inputValues.UOM,'M',decode(costs.DEBIT_OR_CREDIT,'D',costs.COSTED_VALUE)))||','||elementTypes.output_currency_code|| '|Amount Credited='||sum(decode(inputValues.UOM,'M',decode(costs.DEBIT_OR_CREDIT,'C',costs.COSTED_VALUE)))||','||elementTypes.output_currency_code from pay_costs costs, pay_element_types_vl elementTypes, pay_input_values_vl inputValues where costs.payroll_rel_action_id=CHILD_OBJECT_ACTION_ID and costs.input_value_id = inputValues.input_value_id and elementTypes.element_type_id=inputValues.element_type_id group by costs.payroll_rel_action_id,elementTypes.output_currency_code) ,'Archived Information',null ,null) KEY_INFO, Earn_start_date, Earn_end_date FROM (SELECT distinct 'PRA' OBJECT_TYPE, prl.payroll_relationship_id as OBJECT_ID, pay_obj_act.payroll_rel_ACTION_ID OBJECT_ACTION_ID, NVL( decode(actiontypelookup.lookup_code,'L', (SELECT MAX(ch.payroll_rel_action_id) FROM pay_payroll_rel_actions ch WHERE ch.source_id = pay_obj_act.payroll_rel_action_id AND ch.RETRO_COMPONENT_ID IS NOT NULL AND ch.payroll_relationship_id = pay_obj_act.payroll_relationship_id ) ,(SELECT MAX(ch.payroll_rel_action_id) FROM pay_payroll_rel_actions ch WHERE ch.payroll_action_id = payrollactioneo.payroll_action_id AND ch.source_action_id = pay_obj_act.payroll_rel_action_id AND ch.RETRO_COMPONENT_ID IS NULL )) ,pay_obj_act.payroll_rel_action_id) AS child_object_Action_id, (SELECT max(ch.payroll_rel_ACTION_ID) from pay_action_interlocks l, pay_payroll_rel_actions ch , pay_payroll_actions ppa where locked_action_id=pay_obj_act.payroll_rel_ACTION_ID and ch.payroll_rel_ACTION_ID=l.locking_action_id and ch.payroll_action_id=ppa.payroll_action_id and ppa.action_type in ('U','P') ) prepay_rel_Action_id, 'PREL' AS ACTION_CODE, actionstatuslookup.meaning status, actionstatuslookup.lookup_code action_status_code, actiontypelookup.meaning action_type, actiontypelookup.lookup_code action_type_code, pay_obj_act.PAYROLL_ACTION_ID AS payroll_action_id, payrollactioneo.effective_date AS process_date, NVL( (SELECT MAX(l.locking_action_id) AS lockingId FROM pay_action_interlocks l WHERE l.locked_action_id=pay_obj_act.payroll_rel_ACTION_ID ),-1) AS LockingFlag, (SELECT NVL(rel.action_status,'N/A') FROM pay_payroll_rel_actions rel WHERE rel.payroll_rel_action_id = NVL( (SELECT MAX(l.locking_action_id) AS lockingId FROM pay_action_interlocks l WHERE l.locked_action_id=pay_obj_act.payroll_rel_ACTION_ID ),-1) ) AS LockingStatus , NVL(pt.task_name,actiontypelookup.meaning) AS task_name, (select pname.LIST_NAME LIST_NAME from per_person_names_f pname where pname.person_id = prl.person_id and pname.name_type= 'GLOBAL' and pname.effective_start_Date = (Select max(effective_start_Date) from per_person_names_f ppnf where ppnf.person_id = prl.person_id and ppnf.name_type= 'GLOBAL')) object_name, ppp.payroll_name object_reference, prl.person_id, (select peo.person_number PERSON_NUMBER from per_all_people_f peo where peo.person_id = prl.person_id and peo.effective_start_Date = (Select max(effective_start_Date) from per_all_people_f papf where papf.person_id = prl.person_id)) person_number, prl.payroll_relationship_number relationship_number, ppp.payroll_name payroll, TimePeriodPEOEarn.period_name payroll_period_name, paytimeperiodseo.PERIOD_NUM payroll_period_number, payrollactioneo.date_earned date_earned, (SELECT MAX(asg.assignment_id)||'[#]'||max(asg.assignment_NUMBER) FROM pay_rel_groups_dn asg WHERE asg.payroll_relationship_id = prl.payroll_relationship_id and asg.group_type='A' ) AS assignment_id, null Relationship_type, null keywords, ldg.legislative_data_group_id legislative_data_group_id, ldg.name legislative_data_group_name, null assignment_status, prq.flow_task_instance_id task_instance_id, RunTypeDPEO.RUN_TYPE_NAME, pfi.instance_name as flow_name, null as Accounting_Start_Date, null as Accounting_End_Date, NULL AS LOCATION_NAME, NULL AS Job_NAME , ACT_FLAG.ACT_FLAG_ACTION_TYPE, payrollactioneo.pay_request_id, TimePeriodPEOEarn.START_DATE Earn_start_date, TimePeriodPEOEarn.END_DATE Earn_end_date FROM hcm_lookups actiontypelookup, hcm_lookups actionstatuslookup, pay_payroll_rel_actions pay_obj_act, pay_payroll_actions payrollactioneo, pay_requests prq, FUSION.pay_task_actions pta, pay_tasks_vl pt, per_legislative_data_groups_vl ldg, pay_pay_relationships_dn prl, pay_all_payrolls_f ppp, PAY_TIME_PERIODS TimePeriodPEOEarn, pay_time_periods paytimeperiodseo, PAY_RUN_TYPES_VL RunTypeDPEO, pay_flow_instances pfi, (SELECT LOOKUP_CODE,'1' ACT_FLAG_ACTION_TYPE FROM HCM_LOOKUPS ACT WHERE LOOKUP_CODE IN('B','C','CP','CA','CQ','CR','D','E','EC','GI','H','L','M','P','PP','PS','PRU','Q','R','RG','S','T','TC','U','X','XWr','V','Wr') AND LOOKUP_TYPE='ACTION_TYPE') ACT_FLAG WHERE payrollactioneo.action_type=ACT_FLAG.LOOKUP_CODE(+) AND pfi.flow_instance_id(+)=prq.flow_instance_id and actiontypelookup.lookup_type = 'ACTION_TYPE' AND actiontypelookup.lookup_code = payrollactioneo.action_type AND actionstatuslookup.lookup_type = 'PAY_ACTION_STATUS' AND actionstatuslookup.lookup_code = pay_obj_act.ACTION_STATUS AND payrollactioneo.payroll_action_id =pay_obj_act.payroll_action_id AND payrollactioneo.dedn_time_period_id = paytimeperiodseo.time_period_id (+) AND payrollactioneo.earn_time_period_id =TimePeriodPEOEarn.TIME_PERIOD_ID (+) AND payrollactioneo.RUN_TYPE_ID = RunTypeDPEO.RUN_TYPE_ID (+) AND pay_obj_act.source_action_id IS NULL AND pay_obj_act.RETRO_COMPONENT_ID IS NULL AND prq.pay_request_id (+) = payrollactioneo.pay_request_id AND prq.pay_task_action_id = pta.task_action_id (+) AND pta.base_task_id = pt.task_id (+) AND payrollactioneo.legislative_data_group_id = ldg.legislative_data_group_id (+) AND ((pt.legislative_data_group_id IS NOT NULL AND pt.legislation_code IS NULL AND pt.legislative_data_group_id = ldg.legislative_data_group_id) OR (pt.legislation_code IS NOT NULL AND pt.legislative_data_group_id IS NULL AND pt.legislation_code =ldg.legislation_code AND ( NOT EXISTS (SELECT TASK_ID FROM FUSION.PAY_TASK_ACTIONS_VL c1 WHERE pt.BASE_TASK_ID = c1.BASE_TASK_ID AND (c1.legislative_data_group_id IS NOT NULL AND c1.legislation_code IS NULL AND c1.legislative_data_group_id = ldg.legislative_data_group_id ) ))) OR ( pt.legislative_data_group_id IS NULL AND pt.legislation_code IS NULL AND ( NOT EXISTS (SELECT TASK_ID FROM FUSION.PAY_TASK_ACTIONS_VL c2 WHERE pt.BASE_TASK_ID = c2.BASE_TASK_ID AND (( c2.legislative_data_group_id IS NOT NULL AND c2.legislation_code IS NULL AND c2.legislative_data_group_id = ldg.legislative_data_group_id) OR ( c2.legislation_code IS NOT NULL AND c2.legislative_data_group_id IS NULL AND c2.legislation_code = ldg.legislation_code )) )))) and prl.payroll_relationship_id = pay_obj_act.payroll_relationship_id and payrollactioneo.payroll_id=ppp.payroll_id (+) and payrollactioneo.effective_date between ppp.effective_start_Date (+) and ppp.effective_end_date (+) AND (payrollactioneo.EFFECTIVE_DATE BETWEEN RunTypeDPEO.EFFECTIVE_START_DATE (+) AND RunTypeDPEO.EFFECTIVE_END_DATE (+) ) ) zzz order by zzz.process_date desc, zzz.object_Action_id desc, decode(zzz.action_status_code,'P',0,'E',1,'U',2,'I',3,'V',4,'S',5,'M',6,7)
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
