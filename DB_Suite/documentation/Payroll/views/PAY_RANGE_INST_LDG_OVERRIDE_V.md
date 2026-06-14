# PAY_RANGE_INST_LDG_OVERRIDE_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrangeinstldgoverridev-3568.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payrangeinstldgoverridev-3568.html)

## Columns

- RANGE_TYPE
- RANGE_DEF_ID
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- VALUE_DEFN_ID
- LOW_VALUE
- HIGH_VALUE
- CALC_TYPE_ID
- VALUE1
- VALUE2
- VALUE3
- ENTERPRISE_ID
- LEGISLATION_CODE
- LEGISLATIVE_DATA_GROUP_ID
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- LAST_UPDATED_BY
- MODULE_ID
- SEED_STATUS
- SGUID
- VBC_VALUE_TEXT
- TYPE
- VD_SOURCE_ID
- VD_SOURCE_ID_RANK
- VD_LEGISLATIVE_DATA_GROUP_ID
- VD_PARENT_VALUE_DEFN_ID

## Query

```sql
SELECT "RANGE_TYPE","RANGE_DEF_ID","EFFECTIVE_START_DATE","EFFECTIVE_END_DATE","VALUE_DEFN_ID","LOW_VALUE","HIGH_VALUE","CALC_TYPE_ID","VALUE1","VALUE2","VALUE3","ENTERPRISE_ID","LEGISLATION_CODE","LEGISLATIVE_DATA_GROUP_ID","OBJECT_VERSION_NUMBER","CREATED_BY","CREATION_DATE","LAST_UPDATE_DATE","LAST_UPDATE_LOGIN","LAST_UPDATED_BY","MODULE_ID","SEED_STATUS","SGUID","VBC_VALUE_TEXT","TYPE","VD_SOURCE_ID","VD_SOURCE_ID_RANK","VD_LEGISLATIVE_DATA_GROUP_ID","VD_PARENT_VALUE_DEFN_ID" FROM ( SELECT 'INST' range_type, ri.range_inst_id AS range_def_id, ri.effective_start_date, ri.effective_end_date, vi.parent_value_defn_id AS value_defn_id, ri.low_value, ri.high_value, ri.calc_type_id, ri.value1, ri.value2, ri.value3, ri.enterprise_id, ri.legislation_code, ri.legislative_data_group_id, 1 as object_version_number, 'ldg_override' as created_by, sysdate as creation_date, sysdate as last_update_date, '-1' as last_update_login, 'ldg_override' as last_updated_by, NULL AS module_id, NULL AS seed_status, NULL AS sguid, NULL AS vbc_value_text, ct.type, vi.source_id as vd_source_id, rank() over (partition by vi.parent_value_defn_id,vi.legislative_data_group_id order by vi.source_id asc) as vd_source_id_rank, vi.legislative_data_group_id as vd_legislative_data_group_id, vi.parent_value_defn_id as vd_parent_value_defn_id FROM pay_range_insts_f ri, pay_calc_types ct, pay_value_insts_f vi, fusion.pay_dir_card_components_f cc, fusion.pay_dir_cards_f c WHERE ri.calc_type_id = ct.calc_type_id (+) AND ri.value_inst_id = vi.value_inst_id AND vi.source_type = 'PDCC' AND vi.source_id = cc.dir_card_comp_id AND cc.dir_card_id = c.dir_card_id AND c.source_type = 'LDG')
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
