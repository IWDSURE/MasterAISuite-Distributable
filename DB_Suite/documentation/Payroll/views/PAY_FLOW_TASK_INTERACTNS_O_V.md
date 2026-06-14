# PAY_FLOW_TASK_INTERACTNS_O_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowtaskinteractnsov-8796.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowtaskinteractnsov-8796.html)

## Columns

- INTERACTION_ID
- BASE_INTERACTION_ID
- BASE_INTERACTION_NAME
- MODULE_ID
- LEGISLATIVE_DATA_GROUP_ID
- LEGISLATION_CODE
- OBJECT_VERSION_NUMBER
- FROM_FLOW_TASK_ID
- INTERACTION_FLOW_ID
- BASE_FLOW_ID
- TO_FLOW_TASK_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- FORMULA_ID

## Query

```sql
SELECT b.INTERACTION_ID, b.BASE_INTERACTION_ID, b.BASE_INTERACTION_NAME, b.MODULE_ID, ldg.LEGISLATIVE_DATA_GROUP_ID, ldg.LEGISLATION_CODE, b.OBJECT_VERSION_NUMBER, b.FROM_FLOW_TASK_ID, b.INTERACTION_FLOW_ID, b.BASE_FLOW_ID, b.TO_FLOW_TASK_ID, b.CREATED_BY, b.CREATION_DATE, b.LAST_UPDATED_BY, b.LAST_UPDATE_DATE, b.LAST_UPDATE_LOGIN, b.formula_id FROM pay_flow_task_interactns b, per_legislative_data_groups ldg WHERE ( (b.legislative_data_group_id IS NOT NULL AND b.legislation_code IS NULL AND b.legislative_data_group_id =ldg.legislative_data_group_id) OR (b.legislation_code IS NOT NULL AND b.legislative_data_group_id IS NULL AND b.legislation_code =ldg.legislation_code AND ( NOT EXISTS ( SELECT NULL FROM pay_flow_task_interactns c1 WHERE b.BASE_INTERACTION_ID = c1.BASE_INTERACTION_ID AND (c1.legislative_data_group_id IS NOT NULL AND c1.legislation_code IS NULL AND c1.legislative_data_group_id =ldg.legislative_data_group_id ) ))) OR ( b.legislative_data_group_id IS NULL AND b.legislation_code IS NULL AND ( NOT EXISTS ( SELECT NULL FROM pay_flow_task_interactns c2 WHERE b.BASE_INTERACTION_ID = c2.BASE_INTERACTION_ID AND ( ( c2.legislative_data_group_id IS NOT NULL AND c2.legislation_code IS NULL AND c2.legislative_data_group_id =ldg.legislative_data_group_id ) OR ( c2.legislation_code IS NOT NULL AND c2.legislative_data_group_id IS NULL AND c2.legislation_code =ldg.legislation_code ) ) ) ) ))
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
