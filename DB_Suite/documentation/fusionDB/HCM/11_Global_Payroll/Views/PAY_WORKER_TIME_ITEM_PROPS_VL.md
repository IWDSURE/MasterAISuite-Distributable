# PAY_WORKER_TIME_ITEM_PROPS_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payworkertimeitempropsvl-6538.html#payworkertimeitempropsvl-6538](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payworkertimeitempropsvl-6538.html#payworkertimeitempropsvl-6538)

## Columns

- NAME
- PROPERTY_VALUE_ID
- PAYROLL_TIME_ITEM_ID
- PROPERTY_BASE_NAME
- PROPERTY_NAME
- PROPERTY_VALUE
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- TIME_CARD_INSTANCE_ID
- PARENT_VALUE_DEFN_ID
- VO_NAME1
- VO_NAME2
- VO_NAME3
- DIR_OVERRIDE_USAGE_ID
- OBJECT_VERSION_NUMBER

## Query

```sql
select props.Property_name name , props.PROPERTY_VALUE_ID, props.PAYROLL_TIME_ITEM_ID, props.PROPERTY_BASE_NAME PROPERTY_BASE_NAME, props.Property_name PROPERTY_NAME, props.PROPERTY_VALUE, props.EFFECTIVE_START_DATE, props.EFFECTIVE_END_DATE, props.TIME_CARD_INSTANCE_ID, props.PARENT_VALUE_DEFN_ID, props.VO_NAME1,props.VO_NAME2,props.VO_NAME3, props.DIR_OVERRIDE_USAGE_ID, props.object_version_number from (select pri.RANGE_ITEM_ID Property_value_id, pri.object_version_number, pdc.dir_card_comp_id Payroll_Time_Item_Id, pvd1.name Property_name, pvd.base_name Property_base_name, pri.value1 Property_value, pri.effective_start_date, pri.effective_end_date, pdc.PARENT_DIR_CARD_COMP_ID Time_Card_Instance_ID, pvd.PARENT_VALUE_DEFN_ID, pvd.DIR_OVERRIDE_USAGE_ID, pvd1.VO_NAME1, pvd1.VO_NAME2, pvd1.VO_NAME3 from pay_dir_card_components_f pdc, PAY_VALUE_INSTANCES_V pvd, PAY_RANGE_INST_V pri, PAY_VALUE_DEFS_VL pvd1 where pdc.dir_card_comp_id = pvd.source_id and pvd.PARENT_VALUE_DEFN_ID=pvd1.value_defn_id and pvd.source_type = 'PDCC' and pvd.value_defn_id = pri.value_defn_id and pvd.base_name not like '%_RATE_AMOUNT' and pvd.base_name not like '%_PAYMENT_RATE' and pvd.base_name != 'Time Unit' and pvd.base_name != 'Accrual Unit' and pvd.base_name != 'Leave Unit' and pvd.base_name != 'Leave Factor' and pvd.base_name not like '%_TIME_FACTOR' union all select segments.element_entry_id Property_value_id, pdc.object_version_number, pdc.dir_card_comp_id time_type_id, segments.segment_name Property_name, null Property_base_name, segments.segment_value Property_value, pee.effective_start_date, pee.effective_end_date, pdc.PARENT_DIR_CARD_COMP_ID Time_Card_Instance_ID, null PARENT_VALUE_DEFN_ID, null DIR_OVERRIDE_USAGE_ID, null VO_NAME1, null VO_NAME2, null VO_NAME3 from pay_dir_card_components_f pdc, pay_element_entries_f pee, ( select ffs.segment_name, pca.source_id element_entry_id, case when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT1' then segment1 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT2' then segment2 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT3' then segment3 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT4' then segment4 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT5' then segment5 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT6' then segment6 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT7' then segment7 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT8' then segment8 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT9' then segment9 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT10' then segment10 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT11' then segment11 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT12' then segment12 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT13' then segment13 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT14' then segment14 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT15' then segment15 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT16' then segment16 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT17' then segment17 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT18' then segment18 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT19' then segment19 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT20' then segment20 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT21' then segment21 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT22' then segment22 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT23' then segment23 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT24' then segment24 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT25' then segment25 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT26' then segment26 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT27' then segment27 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT28' then segment28 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT29' then segment29 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT30' then segment30 end segment_value from PAY_COST_ALLOC_ACCOUNTS pcaa, PAY_COST_ALLOCATIONS_F pca, FND_ID_FLEX_SEGMENTS ffs where pcaa.COST_ALLOCATION_RECORD_ID = pca.COST_ALLOCATION_RECORD_ID and pcaa.ID_FLEX_NUM = ffs.ID_FLEX_NUM and pca.source_type = 'EE1' and ffs.ID_FLEX_CODE='COST' ) segments where segments.segment_value is not null and pee.element_entry_id = segments.element_entry_id and pee.creator_id = pdc.dir_card_comp_id union all select segments.card_comp_id Property_value_id, pdc.object_version_number, pdc.dir_card_comp_id time_type_id, segments.segment_name Property_name, null Property_base_name, segments.segment_value Property_value, pdc.effective_start_date, pdc.effective_end_date, pdc.PARENT_DIR_CARD_COMP_ID Time_Card_Instance_ID, null PARENT_VALUE_DEFN_ID, null DIR_OVERRIDE_USAGE_ID, null VO_NAME1, null VO_NAME2, null VO_NAME3 from pay_dir_card_components_f pdc, ( select ffs.segment_name, pca.source_id card_comp_id, case when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT1' then segment1 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT2' then segment2 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT3' then segment3 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT4' then segment4 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT5' then segment5 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT6' then segment6 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT7' then segment7 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT8' then segment8 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT9' then segment9 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT10' then segment10 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT11' then segment11 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT12' then segment12 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT13' then segment13 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT14' then segment14 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT15' then segment15 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT16' then segment16 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT17' then segment17 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT18' then segment18 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT19' then segment19 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT20' then segment20 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT21' then segment21 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT22' then segment22 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT23' then segment23 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT24' then segment24 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT25' then segment25 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT26' then segment26 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT27' then segment27 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT28' then segment28 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT29' then segment29 when ffs.APPLICATION_COLUMN_NAME = 'SEGMENT30' then segment30 end segment_value from PAY_COST_ALLOC_ACCOUNTS pcaa, PAY_COST_ALLOCATIONS_F pca, FND_ID_FLEX_SEGMENTS ffs where pcaa.COST_ALLOCATION_RECORD_ID = pca.COST_ALLOCATION_RECORD_ID and pcaa.ID_FLEX_NUM = ffs.ID_FLEX_NUM and pca.source_type = 'DCC' and ffs.ID_FLEX_CODE='COST' ) segments where segments.segment_value is not null and segments.card_comp_id = pdc.dir_card_comp_id ) props
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
