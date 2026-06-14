# PAY_TASK_ACTIONS_O_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytaskactionsov-5529.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytaskactionsov-5529.html)

## Columns

- TASK_ACTION_ID
- BASE_TASK_ACTION_ID
- BASE_TASK_ACTION_NAME
- LEGISLATIVE_DATA_GROUP_ID
- LEGISLATION_CODE
- EXECUTION_MODE
- ACTION_TYPE
- ACTION_METHOD
- ACTION_SEQUENCE
- BASE_TASK_ID
- DEFAULT_ACTION_FLAG
- PARENT_ACTION_FLAG
- OBJECT_VERSION_NUMBER
- MODULE_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- ACTION_NAME
- DESCRIPTION

## Query

```sql
SELECT b.TASK_ACTION_ID TASK_ACTION_ID, b.BASE_TASK_ACTION_ID BASE_TASK_ACTION_ID, b.BASE_TASK_ACTION_NAME BASE_TASK_ACTION_NAME, ldg.LEGISLATIVE_DATA_GROUP_ID LEGISLATIVE_DATA_GROUP_ID, ldg.LEGISLATION_CODE LEGISLATION_CODE, b.EXECUTION_MODE EXECUTION_MODE, b.ACTION_TYPE ACTION_TYPE, b.ACTION_METHOD ACTION_METHOD, b.ACTION_SEQUENCE ACTION_SEQUENCE, b.BASE_TASK_ID BASE_TASK_ID, b.DEFAULT_ACTION_FLAG, b.PARENT_ACTION_FLAG, b.OBJECT_VERSION_NUMBER OBJECT_VERSION_NUMBER, b.MODULE_ID MODULE_ID, b.CREATED_BY CREATED_BY, b.CREATION_DATE CREATION_DATE, b.LAST_UPDATED_BY LAST_UPDATED_BY, b.LAST_UPDATE_DATE LAST_UPDATE_DATE, b.LAST_UPDATE_LOGIN LAST_UPDATE_LOGIN, tl.ACTION_NAME ACTION_NAME, tl.DESCRIPTION DESCRIPTION FROM PAY_TASK_ACTIONS b, PAY_TASK_ACTIONS_TL tl, per_legislative_data_groups ldg WHERE b.TASK_ACTION_ID = tl.TASK_ACTION_ID AND USERENV('LANG') = tl.LANGUAGE AND ( (b.legislative_data_group_id IS NOT NULL AND b.legislation_code IS NULL AND b.legislative_data_group_id =ldg.legislative_data_group_id) OR (b.legislation_code IS NOT NULL AND b.legislative_data_group_id IS NULL AND b.legislation_code =ldg.legislation_code AND ( NOT EXISTS ( SELECT null FROM PAY_TASK_ACTIONS c1 WHERE b.BASE_TASK_ACTION_ID = c1.BASE_TASK_ACTION_ID AND (c1.legislative_data_group_id IS NOT NULL AND c1.legislation_code IS NULL AND c1.legislative_data_group_id =ldg.legislative_data_group_id ) ))) OR ( b.legislative_data_group_id IS NULL AND b.legislation_code IS NULL AND ( NOT EXISTS ( SELECT null FROM PAY_TASK_ACTIONS c2 WHERE b.BASE_TASK_ACTION_ID = c2.BASE_TASK_ACTION_ID AND ( ( c2.legislative_data_group_id IS NOT NULL AND c2.legislation_code IS NULL AND c2.legislative_data_group_id =ldg.legislative_data_group_id ) OR ( c2.legislation_code IS NOT NULL AND c2.legislative_data_group_id IS NULL AND c2.legislation_code =ldg.legislation_code ) ) ) ) ))
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
