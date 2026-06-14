# PAY_FLOWS_O_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowsov-3173.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowsov-3173.html)

## Columns

- FLOW_ID
- BASE_FLOW_ID
- BASE_FLOW_NAME
- DEFAULT_FLOW_FLAG
- LDG_RQD_FLAG
- OBJECT_VERSION_NUMBER
- MODULE_ID
- LEGISLATIVE_DATA_GROUP_ID
- LEGISLATION_CODE
- LAST_UPDATE_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_LOGIN
- CREATED_BY
- CREATION_DATE
- START_SCH_TIME_DEF_ID
- FLOW_NAME
- DESCRIPTION
- FORMULA_ID

## Query

```sql
SELECT b.flow_id, b.base_flow_id, b.base_flow_name, b.default_flow_flag, b.ldg_rqd_flag, b.object_version_number, b.module_id, ldg.legislative_data_group_id , ldg.legislation_code , b.last_update_date , b.last_updated_by , b.last_update_login , b.created_by , b.creation_date, b.start_sch_time_def_id, tl.flow_name , tl.description, b.formula_id FROM pay_flows b, pay_flows_tl tl, per_legislative_data_groups ldg WHERE b.flow_id = tl.flow_id AND USERENV('LANG')=tl.language AND ( (b.legislative_data_group_id IS NOT NULL AND b.legislation_code IS NULL AND b.legislative_data_group_id =ldg.legislative_data_group_id) OR (b.legislation_code IS NOT NULL AND b.legislative_data_group_id IS NULL AND b.legislation_code =ldg.legislation_code AND ( NOT EXISTS ( SELECT c1.base_flow_id FROM pay_flows c1 WHERE b.base_flow_id = c1.base_flow_id AND (c1.legislative_data_group_id IS NOT NULL AND c1.legislation_code IS NULL AND c1.legislative_data_group_id =ldg.legislative_data_group_id ) ))) OR ( b.legislative_data_group_id IS NULL AND b.legislation_code IS NULL AND ( NOT EXISTS ( SELECT c2.base_flow_id FROM pay_flows c2 WHERE b.base_flow_id = c2.base_flow_id AND ( ( c2.legislative_data_group_id IS NOT NULL AND c2.legislation_code IS NULL AND c2.legislative_data_group_id =ldg.legislative_data_group_id ) OR ( c2.legislation_code IS NOT NULL AND c2.legislative_data_group_id IS NULL AND c2.legislation_code =ldg.legislation_code ) ) ) ) ))
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
