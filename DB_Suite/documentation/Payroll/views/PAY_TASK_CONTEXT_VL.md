# PAY_TASK_CONTEXT_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytaskcontextvl-7183.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytaskcontextvl-7183.html)

## Columns

- MODULE_NAME
- FLOW_NAME
- FLOW_PATTERN
- TASK_NAME
- TASK_DESCRIPTION
- CATEGORY
- SUB_CATEGORY
- OWNER
- DUE_DATE
- LAST_UPDATED_DATE
- NOTIFICATION_DETAIL
- PARAMETERS
- EXTRACT_BASED_FLAG
- DELIVERY_OPTION
- REPORT_CATEGORY
- CHANGE_ONLY_MODE
- CRITERIA_DEFINED
- FLOW_INSTANCE_ID
- TASK_INSTANCE_ID

## Query

```sql
select aaa.module_name, aaa.flow_Name,aaa.Flow_pattern, aaa.TASK_NAME, aaa.TASK_description TASK_description, aaa.Cat_CK_Instance_Name Category, aaa.Sub_Cat_CK_Instance_Name Sub_category, aaa.Submitted_By Owner, aaa.Due_Date due_date,aaa.region_last_updated_date last_updated_date, (select 'Overdue '||DECODE(pck.OVERDUE_NOTIF_FLAG,'Y','Yes','N','No',pck.OVERDUE_NOTIF_FLAG)||' | Error '||DECODE(pck.ERROR_NOTIF_FLAG,'Y','Yes','N','No',pck.ERROR_NOTIF_FLAG)||' | Warning '||DECODE(pck.WARNING_NOTIF_FLAG,'Y','Yes','N','No',pck.WARNING_NOTIF_FLAG) from pay_flow_tasks_vl pck where aaa.base_flow_task_id = pck.flow_task_id) Notification_Detail, (select distinct listagg( fp.parameter_name||':'|| decode(fp.param_disp_type ,'D',to_char(to_Date(fpv.flow_task_param_value,'YYYY-MM-DD HH24:MI:SS'),'DD-MM-YYYY'), 'T',fpv.flow_task_param_value, 'N',fpv.flow_task_param_value, PAY_FLOW_COMMON_UTIL_PKG.convert_value (to_char(sysdate,'YYYYMMDDHHMISS'),sysdate, bbb.lc_code, bbb.ldg_id, decode(fp.param_disp_type,'LK','LOOKUP','LOV','VO','L','VO','ORA_VALUESET','VALUESET'), fp.param_lookup,fpv.flow_task_param_value,'Y')) ,' | ') within group (order by param_sequence) from PAY_FLOW_TASK_PARAM_VALS fpv, PAY_FLOW_TASK_PARAMETERS_VL fp where aaa.task_instance_id = fpv.flow_task_instance_id and fp.base_flow_task_param_id = fpv.base_flow_task_param_id and fpv.flow_task_param_value is not null and fp.DISPLAY_FLAG != 'N' and not exists (select null from PAY_FLOW_TASK_PARAM_VALS ddd where ddd.flow_task_instance_id = fpv.flow_task_instance_id and ddd.action_sequence > fpv.action_sequence) ) Parameters, decode(aaa.Extract_Type,null,null,'Y') Extract_based_flag, ( select max(ext.delivery_type) from per_ext_delivery_options_vl ext, pay_rep_cat_components prcc where aaa.report_category_id=prcc.REPORT_CATEGORY_ID and prcc.style_sheet_id=ext.ext_delivery_option_id) Delivery_option, (select max(prd.report_type) from PAY_REPORT_CATEGORIES prg, PAY_REPORT_DEFINITIONS prd, PER_EXT_DEFINITIONS_VL ext, PER_EXT_TYPES_VL extt where aaa.report_category_id = prg.report_category_id and prg.REPORT_GROUP_ID=prd.REPORT_GROUP_ID and prd.EXT_DEFINITION_ID=ext.EXT_DEFINITION_ID and extt.EXT_TYPE_CODE=ext.EXT_TYPE_CODE) report_category, decode(aaa.Extract_Type,null,null,'No') change_only_mode, decode(aaa.Extract_Type,null,null,'Yes') Criteria_defined, aaa.flow_instance_id,aaa.task_instance_id from PAY_task_STATUS_VL aaa, pay_flow_status_basic_vl bbb where aaa.task_instance_id=bbb.task_instance_id and aaa.flow_instance_id=bbb.flow_instance_id and aaa.module_name=bbb.module_name
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
