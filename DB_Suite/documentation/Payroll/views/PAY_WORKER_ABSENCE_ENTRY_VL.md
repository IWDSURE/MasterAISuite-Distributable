# PAY_WORKER_ABSENCE_ENTRY_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payworkerabsenceentryvl-6894.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payworkerabsenceentryvl-6894.html)

## Columns

- ABSENCE_ENTRY_INSTANCE_ID
- OBJECT_VERSION_NUMBER
- ABSENCE_INSTANCE_ID
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- ABSENCE_PLAN_NAME
- ABSENCE_ELEMENT_COMPONENT_NAME
- ABSENCE_PLAN_ID
- ABSENCE_ENTRY_TYPE
- ABSENCE_ENTRY_TYPE_DEF_ID
- ABSENCE_ID
- ABSENCE_ENTRY_ID
- OVERRIDING_TIME
- OVERRIDING_UNIT_OF_MEASURE
- PERIODICITY
- ACCRUAL_DATE
- LEAVE_DATE
- OVERRIDING_FACTOR
- OVERRIDING_RATE_NAME
- OVERRIDING_RATE_DEFINITION_ID

## Query

```sql
select pdcc.DIR_CARD_COMP_ID ABSENCE_ENTRY_Instance_id , pdcc.object_version_number, pdcc.PARENT_DIR_CARD_COMP_ID ABSENCE_Instance_ID, pdcc.effective_start_date effective_start_date, pdcc.effective_end_date effective_end_date, (select cdef.BASE_COMPONENT_NAME from (select pdcc1.PARENT_DIR_CARD_COMP_ID from (select DIR_CARD_ID,COMPONENT_SEQUENCE, DIR_CARD_COMP_DEF_ID,DIR_CARD_COMP_ID,PARENT_DIR_CARD_COMP_ID FROM PAY_DIR_CARD_COMPONENTS_F WHERE DIR_CARD_COMP_ID =pdcc.PARENT_DIR_CARD_COMP_ID) pdcc1) pdcc2, PAY_DIR_CARD_COMPONENTS_F pdcc3, Pay_Dir_Card_Comp_Defs_vl cdef where cdef.DIR_CARD_COMP_DEF_ID = pdcc3.DIR_CARD_COMP_DEF_ID and pdcc2.PARENT_DIR_CARD_COMP_ID =pdcc3.DIR_CARD_COMP_ID) as Absence_Plan_Name, (select cdef.BASE_COMPONENT_NAME from (select pdcc1.PARENT_DIR_CARD_COMP_ID from (select DIR_CARD_ID,COMPONENT_SEQUENCE, DIR_CARD_COMP_DEF_ID,DIR_CARD_COMP_ID,PARENT_DIR_CARD_COMP_ID FROM PAY_DIR_CARD_COMPONENTS_F WHERE DIR_CARD_COMP_ID =pdcc.PARENT_DIR_CARD_COMP_ID) pdcc1) pdcc2, PAY_DIR_CARD_COMPONENTS_F pdcc3, Pay_Dir_Card_Comp_Defs_vl cdef where cdef.DIR_CARD_COMP_DEF_ID = pdcc3.DIR_CARD_COMP_DEF_ID and pdcc2.PARENT_DIR_CARD_COMP_ID =pdcc3.DIR_CARD_COMP_ID) as Absence_Element_Component_Name, (select cdef.DIR_CARD_COMP_DEF_ID from (select pdcc1.PARENT_DIR_CARD_COMP_ID from (select DIR_CARD_ID,COMPONENT_SEQUENCE, DIR_CARD_COMP_DEF_ID,DIR_CARD_COMP_ID,PARENT_DIR_CARD_COMP_ID FROM PAY_DIR_CARD_COMPONENTS_F WHERE DIR_CARD_COMP_ID =pdcc.PARENT_DIR_CARD_COMP_ID) pdcc1) pdcc2, PAY_DIR_CARD_COMPONENTS_F pdcc3, Pay_Dir_Card_Comp_Defs_vl cdef where cdef.DIR_CARD_COMP_DEF_ID = pdcc3.DIR_CARD_COMP_DEF_ID and pdcc2.PARENT_DIR_CARD_COMP_ID =pdcc3.DIR_CARD_COMP_ID) as Absence_Plan_Id, pdccd.BASE_COMPONENT_NAME ABSENCE_ENTRY_TYPE, pdccd.DIR_CARD_COMP_DEF_ID ABSENCE_ENTRY_TYPE_DEF_ID, (select CREATOR_ID FROM PAY_DIR_CARD_COMPONENTS_F WHERE DIR_CARD_COMP_ID =pdcc.PARENT_DIR_CARD_COMP_ID) ABSENCE_ID, pdcc.CREATOR_ID ABSENCE_ENTRY_ID, (select pri.value1 from PAY_VALUE_INSTANCES_V pvd, PAY_RANGE_INST_V pri where pvd.source_id = pdcc.DIR_CARD_COMP_ID and pvd.source_type = 'PDCC' and pvd.value_defn_id = pri.value_defn_id and pvd.base_name IN('ORA_DONATION_POOL_UNIT','GLB_ENTITLEMENT_UNIT','GLB_DISCRETIONARY_DISBURSEMENT_UNIT','GLB_FINAL_DISBURSEMENT_UNIT')) Overriding_TIME, (select pvd.UOM from PAY_VALUE_INSTANCES_V pvd, hcm_lookups lk where pvd.source_id = pdcc.DIR_CARD_COMP_ID and pvd.source_type = 'PDCC' and lk.lookup_code=pvd.UOM and lk.lookup_type='PAY_UNITS' and pvd.base_name IN('ORA_DONATION_POOL_UNIT','GLB_ENTITLEMENT_UNIT','GLB_DISCRETIONARY_DISBURSEMENT_UNIT','GLB_FINAL_DISBURSEMENT_UNIT')) Overriding_UNIT_OF_MEASURE, (select pvd.periodicity from PAY_VALUE_INSTANCES_V pvd where pvd.source_id = pdcc.DIR_CARD_COMP_ID and pvd.source_type = 'PDCC' and pvd.base_name IN('ORA_DONATION_POOL_UNIT','GLB_ENTITLEMENT_UNIT','GLB_DISCRETIONARY_DISBURSEMENT_UNIT','GLB_FINAL_DISBURSEMENT_UNIT')) periodicity, (select pri.value1 from PAY_VALUE_INSTANCES_V pvd, PAY_RANGE_INST_V pri where pvd.source_id = pdcc.DIR_CARD_COMP_ID and pvd.source_type = 'PDCC' and pvd.value_defn_id = pri.value_defn_id and pvd.base_name IN('GLB_ENTITLEMENT_ACCRUED_DATE','GLB_DISCRETIONARY_DISBURSEMENT_ACCRUED_DATE','GLB_FINAL_DISBURSEMENT_ACCRUED_DATE')) Accrual_Date, pdcc.effective_start_date LEAVE_DATE, (select pri.value1 from PAY_VALUE_INSTANCES_V pvd, PAY_RANGE_INST_V pri where pvd.source_id = pdcc.DIR_CARD_COMP_ID and pvd.source_type = 'PDCC' and pvd.value_defn_id = pri.value_defn_id and pvd.base_name IN('ORA_DONATION_POOL_FACTOR','GLB_ENTITLEMENT_FACTOR','ORA_DISCRETIONARY_DISBURSEMENT_FACTOR','GLB_DISCRETIONARY_DISBURSEMENT_FACTOR','GLB_FINAL_DISBURSEMENT_FACTOR')) Overriding_FACTOR, (select RDT.NAME from PAY_RATE_DEFINITIONS_F_TL RDT, (select max(pri.value1) RATE_DEFINITION_ID from PAY_VALUE_INSTANCES_V pvd, PAY_RANGE_INST_V pri where pvd.source_id = pdcc.DIR_CARD_COMP_ID and pvd.source_type = 'PDCC' and pvd.value_defn_id = pri.value_defn_id and pvd.base_name IN(pdccd.BASE_COMPONENT_NAME||'_ENTITLEMENT_RATE',pdccd.BASE_COMPONENT_NAME||'_DONATION_POOL_RATE',pdccd.BASE_COMPONENT_NAME||'_DISCRETIONARY_DISBURSEMENT_RATE',pdccd.BASE_COMPONENT_NAME||'_FINAL_DISBURSEMENT_RATE')) RD where RD.RATE_DEFINITION_ID=RDT.RATE_DEFINITION_ID and pdcc.EFFECTIVE_START_DATE >= RDT.EFFECTIVE_START_DATE and pdcc.EFFECTIVE_END_DATE <= RDT.EFFECTIVE_END_DATE and (RDT.LANGUAGE=SYS_CONTEXT('USERENV','LANG'))) Overriding_RATE_NAME, (select pri.value1 from PAY_VALUE_INSTANCES_V pvd, PAY_RANGE_INST_V pri where pvd.source_id = pdcc.DIR_CARD_COMP_ID and pvd.source_type = 'PDCC' and pvd.value_defn_id = pri.value_defn_id and pvd.base_name IN(pdccd.BASE_COMPONENT_NAME||'_ENTITLEMENT_RATE',pdccd.BASE_COMPONENT_NAME||'_DONATION_POOL_RATE',pdccd.BASE_COMPONENT_NAME||'_DISCRETIONARY_DISBURSEMENT_RATE',pdccd.BASE_COMPONENT_NAME||'_FINAL_DISBURSEMENT_RATE')) Overriding_Rate_DEFINITION_Id from PAY_DIR_CARD_COMPONENTS_F pdcc, PAY_DIR_CARD_COMP_DEFS_F pdccd where pdccd.DIR_CARD_COMP_DEF_ID = pdcc.DIR_CARD_COMP_DEF_ID
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
