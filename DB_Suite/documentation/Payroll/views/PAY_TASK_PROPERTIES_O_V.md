# PAY_TASK_PROPERTIES_O_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytaskpropertiesov-4470.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytaskpropertiesov-4470.html)

## Columns

- TASK_PROPERTY_ID
- BASE_TASK_PROPERTY_ID
- BASE_TASK_PROPERTY_NAME
- OBJECT_VERSION_NUMBER
- MODULE_ID
- BASE_TASK_ACTION_ID
- TASK_PROPERTY_TYPE
- TASK_PROPERTY_VALUE
- LEGISLATIVE_DATA_GROUP_ID
- LEGISLATION_CODE
- ADDNL_PROPERTY_INFO
- LAST_UPDATE_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_LOGIN
- CREATED_BY
- CREATION_DATE
- TASK_PROPERTY_NAME
- TASK_PROPERTY_DESC

## Query

```sql
SELECT B.TASK_PROPERTY_ID , B.BASE_TASK_PROPERTY_ID, B.BASE_TASK_PROPERTY_NAME, B.OBJECT_VERSION_NUMBER , B.MODULE_ID, B.BASE_TASK_ACTION_ID, B.TASK_PROPERTY_TYPE , B.TASK_PROPERTY_VALUE , ldg.LEGISLATIVE_DATA_GROUP_ID , ldg.LEGISLATION_CODE , B.ADDNL_PROPERTY_INFO, B.LAST_UPDATE_DATE , B.LAST_UPDATED_BY , B.LAST_UPDATE_LOGIN , B.CREATED_BY , B.CREATION_DATE , TL.TASK_PROPERTY_NAME , TL.TASK_PROPERTY_DESC FROM PAY_TASK_PROPERTIES B, PAY_TASK_PROPERTIES_TL TL, per_legislative_data_groups ldg WHERE B.TASK_PROPERTY_ID = TL.TASK_PROPERTY_ID AND USERENV('LANG') =TL.LANGUAGE AND ( (b.legislative_data_group_id IS NOT NULL AND b.legislation_code IS NULL AND b.legislative_data_group_id =ldg.legislative_data_group_id) OR (b.legislation_code IS NOT NULL AND b.legislative_data_group_id IS NULL AND b.legislation_code =ldg.legislation_code AND ( NOT EXISTS ( SELECT null FROM PAY_TASK_PROPERTIES c1 WHERE b.BASE_TASK_PROPERTY_ID = c1.BASE_TASK_PROPERTY_ID AND (c1.legislative_data_group_id IS NOT NULL AND c1.legislation_code IS NULL AND c1.legislative_data_group_id =ldg.legislative_data_group_id ) ))) OR ( b.legislative_data_group_id IS NULL AND b.legislation_code IS NULL AND ( NOT EXISTS ( SELECT null FROM PAY_TASK_PROPERTIES c2 WHERE b.BASE_TASK_PROPERTY_ID = c2.BASE_TASK_PROPERTY_ID AND ( ( c2.legislative_data_group_id IS NOT NULL AND c2.legislation_code IS NULL AND c2.legislative_data_group_id =ldg.legislative_data_group_id ) OR ( c2.legislation_code IS NOT NULL AND c2.legislative_data_group_id IS NULL AND c2.legislation_code =ldg.legislation_code ) ) ) ) ))
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
