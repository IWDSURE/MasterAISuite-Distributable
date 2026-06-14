# PAY_WORKER_TIME_ITEM_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payworkertimeitemvl-7704.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payworkertimeitemvl-7704.html)

## Columns

- PAYROLL_TIME_ITEM_ID
- OBJECT_VERSION_NUMBER
- CREATOR_ID
- CREATOR_TYPE
- TIME_CARD_INSTANCE_ID
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- TIME_TYPE
- TIME_TYPE_NAME
- TIME_TYPE_DEF_ID
- TIME_CARD_ID
- TIME_CARD_SEQUENCE
- TIME_ENTRY_ID
- TIME_ENTRY_SEQUENCE
- TIME
- UNIT_OF_MEASURE
- RATE_VALUE
- PERIODICITY
- FACTOR
- RATE_NAME
- RATE_DEFINITION_ID
- SEGMENT1
- SEGMENT2
- SEGMENT3
- SEGMENT4
- SEGMENT5
- SEGMENT6
- SEGMENT7
- SEGMENT8
- SEGMENT9
- SEGMENT10
- SEGMENT11
- SEGMENT12
- SEGMENT13
- SEGMENT14
- SEGMENT15
- SEGMENT16
- SEGMENT17
- SEGMENT18
- SEGMENT19
- SEGMENT20
- SEGMENT21
- SEGMENT22
- SEGMENT23
- SEGMENT24
- SEGMENT25
- SEGMENT26
- SEGMENT27
- SEGMENT28
- SEGMENT29
- SEGMENT30

## Query

