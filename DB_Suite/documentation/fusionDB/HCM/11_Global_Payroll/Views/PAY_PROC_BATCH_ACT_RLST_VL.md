# PAY_PROC_BATCH_ACT_RLST_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payprocbatchactrlstvl-5304.html#payprocbatchactrlstvl-5304](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payprocbatchactrlstvl-5304.html#payprocbatchactrlstvl-5304)

## Columns

- OBJECT_ID
- OBJECT_NAME
- BATCH_LINE_ID
- LINE_STATUS
- LINE_STATUS_CODE
- ACTION_TYPE
- FLOW_NAME
- TASK_NAME
- LEGISLATIVE_DATA_GROUP_ID
- LEGISLATIVE_DATA_GROUP_NAME
- TASK_INSTANCE_ID
- FLOW_INSTANCE_ID
- SUBMISSION_DATE
- MESSAGES_DISPLAY_FLAG
- PRIMARY_RESULTS

## Query

```sql
SELECT zzz.OBJECT_ID , zzz.object_name, zzz.batch_line_id , zzz.LINE_STATUS , zzz.LINE_STATUS_CODE , zzz.ACTION_TYPE , zzz.flow_name, zzz.TASK_NAME, zzz.legislative_data_group_id, zzz.legislative_data_group_name, zzz.task_instance_id, zzz.flow_instance_id, zzz.submission_date, 'Y' MESSAGES_DISPLAY_FLAG, 'Messages' PRIMARY_RESULTS FROM ( SELECT distinct to_char((select distinct max(pblv.action_parameter_value) from pay_batch_line_values pblv, pay_task_parameters_vl ddd where pblv.batch_line_id = pbl.batch_line_id and pblv.action_parameter_id = ddd.task_parameter_id and pblv.action_parameter_value is not null and ddd.display_flag='N' and ddd.element_name='PAYROLL_RELATIONSHIP_ID')) as OBJECT_ID, pbl.batch_line_id batch_line_id, actionstatuslookup.meaning line_Status, actionstatuslookup.lookup_code line_status_code, pblta.display_task_action_name|| (select max(':'||pblv.action_parameter_value) from pay_batch_line_values pblv where pblv.batch_line_id = pbl.batch_line_id and pblv.action_parameter_id = pbltpp.task_parameter_id) action_type, pbh.batch_id , pblt.display_task_name||'-'||pt.task_name AS task_name, (select distinct listagg( ddd.parameter_name||'='||pblv.action_parameter_value,'|') within group (order by ddd.param_sequence) from pay_batch_line_values pblv, pay_task_parameters_vl ddd where pblv.batch_line_id = pbl.batch_line_id and pblv.action_parameter_id = ddd.task_parameter_id and ddd.display_flag != 'N' and pblv.action_parameter_value is not null) object_name, ldg.legislative_data_group_id legislative_data_group_id, ldg.name legislative_data_group_name, pft.flow_task_instance_id task_instance_id, pfi.flow_instance_id, pfi.instance_name as flow_name, trunc(pfi.creation_date) submission_date FROM pay_batch_headers pbh, pay_batch_lines pbl, pay_flow_task_instances pft, pay_flow_tasks_vl ft, PAY_FLOW_TASK_PARAM_VALS ppp, pay_flow_task_parameters pftp, pay_task_parameters ptp, hcm_lookups actionstatuslookup, pay_tasks_vl pt, FUSION.pay_bl_task_actions_vl pblta, pay_bl_tasks_vl pblt, pay_flow_instances pfi, pay_task_properties pbltp, pay_task_parameters pbltpp, per_legislative_data_groups_vl ldg WHERE pfi.flow_instance_id=pft.flow_instance_id AND ppp.flow_task_instance_id = pft.flow_task_instance_id and pbh.legislative_data_group_id= ldg.legislative_data_group_id and pftp.base_flow_task_param_id=ppp.base_flow_task_param_id and pt.base_task_id = ft.base_task_id and pftp.base_task_parameter_id = ptp.base_task_parameter_id and ptp.BASE_TASK_PARAMETER_NAME like '%BATCH%' and to_char(ppp.flow_task_param_value) = to_char(pbh.batch_id) and DECODE(length(TRIM(translate(ppp.flow_task_param_value,'0123456789',' ') ) ),NULL,to_number(ppp.flow_task_param_value),NULL) = pbh.batch_id AND ft.flow_task_id = pft.BASE_FLOW_TASK_ID and pbl.batch_id=pbh.batch_id and decode(pbl.batch_line_status,'T','C',pbl.batch_line_status) = actionstatuslookup.lookup_code AND actionstatuslookup.lookup_type = 'ORA_PAY_WU_ACTION_STATUS' and pblta.task_action_id = pbl.task_action_id and pblta.task_id = pblt.task_id and pbltp.base_task_action_id (+) = pblta.task_action_id and pbltp.TASK_PROPERTY_TYPE (+) = 'BL_KEY_PARAMETER' and pbltpp.base_task_action_id (+) = pbltp.base_task_action_id and pbltpp.element_name (+) = pbltp.task_property_value and pt.task_type != 'MANUAL_TASK' /* Bal Init */ union all select to_char(pbl.PAYROLL_RELATIONSHIP_ID) as OBJECT_ID, pbl.batch_line_id , nvl(actionstatuslookup.meaning,BLstatuslookup.meaning) line_status, nvl(actionstatuslookup.lookup_code,BLstatuslookup.lookup_code) line_status_code, pt.task_name action_type, pbh.batch_id , pt.task_name AS task_name, 'Line Sequence='||pbl.LINE_SEQUENCE||'|'|| 'Payroll Relationship Number='||pbl.payroll_relationship_number||'|'|| 'Assignment Number='||pbl.assignment_number||'|'|| 'Balance Name='||pbl.BALANCE_NAME||'|'|| 'Balance Dimension='||pbl.DIMENSION_NAME||'|'|| 'Upload Date='||pbl.UPLOAD_DATE||'|'|| 'Value='||pbl.VALUE object_name, ldg.legislative_data_group_id legislative_data_group_id, ldg.name legislative_data_group_name, pft.flow_task_instance_id task_instance_id, pfi.flow_instance_id, pfi.instance_name as flow_name, trunc(pfi.creation_date) submission_date FROM PAY_BAL_BATCH_HEADERS pbh, PAY_BAL_BATCH_LINES pbl, hcm_lookups BLstatuslookup, pay_flow_task_instances pft, pay_flow_tasks_vl ft, PAY_FLOW_TASK_PARAM_VALS ppp, pay_flow_task_parameters pftp, pay_task_parameters ptp, hcm_lookups actionstatuslookup, pay_flow_instances pfi, per_legislative_data_groups_vl ldg, pay_tasks_vl pt WHERE pfi.flow_instance_id=pft.flow_instance_id AND ppp.flow_task_instance_id = pft.flow_task_instance_id and pbh.legislative_data_group_id= ldg.legislative_data_group_id and pftp.base_flow_task_param_id=ppp.base_flow_task_param_id and pt.base_task_id = ft.base_task_id and pftp.base_task_parameter_id = ptp.base_task_parameter_id and ptp.BASE_TASK_PARAMETER_NAME like '%BATCH%' and pt.base_task_name='BALANCE_INITIALIZATION' and ppp.flow_task_param_value = to_char(pbh.batch_id) AND ft.flow_task_id = pft.BASE_FLOW_TASK_ID and pbl.batch_id=pbh.batch_id and decode(pbl.batch_line_status,'T','C',pbl.batch_line_status) = actionstatuslookup.lookup_code(+) AND actionstatuslookup.lookup_type(+) = 'ORA_PAY_WU_ACTION_STATUS' AND BLstatuslookup.lookup_type = 'PAY_BATCH_STATUS' AND BLstatuslookup.lookup_code = pbl.batch_line_status ) zzz order by zzz.submission_date desc, zzz.batch_line_id desc, decode(zzz.line_status_code,'P',0,'E',1,'U',2,'I',3,'V',4,'S',5,'M',6,7)
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
