# PAY_WORKER_ABSENCE_PROPS_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payworkerabsencepropsvl-5623.html#payworkerabsencepropsvl-5623](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payworkerabsencepropsvl-5623.html#payworkerabsencepropsvl-5623)

## Columns

- PROPERTY_VALUE_ID
- OBJECT_VERSION_NUMBER
- ABSENCE_INSTANCE_ID
- ABSENCE_PLAN_NAME
- ABSENCE_ELEMENT_COMPONENT_NAME
- ABSENCE_PLAN_ID
- PROPERTY_NAME
- PROPERTY_VALUE
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- PARENT_VALUE_DEFN_ID
- VALUE_DEFN_ID
- DIR_OVERRIDE_USAGE_ID

## Query

```sql
select pri.RANGE_ITEM_ID Property_value_id, pri.object_version_number, pdc.dir_card_comp_id ABSENCE_Instance_Id, (select cdef.BASE_COMPONENT_NAME from (select pdcc1.PARENT_DIR_CARD_COMP_ID from (select DIR_CARD_ID,COMPONENT_SEQUENCE, DIR_CARD_COMP_DEF_ID,DIR_CARD_COMP_ID,PARENT_DIR_CARD_COMP_ID FROM PAY_DIR_CARD_COMPONENTS_F WHERE DIR_CARD_COMP_ID =pdc.PARENT_DIR_CARD_COMP_ID) pdcc1) pdcc2, PAY_DIR_CARD_COMPONENTS_F pdcc3, Pay_Dir_Card_Comp_Defs_vl cdef where cdef.DIR_CARD_COMP_DEF_ID = pdcc3.DIR_CARD_COMP_DEF_ID and pdcc2.PARENT_DIR_CARD_COMP_ID =pdcc3.DIR_CARD_COMP_ID) Absence_Plan_Name, (select cdef.BASE_COMPONENT_NAME from (select pdcc1.PARENT_DIR_CARD_COMP_ID from (select DIR_CARD_ID,COMPONENT_SEQUENCE, DIR_CARD_COMP_DEF_ID,DIR_CARD_COMP_ID,PARENT_DIR_CARD_COMP_ID FROM PAY_DIR_CARD_COMPONENTS_F WHERE DIR_CARD_COMP_ID =pdc.PARENT_DIR_CARD_COMP_ID) pdcc1) pdcc2, PAY_DIR_CARD_COMPONENTS_F pdcc3, Pay_Dir_Card_Comp_Defs_vl cdef where cdef.DIR_CARD_COMP_DEF_ID = pdcc3.DIR_CARD_COMP_DEF_ID and pdcc2.PARENT_DIR_CARD_COMP_ID =pdcc3.DIR_CARD_COMP_ID) Absence_Element_Component_Name, (select cdef.DIR_CARD_COMP_DEF_ID from (select pdcc1.PARENT_DIR_CARD_COMP_ID from (select DIR_CARD_ID,COMPONENT_SEQUENCE, DIR_CARD_COMP_DEF_ID,DIR_CARD_COMP_ID,PARENT_DIR_CARD_COMP_ID FROM PAY_DIR_CARD_COMPONENTS_F WHERE DIR_CARD_COMP_ID =pdc.PARENT_DIR_CARD_COMP_ID) pdcc1) pdcc2, PAY_DIR_CARD_COMPONENTS_F pdcc3, Pay_Dir_Card_Comp_Defs_vl cdef where cdef.DIR_CARD_COMP_DEF_ID = pdcc3.DIR_CARD_COMP_DEF_ID and pdcc2.PARENT_DIR_CARD_COMP_ID =pdcc3.DIR_CARD_COMP_ID) Absence_Plan_Id, pvd.base_name Property_name, pri.value1 Property_value, pri.effective_start_date, pri.effective_end_date, pvd.PARENT_VALUE_DEFN_ID, pvd.VALUE_DEFN_ID, pvd.DIR_OVERRIDE_USAGE_ID from pay_dir_card_components_f pdc, PAY_VALUE_INSTANCES_V pvd, PAY_RANGE_INST_V pri where pdc.dir_card_comp_id = pvd.source_id and pvd.source_type = 'PDCC' and pvd.value_defn_id = pri.value_defn_id and pvd.base_name not like '%_BOOKED_LIABILITY_RATE' and pvd.base_name not like '%_ENTITLEMENT_RATE' and pvd.base_name not like '%_DISCRETIONARY_DISBURSEMENT_RATE' and pvd.base_name not like '%_FINAL_DISBURSEMENT_RATE' and pvd.base_name != 'GLB_ACCRUAL_UNIT' and pvd.base_name != 'GLB_ENTITLEMENT_UNIT' and pvd.base_name != 'GLB_DISCRETIONARY_DISBURSEMENT_UNIT' and pvd.base_name != 'GLB_FINAL_DISBURSEMENT_UNIT' and pvd.base_name != 'GLB_ENTITLEMENT_FACTOR' and pvd.base_name != 'GLB_DISCRETIONARY_DISBURSEMENT_FACTOR' and pvd.base_name != 'ORA_DISCRETIONARY_DISBURSEMENT_FACTOR' and pvd.base_name != 'GLB_FINAL_DISBURSEMENT_FACTOR' and pvd.base_name != 'GLB_CALCULATION_DATE' and pvd.base_name != 'GLB_ENTITLEMENT_ACCRUED_DATE' and pvd.base_name != 'GLB_DISCRETIONARY_DISBURSEMENT_ACCRUED_DATE' and pvd.base_name != 'GLB_FINAL_DISBURSEMENT_ACCRUED_DATE' and pvd.base_name not like '%_DONATION_POOL_RATE' and pvd.base_name != 'ORA_DONATION_POOL_UNIT' and pvd.base_name != 'ORA_DONATION_POOL_FACTOR' union all select segments.card_comp_id Property_value_id, pdc.object_version_number, pdc.dir_card_comp_id ABSENCE_Instance_Id, null Absence_Plan_Name, null Absence_Element_Component_Name, null Absence_Plan_Id, segments.segment_name Property_name, segments.segment_value Property_value, pdc.effective_start_date, pdc.effective_end_date, null PARENT_VALUE_DEFN_ID, null VALUE_DEFN_ID, null DIR_OVERRIDE_USAGE_ID from pay_dir_card_components_f pdc, ( select ffs.segment_name, pca.source_id card_comp_id, case when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT1' then segment1 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT2' then segment2 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT3' then segment3 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT4' then segment4 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT5' then segment5 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT6' then segment6 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT7' then segment7 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT8' then segment8 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT9' then segment9 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT10' then segment10 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT11' then segment11 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT12' then segment12 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT13' then segment13 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT14' then segment14 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT15' then segment15 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT16' then segment16 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT17' then segment17 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT18' then segment18 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT19' then segment19 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT20' then segment20 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT21' then segment21 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT22' then segment22 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT23' then segment23 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT24' then segment24 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT25' then segment25 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT26' then segment26 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT27' then segment27 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT28' then segment28 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT29' then segment29 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT30' then segment30 end segment_value from PAY_COST_ALLOC_ACCOUNTS pcaa, PAY_COST_ALLOCATIONS_F pca, FND_ID_FLEX_SEGMENTS ffs where pcaa.COST_ALLOCATION_RECORD_ID = pca.COST_ALLOCATION_RECORD_ID and pcaa.ID_FLEX_NUM = ffs.ID_FLEX_NUM and pca.source_type = 'DCC' and ffs.ID_FLEX_CODE='COST' ) segments where segments.segment_value is not null and segments.card_comp_id = pdc.dir_card_comp_id
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
