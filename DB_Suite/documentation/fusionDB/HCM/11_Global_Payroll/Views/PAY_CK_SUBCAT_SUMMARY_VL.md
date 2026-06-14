# PAY_CK_SUBCAT_SUMMARY_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycksubcatsummaryvl-8814.html#paycksubcatsummaryvl-8814](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycksubcatsummaryvl-8814.html#paycksubcatsummaryvl-8814)

## Columns

- FLOW_INSTANCE_ID
- FLOW_NAME
- CHECKLIST_TYPE
- CHECKLIST_SUBCATEGORY
- CHECKLIST_SUBCATEGORY_ID
- SUBCATEGORY_STATUS
- PRNT_CHKLST_INST_ID
- FLOW_PROGRESS
- SUBCATEGORY_PROGRESS
- ACTION1
- ACTION2

## Query

```sql
select pfi.Flow_Instance_Id,pfi.instance_name as FLOW_NAME,ck.checklist_type,ck.checklist_name as CHECKLIST_SUBCATEGORY, ci.checklist_instance_id as CHECKLIST_SUBCATEGORY_ID,ci.status as SUBCATEGORY_STATUS, ci.prnt_chklst_inst_id, '('||(select count(distinct pti.base_flow_task_id) from pay_flow_task_instances pti where pti.flow_instance_id = pfi.flow_instance_id and pti.status in ('COMPLETED','SKIPPED'))||'/'|| (select count(distinct pti.base_flow_task_id)-2 from pay_flow_task_instances pti where pti.flow_instance_id = pfi.flow_instance_id )||')' Flow_Progress, '('||(select count(distinct pti.base_flow_task_id) from pay_flow_task_instances pti where pti.flow_task_instance_id in ( SELECT flow_task_instance_id FROM pay_checklist_instances ci1 where ci.checklist_instance_id= ci1.prnt_chklst_inst_id) and pti.status in ('COMPLETED','SKIPPED'))||'/'|| (select count(distinct pti.base_flow_task_id) from pay_flow_task_instances pti where pti.flow_task_instance_id in ( SELECT flow_task_instance_id FROM pay_checklist_instances ci1 where ci.checklist_instance_id= ci1.prnt_chklst_inst_id))||')' SUBCATEGORY_PROGRESS, null as Action1 , null as Action2 from pay_flow_instances pfi, pay_checklist_instances ci, pay_checklists_vl ck where ci.Flow_Instance_Id =pfi.Flow_Instance_Id and ci.base_checklist_id = ck.checklist_id and ck.checklist_type IN ('SUBCAT_CHECKLIST')
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
