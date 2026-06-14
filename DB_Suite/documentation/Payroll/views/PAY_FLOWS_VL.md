# PAY_FLOWS_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowsvl-4460.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowsvl-4460.html)

## Columns

- FLOW_ID
- BASE_FLOW_ID
- BASE_FLOW_NAME
- LDG_RQD_FLAG
- DEFAULT_FLOW_FLAG
- OBJECT_VERSION_NUMBER
- MODULE_ID
- LEGISLATIVE_DATA_GROUP_ID
- LEGISLATION_CODE
- ENTERPRISE_ID
- LAST_UPDATE_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_LOGIN
- CREATED_BY
- CREATION_DATE
- START_SCH_TIME_DEF_ID
- FLOW_NAME
- DESCRIPTION
- FORMULA_ID
- START_SCH_FORMULA_ID
- CONNECTOR_TAG
- CONNECTOR_STATUS
- FLOW_TYPE
- OUTBOUND_ENABLED_FLAG
- TASK_COUNT
- TASK_TYPES
- MT_WITHOUT_SOA_FLAG
- IMPL_CLASS_CODE
- TASK_VERSIONING_ENABLED
- SETUP_RULES

## Query

```sql
SELECT b.flow_id, b.base_flow_id, b.base_flow_name, b.ldg_rqd_flag, b.default_flow_flag, b.object_version_number, b.module_id, b.legislative_data_group_id , b.legislation_code , b.enterprise_id , b.last_update_date , b.last_updated_by , b.last_update_login , b.created_by , b.creation_date , b.start_sch_time_def_id, tl.flow_name, tl.description, b.formula_id, b.start_sch_formula_id , b.connector_tag, b.connector_status, b.flow_type, b.outbound_enabled_flag, b.task_count, b.task_types, b.mt_without_soa_flag, b.impl_class_code, b.task_versioning_enabled, b.setup_rules FROM pay_flows b, pay_flows_tl tl WHERE b.flow_id = tl.flow_id AND USERENV('LANG')=tl.language
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
