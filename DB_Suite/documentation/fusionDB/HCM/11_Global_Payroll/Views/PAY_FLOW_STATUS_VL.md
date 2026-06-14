# PAY_FLOW_STATUS_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowstatusvl-4424.html#payflowstatusvl-4424](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowstatusvl-4424.html#payflowstatusvl-4424)

## Columns

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
- WITH_ERROR
- OVERDUE
- TAKING_LONGER
- NUMBER_OF_OBJECTS
- OBJECT_NAME
- STATUS
- PROCESSING_FLAG
- TO_DO_FLAG
- REQUIRES_ATTENTION_FLAG
- RECENTLY_COMPLETD_FLAG
- PAYROLL
- LOCATION
- TRU
- PSU
- EXTRACT_TYPE
- EXTRACT_GROUP
- EXTRACT_AREA
- SUMMARY_TYPE
- SUMMARY_BREAKDOWN
- FLOW_DESC
- SCHEDULE_END_DATE
- RECURRING_FLAG
- RECUR_SCH_FORMULA_ID
- RECUR_TIME_COMPONENT
- RECUR_SCH_TIME_DEF_ID
- REGION_LAST_UPDATED_DATE
- PAGE_LAST_UPDATED_DATE

## Query

```sql
select Flow_Instance_Id,Flow_Name,Flow_Pattern,Flow_Param_Partial,Flow_Param_Full,Submitted_By,Submitted_On, Scheduled_Date,Flow_Status,Flow_Progress,With_Error,Overdue,Taking_Longer,Number_of_Objects,decode(Number_of_Objects,null,null,object_name) Object_Name, status, Processing_flag,to_do_flag,Requires_attention_flag,Recently_completd_flag,Payroll ,Location, TRU,PSU,Extract_Type,Extract_Group,Extract_Area , summary_type,summary_breakdown,flow_desc, SCHEDULE_END_DATE,RECURRING_FLAG,RECUR_SCH_FORMULA_ID,RECUR_TIME_COMPONENT,RECUR_SCH_TIME_DEF_ID, sysdate region_last_updated_date, sysdate page_last_updated_date from ( select distinct aaa.summary_type,aaa.summary_breakdown, aaa.Flow_Instance_Id,aaa.Flow_Name,aaa.Flow_Pattern,aaa.flow_desc, aaa.SCHEDULE_END_DATE,aaa.RECURRING_FLAG,aaa.RECUR_SCH_FORMULA_ID,aaa.RECUR_TIME_COMPONENT,aaa.RECUR_SCH_TIME_DEF_ID, null Flow_Param_Partial, (select distinct listagg( fp.parameter_name||':'|| decode(fp.param_disp_type,'D',fnd_date.date_to_displaydate(to_Date(fpv.flow_param_value,'YYYY-MM-DD')), 'T',fpv.flow_param_value, 'N',fpv.flow_param_value, PAY_FLOW_COMMON_UTIL_PKG.convert_value (to_char(sysdate,'YYYYMMDDHHMISS'),sysdate, aaa.lc_code, aaa.ldg_id, decode(fp.param_disp_type,'LK','LOOKUP','LOV','VO','L','VO','ORA_VALUESET','VALUESET'), fp.param_lookup,fpv.flow_param_value,'Y')) ,' | ') within group (order by param_sequence) from pay_flow_param_values fpv, pay_flow_parameters_vl fp where aaa.flow_instance_id = fpv.flow_instance_id and fp.flow_parameter_id = fpv.base_flow_parameter_id and fpv.flow_param_value is not null and fp.display_flag!='N') Flow_Param_Full, aaa.Submitted_By,aaa.Submitted_On,aaa.Scheduled_Date,aaa.Flow_Status, '('||(select count(distinct pti.base_flow_task_id) from pay_flow_task_instances pti where pti.flow_instance_id = aaa.flow_instance_id and pti.status in ('COMPLETED','SKIPPED'))||'/'|| (select count(distinct pti.base_flow_task_id)-2 from pay_flow_task_instances pti where pti.flow_instance_id = aaa.flow_instance_id )||')' Flow_Progress, aaa.With_Error,aaa.Overdue,aaa.Taking_Longer, (select max(count(*)) from pay_payroll_rel_actions pra, pay_payroll_actions ppa, pay_requests prq, pay_object_actions poa, pay_temp_object_actions pta, pay_flow_task_instances pti where pti.flow_instance_id = aaa.flow_instance_id and prq.flow_task_instance_id = pti.flow_task_instance_id and prq.pay_request_id = ppa.pay_request_id and ppa.payroll_action_id = pra.payroll_action_id (+) and ppa.payroll_action_id = poa.payroll_action_id (+) and ppa.payroll_action_id = pta.payroll_action_id (+) group by ppa.payroll_action_id) Number_of_Objects,'Records' Object_Name, null Processing_flag,null to_do_flag,null Requires_attention_flag,null Recently_completd_flag, aaa.ldg_name ldg,aaa.ldg_id,aaa.lc_code, aaa.status,aaa.status_code, aaa.Payroll,aaa.Location,aaa.TRU,aaa.PSU,aaa.Extract_Area,aaa.Extract_Group,aaa.Extract_type,aaa.flow_status_meaning from pay_flow_status_basic_vl aaa ) order by Submitted_On desc
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
