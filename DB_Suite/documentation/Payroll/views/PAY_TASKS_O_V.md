# PAY_TASKS_O_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytasksov-8694.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytasksov-8694.html)

## Columns

- TASK_ID
- BASE_TASK_ID
- BASE_TASK_NAME
- OBJECT_VERSION_NUMBER
- TASK_TYPE
- MODULE_ID
- DEF_CATEGORY_TYPE
- DEF_SUB_CATEGORY_TYPE
- DEFAULT_CHECKLIST_NAME
- LEGISLATIVE_DATA_GROUP_ID
- LEGISLATION_CODE
- NAME_SPACE
- DEST_UI_URL
- LAST_UPDATE_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_LOGIN
- CREATED_BY
- CREATION_DATE
- AUTOMATIC_FLAG
- ACTION_FREEZE_FLAG
- START_SCH_TIME_DEF_ID
- TASK_NAME
- DESCRIPTION

## Query

```sql
SELECT b.TASK_ID, b.BASE_TASK_ID, b.BASE_TASK_NAME, b.OBJECT_VERSION_NUMBER, b.TASK_TYPE, b.MODULE_ID, b.DEF_CATEGORY_TYPE, b.DEF_SUB_CATEGORY_TYPE, b.DEFAULT_CHECKLIST_NAME, ldg.LEGISLATIVE_DATA_GROUP_ID, ldg.LEGISLATION_CODE, b.NAME_SPACE, b.DEST_UI_URL, b.LAST_UPDATE_DATE, b.LAST_UPDATED_BY, b.LAST_UPDATE_LOGIN, b.CREATED_BY, b.CREATION_DATE, b.AUTOMATIC_FLAG, b.ACTION_FREEZE_FLAG, b.start_sch_time_def_id, tl.TASK_NAME, tl.DESCRIPTION FROM PAY_TASKS b, PAY_TASKS_TL tl, per_legislative_data_groups ldg WHERE b.TASK_ID = tl.TASK_ID AND USERENV('LANG') = tl.LANGUAGE AND ( (b.legislative_data_group_id IS NOT NULL AND b.legislation_code IS NULL AND b.legislative_data_group_id =ldg.legislative_data_group_id) OR (b.legislation_code IS NOT NULL AND b.legislative_data_group_id IS NULL AND b.legislation_code =ldg.legislation_code AND ( NOT EXISTS (SELECT c1.BASE_TASK_ID FROM PAY_TASKS c1 WHERE b.BASE_TASK_ID = c1.BASE_TASK_ID AND (c1.legislative_data_group_id IS NOT NULL AND c1.legislation_code IS NULL AND c1.legislative_data_group_id =ldg.legislative_data_group_id )))) OR ( b.legislative_data_group_id IS NULL AND b.legislation_code IS NULL AND ( NOT EXISTS (SELECT c2.BASE_TASK_ID FROM PAY_TASKS c2 WHERE b.BASE_TASK_ID = c2.BASE_TASK_ID AND ( ( c2.legislative_data_group_id IS NOT NULL AND c2.legislation_code IS NULL AND c2.legislative_data_group_id =ldg.legislative_data_group_id ) OR ( c2.legislation_code IS NOT NULL AND c2.legislative_data_group_id IS NULL AND c2.legislation_code =ldg.legislation_code ) ) ) ) ))
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
