# PAY_FLOW_SEARCH_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowsearchvl-6943.html#payflowsearchvl-6943](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowsearchvl-6943.html#payflowsearchvl-6943)

## Columns

- KEYWORDSTRING
- FLOW_INSTANCE_ID
- FLOW_NAME
- FLOW_PATTERN
- FLOW_PARAM_PARTIAL
- FLOW_PARAM_FULL
- SUBMITTED_BY
- SUBMITTED_ON
- SCHEDULED_DATE
- FLOW_STATUS
- FLOW_PROGRESS
- PAYROLL
- LDG_NAME
- LEGISLATIVE_DATA_GROUP_ID
- WITH_ERROR
- OVERDUE
- TAKING_LONGER
- NUMBER_OF_OBJECTS
- OBJECT_NAME
- PROCESSING_FLAG
- TO_DO_FLAG
- REQUIRES_ATTENTION_FLAG
- RECENTLY_COMPLETD_FLAG
- MODULE_NAME

## Query

```sql
SELECT FLOW_NAME||': '||FLOW_PATTERN||' by '||SUBMITTED_BY as KeywordString, FLOW_INSTANCE_ID, FLOW_NAME, FLOW_PATTERN, null FLOW_PARAM_PARTIAL, FLOW_PARAM_FULL, SUBMITTED_BY, SUBMITTED_ON, SCHEDULED_DATE, FLOW_STATUS, FLOW_PROGRESS, PAYROLL, LDG_NAME, LEGISLATIVE_DATA_GROUP_ID, null WITH_ERROR, null OVERDUE, null TAKING_LONGER, null NUMBER_OF_OBJECTS, null OBJECT_NAME, null PROCESSING_FLAG, null TO_DO_FLAG, null REQUIRES_ATTENTION_FLAG, null RECENTLY_COMPLETD_FLAG, MODULE_NAME FROM ( select distinct aaa.Flow_Instance_Id,aaa.Flow_Name,aaa.Flow_Pattern, (select distinct listagg( fp.parameter_name||':'|| decode(fp.param_disp_type,'D',fnd_date.date_to_displaydate(to_Date(fpv.flow_param_value,'YYYY-MM-DD')), 'T',fpv.flow_param_value, 'N',fpv.flow_param_value, PAY_FLOW_COMMON_UTIL_PKG.convert_value (to_char(sysdate,'YYYYMMDDHHMISS'),sysdate, aaa.lc_code, aaa.ldg_id, decode(fp.param_disp_type,'LK','LOOKUP','LOV','VO','L','VO','ORA_VALUESET','VALUESET'), fp.param_lookup,fpv.flow_param_value,'Y')) ,' | ') within group (order by param_sequence) from pay_flow_param_values fpv, pay_flow_parameters_vl fp where aaa.flow_instance_id = fpv.flow_instance_id and fp.flow_parameter_id = fpv.base_flow_parameter_id and fpv.flow_param_value is not null and fp.display_flag!='N') Flow_Param_Full, aaa.Submitted_By,aaa.Submitted_On,aaa.Scheduled_Date,aaa.Flow_Status, '('||(select count(distinct pti.base_flow_task_id) from pay_flow_task_instances pti where pti.flow_instance_id = aaa.flow_instance_id and pti.status in ('COMPLETED','SKIPPED'))||'/'|| (select count(distinct pti.base_flow_task_id)-2 from pay_flow_task_instances pti where pti.flow_instance_id = aaa.flow_instance_id )||')' Flow_Progress,Payroll, ldg_name, legislative_data_group_id, MODULE_NAME from ( select distinct pfi.flow_instance_id Flow_Instance_Id,pfi.instance_name Flow_Name,pf.flow_name Flow_Pattern, pu.username Submitted_By,pfi.creation_date Submitted_On,pfi.scheduled_date Scheduled_Date, decode(pfi.status,'CREATED','NOT_STARTED',pfi.status) Flow_Status, /* This needs to stored in the flow instance attributes */ (SELECT max(ppp.payroll_name) FROM pay_requests prq, pay_payroll_actions ppa, pay_all_payrolls_f ppp WHERE prq.FLOW_INSTANCE_ID= pfi.flow_instance_id and ((prq.pay_request_id=ppa.pay_request_id and ppa.payroll_id=ppp.payroll_id) or (ppp.payroll_id = pfi.attribute1 and pfi.attribute1 is not null))) Payroll, ldg.name ldg_name, ldg.legislative_data_group_id ldg_id, ldg.legislative_data_group_id, ldg.legislation_code lc_code, MODULE_NAME from pay_flow_instances pfi, pay_flows_vl pf, per_legislative_data_groups_vl ldg, per_users pu, PAY_CHECKLISTS_vl pc, PAY_CHECKLIST_INSTANCES pci, PAY_CHECKLISTS pfcat, (select max(decode(fup.PREFERENCE_NAME,'CATEGORY',fup.preference_value,null)) ctx_flow_category, max(decode(fup.PREFERENCE_NAME,'SUB_CATEGORY',fup.preference_value,null)) ctx_flow_sub_category, max(decode(fup.PREFERENCE_NAME,'FLOW_PATTERN',fup.preference_value,null)) ctx_flow_pattern, max(decode(fup.PREFERENCE_NAME,'DEFAULT_FLOW',fup.preference_value,null)) ctx_default_flow, fup.MODULE_NAME from FND_USER_PREFERENCES fup where fup.user_name=fnd_session_ns.get_namespace_attr(FND_GLOBAL.session_id,'FND$SECURITY', 'USER_NAME') and fup.MODULE_NAME like 'ORA_DX%' group by fup.MODULE_NAME) session_contexts where pfi.base_flow_id = pf.base_flow_id and (PAY_FLOW_COMMON_UTIL_PKG.check_security(pf.base_flow_id,'PAY_FLOWS','BASE_FLOW_ID','PAY_VIEW_PAYROLL_FLOW_DATA') ='Y' and (PAY_FLOW_COMMON_UTIL_PKG.check_security(pfi.LEGISLATIVE_DATA_GROUP_ID,'PER_LEGISLATIVE_DATA_GROUPS','LEGISLATIVE_DATA_GROUP_ID','PER_CHOOSE_LEGISLATIVE_DATA_GROUP_DATA') ='Y' OR pfi.LEGISLATIVE_DATA_GROUP_ID is null)) and pfcat.base_flow_id = pfi.base_flow_id and nvl(pfcat.category_type,'#')=nvl(session_contexts.ctx_flow_category, nvl(pfcat.category_type,'#')) and nvl(pfcat.sub_category_type,'#')=nvl(session_contexts.ctx_flow_sub_category, nvl(pfcat.sub_category_type,'#')) and pf.base_flow_name=nvl(session_contexts.ctx_flow_pattern,pf.base_flow_name) and ldg.legislative_data_group_id (+) = pfi.legislative_data_group_id and pu.user_id = pfi.instantiated_by and pf.default_flow_flag=nvl(session_contexts.ctx_default_flow,pf.default_flow_flag) and pc.base_checklist_id = pci.base_checklist_id and pci.flow_instance_id = pfi.flow_instance_id and (pc.legislative_data_group_id = ldg.legislative_data_group_id or pc.legislation_code = ldg.legislation_code or (pc.legislative_data_group_id is null and pc.legislation_code is null)) and (pf.legislative_data_group_id = ldg.legislative_data_group_id or pf.legislation_code = ldg.legislation_code or (pf.legislative_data_group_id is null and pf.legislation_code is null)) ) aaa order by Submitted_On desc )
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
