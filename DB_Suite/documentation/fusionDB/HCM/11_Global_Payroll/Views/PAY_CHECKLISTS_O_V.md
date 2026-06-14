# PAY_CHECKLISTS_O_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paychecklistsov-7974.html#paychecklistsov-7974](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paychecklistsov-7974.html#paychecklistsov-7974)

## Columns

- CHECKLIST_ID
- BASE_CHECKLIST_ID
- BASE_CHECKLIST_NAME
- MODULE_ID
- PARENT_CHECKLIST_ID
- BASE_FLOW_ID
- BASE_FLOW_TASK_ID
- CHECKLIST_TYPE
- OWNER_ID
- RUN_SEQUENCE
- DEST_UI_URL
- LAST_UPDATE_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_LOGIN
- CREATED_BY
- OBJECT_VERSION_NUMBER
- CREATION_DATE
- LEGISLATIVE_DATA_GROUP_ID
- LEGISLATION_CODE
- CATEGORY_TYPE
- SUB_CATEGORY_TYPE
- CHECKLIST_NAME
- DESCRIPTION

## Query

```sql
SELECT B.Checklist_Id, B.base_checklist_id, B.base_checklist_name, B.module_id, B.Parent_Checklist_Id, B.Base_Flow_Id, B.Base_Flow_Task_Id, B.Checklist_type, B.Owner_Id, B.RUN_SEQUENCE, B.DEST_UI_URL, B.LAST_UPDATE_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_LOGIN, B.CREATED_BY, B.OBJECT_VERSION_NUMBER, B.CREATION_DATE, ldg.Legislative_data_group_id, ldg.Legislation_code, B.CATEGORY_TYPE, B.SUB_CATEGORY_TYPE, TL.checklist_name, tl.description FROM PAY_CHECKLISTS B, PAY_CHECKLISTS_TL TL, per_legislative_data_groups ldg WHERE B.Checklist_Id = TL.Checklist_Id AND USERENV('LANG') =tl.language AND ( (b.legislative_data_group_id IS NOT NULL AND b.legislation_code IS NULL AND b.legislative_data_group_id =ldg.legislative_data_group_id) OR (b.legislation_code IS NOT NULL AND b.legislative_data_group_id IS NULL AND b.legislation_code =ldg.legislation_code AND ( NOT EXISTS ( SELECT c1.base_flow_id FROM PAY_CHECKLISTS c1 WHERE b.base_Checklist_Id = c1.base_Checklist_Id AND (c1.legislative_data_group_id IS NOT NULL AND c1.legislation_code IS NULL AND c1.legislative_data_group_id =ldg.legislative_data_group_id ) ))) OR ( b.legislative_data_group_id IS NULL AND b.legislation_code IS NULL AND ( NOT EXISTS ( SELECT c2.base_flow_id FROM PAY_CHECKLISTS c2 WHERE b.base_Checklist_Id = c2.base_Checklist_Id AND ( ( c2.legislative_data_group_id IS NOT NULL AND c2.legislation_code IS NULL AND c2.legislative_data_group_id =ldg.legislative_data_group_id ) OR ( c2.legislation_code IS NOT NULL AND c2.legislative_data_group_id IS NULL AND c2.legislation_code =ldg.legislation_code ) ) ) ) ))
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