```sql
select pdcc.DIR_CARD_COMP_ID Payroll_Time_Item_id , pdcc.object_version_number, pdcc.creator_id, pdcc.creator_type, pdcc.PARENT_DIR_CARD_COMP_ID Time_Card_Instance_ID, pdcc.effective_start_date effective_start_date, pdcc.effective_end_date effective_end_date, pdccd.BASE_COMPONENT_NAME TIME_TYPE, pdccd.COMPONENT_NAME TIME_TYPE_NAME, pdccd.DIR_CARD_COMP_DEF_ID TIME_TYPE_DEF_ID, (SELECT pdcc1.CREATOR_ID FROM (select DIR_CARD_ID,COMPONENT_SEQUENCE, DIR_CARD_COMP_DEF_ID,DIR_CARD_COMP_ID,PARENT_DIR_CARD_COMP_ID,CREATOR_ID FROM PAY_DIR_CARD_COMPONENTS_F WHERE DIR_CARD_COMP_ID =pdcc.PARENT_DIR_CARD_COMP_ID) pdcc1, PAY_DIR_CARDS_F pdc1 where pdcc1.DIR_CARD_COMP_ID = pdcc.PARENT_DIR_CARD_COMP_ID and pdcc1.DIR_CARD_ID=pdc1.DIR_CARD_ID START WITH pdcc1.PARENT_DIR_CARD_COMP_ID IS NULL CONNECT BY PRIOR pdcc1.DIR_CARD_COMP_ID = pdcc1.PARENT_DIR_CARD_COMP_ID ) TIME_CARD_ID, (SELECT pdcc1.COMPONENT_SEQUENCE FROM (select DIR_CARD_ID,COMPONENT_SEQUENCE, DIR_CARD_COMP_DEF_ID,DIR_CARD_COMP_ID,PARENT_DIR_CARD_COMP_ID FROM PAY_DIR_CARD_COMPONENTS_F WHERE DIR_CARD_COMP_ID =pdcc.PARENT_DIR_CARD_COMP_ID) pdcc1, PAY_DIR_CARDS_F pdc1 where pdcc1.DIR_CARD_COMP_ID = pdcc.PARENT_DIR_CARD_COMP_ID and pdcc1.DIR_CARD_ID=pdc1.DIR_CARD_ID START WITH pdcc1.PARENT_DIR_CARD_COMP_ID IS NULL CONNECT BY PRIOR pdcc1.DIR_CARD_COMP_ID = pdcc1.PARENT_DIR_CARD_COMP_ID ) TIME_CARD_SEQUENCE, pdcc.CREATOR_ID TIME_ENTRY_ID, pdcc.COMPONENT_SEQUENCE TIME_ENTRY_SEQUENCE, (select pri.value1 from PAY_VALUE_INSTANCES_V pvd, PAY_RANGE_INST_V pri where pvd.source_id = pdcc.DIR_CARD_COMP_ID and pvd.source_type = 'PDCC' and pvd.value_defn_id = pri.value_defn_id and pvd.base_name = 'Time Unit') TIME, (select pvd.UOM from PAY_VALUE_INSTANCES_V pvd, hcm_lookups lk where pvd.source_id = pdcc.DIR_CARD_COMP_ID and pvd.source_type = 'PDCC' and lk.lookup_code=pvd.UOM and lk.lookup_type='PAY_UNITS' and pvd.base_name = 'Time Unit') UNIT_OF_MEASURE, (select pri.value1 from PAY_VALUE_INSTANCES_V pvd, PAY_RANGE_INST_V pri where pvd.source_id = pdcc.DIR_CARD_COMP_ID and pvd.source_type = 'PDCC' and pvd.value_defn_id = pri.value_defn_id and pvd.base_name = pdccd.BASE_COMPONENT_NAME||'_RATE_AMOUNT') RATE_VALUE, (select pvd.periodicity from PAY_VALUE_INSTANCES_V pvd where pvd.source_id = pdcc.DIR_CARD_COMP_ID and pvd.source_type = 'PDCC' and pvd.base_name = pdccd.BASE_COMPONENT_NAME||'_RATE_AMOUNT') periodicity, (select pri.value1 from PAY_VALUE_INSTANCES_V pvd, PAY_RANGE_INST_V pri where pvd.source_id = pdcc.DIR_CARD_COMP_ID and pvd.source_type = 'PDCC' and pvd.value_defn_id = pri.value_defn_id and pvd.base_name = pdccd.BASE_COMPONENT_NAME||'_TIME_FACTOR') FACTOR, (select RDT.NAME from PAY_RATE_DEFINITIONS_F_TL RDT, (select max(pri.value1) RATE_DEFINITION_ID from PAY_VALUE_INSTANCES_V pvd, PAY_RANGE_INST_V pri where pvd.source_id = pdcc.DIR_CARD_COMP_ID and pvd.source_type = 'PDCC' and pvd.value_defn_id = pri.value_defn_id and pvd.base_name = pdccd.BASE_COMPONENT_NAME||'_PAYMENT_RATE') RD where RD.RATE_DEFINITION_ID=RDT.RATE_DEFINITION_ID and (RDT.LANGUAGE=SYS_CONTEXT('USERENV','LANG'))) RATE_NAME, (select pri.value1 from PAY_VALUE_INSTANCES_V pvd, PAY_RANGE_INST_V pri where pvd.source_id = pdcc.DIR_CARD_COMP_ID and pvd.source_type = 'PDCC' and pvd.value_defn_id = pri.value_defn_id and pvd.base_name = pdccd.BASE_COMPONENT_NAME||'_PAYMENT_RATE') RATE_DEFINITION_ID, null segment1, null segment2, null segment3, null segment4, null segment5, null segment6, null segment7, null segment8, null segment9, null segment10, null segment11, null segment12, null segment13, null segment14, null segment15, null segment16, null segment17, null segment18, null segment19, null segment20, null segment21, null segment22, null segment23, null segment24, null segment25, null segment26, null segment27, null segment28, null segment29, null segment30 from PAY_DIR_CARD_COMPONENTS_F pdcc, PAY_DIR_CARD_COMP_DEFS_VL pdccd where pdccd.DIR_CARD_COMP_DEF_ID = pdcc.DIR_CARD_COMP_DEF_ID
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
