# PAY_FLOW_TASK_PARAMETERS_O_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowtaskparametersov-6987.html#payflowtaskparametersov-6987](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowtaskparametersov-6987.html#payflowtaskparametersov-6987)

## Columns

- FLOW_TASK_PARAM_ID
- BASE_FLOW_TASK_PARAM_ID
- BASE_PARAMETER_NAME
- MODULE_ID
- OBJECT_VERSION_NUMBER
- BASE_FLOW_TASK_ID
- BASE_FLOW_PARAMETER_ID
- BASE_TASK_PARAMETER_ID
- DISPLAY_FLAG
- PARAM_DISP_TYPE
- PARAM_USAGE_TYPE
- PARAM_VALUE_SET
- PARAM_LOOKUP
- PARAM_SEQUENCE
- DEFAULT_TYPE
- DEFAULT_VAL
- LEGISLATIVE_DATA_GROUP_ID
- LEGISLATION_CODE
- LAST_UPDATE_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_LOGIN
- CREATED_BY
- CREATION_DATE
- PARAMETER_NAME
- DESCRIPTION

## Query

```sql
SELECT b.flow_task_param_id , b.base_flow_task_param_id, b.base_parameter_name, b.module_id, b.object_version_number, b.base_flow_task_id , b.base_flow_parameter_id, b.base_task_parameter_id , b.display_flag, b.param_disp_type , b.param_usage_type , b.param_value_set , b.param_lookup , b.param_sequence , b.default_type , b.default_val , ldg.legislative_data_group_id , ldg.legislation_code , b.last_update_date , b.last_updated_by , b.last_update_login , b.created_by , b.creation_date , tl.parameter_name , tl.description FROM pay_flow_task_parameters b, pay_flow_task_parameters_tl tl, per_legislative_data_groups ldg WHERE b.flow_task_param_id = tl.flow_task_param_id AND USERENV('LANG') =tl.language AND ( (b.legislative_data_group_id IS NOT NULL AND b.legislation_code IS NULL AND b.legislative_data_group_id =ldg.legislative_data_group_id) OR (b.legislation_code IS NOT NULL AND b.legislative_data_group_id IS NULL AND b.legislation_code =ldg.legislation_code AND ( NOT EXISTS ( SELECT c1.base_flow_task_param_id FROM pay_flow_task_parameters c1 WHERE b.base_flow_task_param_id = c1.base_flow_task_param_id AND (c1.legislative_data_group_id IS NOT NULL AND c1.legislation_code IS NULL AND c1.legislative_data_group_id =ldg.legislative_data_group_id ) ))) OR ( b.legislative_data_group_id IS NULL AND b.legislation_code IS NULL AND ( NOT EXISTS ( SELECT c2.base_flow_task_param_id FROM pay_flow_task_parameters c2 WHERE b.base_flow_task_param_id = c2.base_flow_task_param_id AND ( ( c2.legislative_data_group_id IS NOT NULL AND c2.legislation_code IS NULL AND c2.legislative_data_group_id =ldg.legislative_data_group_id ) OR ( c2.legislation_code IS NOT NULL AND c2.legislative_data_group_id IS NULL AND c2.legislation_code =ldg.legislation_code ) ) ) ) ))
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
