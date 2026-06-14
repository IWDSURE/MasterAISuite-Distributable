# PAY_TASK_RESULT_FLOWS_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytaskresultflowsvl-5499.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytaskresultflowsvl-5499.html)

## Columns

- OBJECT_NAME
- OBJECT_DISPLAY_NAME
- OBJECT_URL
- OBJECT_PARAMS
- DEFAULT_URL
- ENABLE_FLAG
- TASK_INSTANCE_ID
- OBJECTGROUPNAME

## Query

```sql
select OBJECT_NAME,OBJECT_DISPLAY_NAME, OBJECT_URL, OBJECT_PARAMS, DEFAULT_URL, ENABLE_FLAG,task_instance_id, ObjectGroupName FROM ( select 'COST_ADJ' as OBJECT_NAME, 'Cost Adjustments' as OBJECT_DISPLAY_NAME, '/WEB-INF/oracle/apps/hcm/payrolls/costs/results/publicUi/internal/flow/AccountingWorkareaTF.xml#AccountingWorkareaTF' AS OBJECT_URL, 'pFlowInstanceId='||pfTi.flow_instance_id||';callingMode=COST_ADJ;' AS OBJECT_PARAMS, NULL AS DEFAULT_URL, 'Y' AS ENABLE_FLAG, pfti.FLOW_TASK_INSTANCE_id as task_instance_id , NULL ObjectGroupName from pay_tasks TT, pay_flow_tasks pft , (select pay_flow_task_instances.BASE_FLOW_TASK_ID , pay_flow_task_instances.flow_instance_id, pay_flow_task_instances.flow_task_instance_id, per_person_names_f_v.DISPLAY_NAME as personName, pay_cost_adjustments.cost_adjustment_id, pay_cost_adjustments.cost_adjustment_action_id, pay_cost_adjustments.adjustment_name, pay_cost_adjustments.ADJUSTMENT_DESCRIPTION, pay_cost_adjustments.CREATION_DATE, fnd_lookup_values_vl.MEANING, per_person_names_f_v.legislation_code, pay_cost_adjustments.legislative_data_group_id, pay_cost_adjustments.payroll_relationship_id, pay_cost_adjustments.payroll_rel_action_id, pay_payroll_rel_actions.payroll_action_id from pay_cost_adjustments, pay_pay_relationships_dn, per_person_names_f_v, pay_payroll_rel_actions, pay_payroll_actions, pay_requests, pay_flow_task_instances, fnd_lookup_values_vl where pay_cost_adjustments.PAYROLL_RELATIONSHIP_ID = pay_pay_relationships_dn.PAYROLL_RELATIONSHIP_ID and pay_pay_relationships_dn.PERSON_ID = per_person_names_f_v.PERSON_ID and fnd_lookup_values_vl.LOOKUP_TYPE = 'APPROVAL_ACTION' and pay_cost_adjustments.STATUS = fnd_lookup_values_vl.LOOKUP_CODE and pay_cost_adjustments.PAYROLL_REL_ACTION_ID = pay_payroll_rel_actions.PAYROLL_REL_ACTION_ID and pay_payroll_actions.PAYROLL_ACTION_ID = pay_payroll_rel_actions.PAYROLL_ACTION_ID and pay_requests.pay_REQUEST_ID = pay_payroll_actions.PAY_REQUEST_ID and pay_requests.FLOW_TASK_INSTANCE_ID = pay_flow_task_instances.FLOW_TASK_INSTANCE_ID) pfti where task_type='PUYGEN' AND pft.BASE_TASK_ID=TT.BASE_TASK_ID AND base_task_name ='PAYROLL_RUN' AND pfti.BASE_FLOW_TASK_ID=pft.FLOW_TASK_ID union SELECT 'OBJECT_GROUPS' as OBJECT_NAME, 'Manage Process Information Group' as OBJECT_DISPLAY_NAME, '/WEB-INF/oracle/apps/hcm/objectGroups/ui/flow/ManageObjectGroups.xml#ManageObjectGroups' AS OBJECT_URL, 'pObjectGroupId='||pog.object_group_id||';' AS OBJECT_PARAMS, NULL AS DEFAULT_URL, 'Y' AS ENABLE_FLAG, FLOW_TASK_INSTANCE_id as task_instance_id ,ObjectGroupName FROM pay_object_groups pog, per_legislative_data_groups_vl ldg, PAY_FLOW_TASK_INSTANCES pfti, (SELECT (prq.flow_instance_id) flow_instance_id, max(decode(dlvoa.vo_attribute_name,'ObjectGroupName', pay_flow_common_util_pkg.pay_hdl_function (dlr.row_id,dlr.VO_MAPPING_ID,dlvoa.stage_column_name),null)) as ObjectGroupName, max(decode(dlvoa.vo_attribute_name,'LegislativeDataGroupName', pay_flow_common_util_pkg.pay_hdl_function (dlr.row_id,dlr.VO_MAPPING_ID,dlvoa.stage_column_name),null)) as LegislativeDataGroupName, max(to_date(pfpv.FLOW_PARAM_VALUE,'YYYY-MM-DD')) eff_Date FROM pay_requests prq, pay_requests prq_all, hrc_dl_file_rows dlr, HRC_DL_VO_ATTR_MAPS dlvoa, HRC_DL_VO_MAPS dlvo, HRC_DL_BUSINESS_OBJECTS dlbo, PAY_FLOW_PARAM_VALUES pfpv, PAY_FLOW_PARAMETERS pfp WHERE prq.call_id = null and prq_all.flow_instance_id =prq.flow_instance_id and prq.call_type like '%ESS%' and prq_all.call_type like '%ESS%' and dlr.request_id = null and dlr.VO_MAPPING_ID=dlvo.VO_MAPPING_ID and dlr.VO_MAPPING_ID=dlvoa.VO_MAPPING_ID and dlvo.business_object_id=dlbo.business_object_id and dlbo.business_object_vo_FQ_NAME like '%.ObjectGroupVO' and dlvoa.vo_attribute_name in ('ObjectGroupName','LegislativeDataGroupName') and pfpv.BASE_FLOW_PARAMETER_ID=pfp.FLOW_PARAMETER_ID AND pfp.BASE_FLOW_PARAMETER_NAME ='PROCESS_DATE' AND pfpv.FLOW_INSTANCE_ID =prq.flow_instance_id group by prq.flow_instance_id) aaa WHERE pog.base_object_group_name=aaa.ObjectGroupName and ldg.name=aaa.LegislativeDataGroupName and ldg.legislative_data_group_id=pog.legislative_data_group_id and pfti.flow_instance_id=aaa.flow_instance_id )
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
