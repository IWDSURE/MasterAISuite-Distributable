# PER_PERSON_OVD_GROUP_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpersonovdgroupv-8188.html#perpersonovdgroupv-8188](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpersonovdgroupv-8188.html#perpersonovdgroupv-8188)

## Columns

- USER_GUID
- MANAGER_GUID
- ALL_MANAGER_GUID
- ORGANIZATION_TYPE
- ORGANIZATION_ID
- ALL_ORGANIZATION_ID

## Query

```sql
select per_person.user_guid as user_Guid , per_super_per.user_guid as manager_Guid ,per_super_per2.user_guid as all_manager_guid , to_char(null) as organization_Type ,to_number(null) as organization_Id ,to_number(null) as all_organization_Id from per_persons per_person ,per_all_assignments_f per_asg ,per_manager_hrchy_dn per_super ,per_manager_hrchy_dn per_super2 ,per_persons per_super_per ,per_persons per_super_per2 where per_asg.person_id=per_person.person_id and TRUNC(sysdate) between per_asg.effective_start_date AND per_asg.effective_end_date and per_super.assignment_id=per_asg.assignment_id and TRUNC(sysdate) between per_super.effective_start_date AND per_super.effective_end_date and per_super.manager_id=per_super_per.person_id and per_super.manager_level=1 and per_super2.assignment_id=per_asg.assignment_id and TRUNC(sysdate) between per_super2.effective_start_date AND per_super2.effective_end_date and per_super2.manager_id=per_super_per2.person_id UNION ALL select per_person.user_guid as user_Guid ,to_char(null) as manager_Guid , to_char(null) as all_manager_guid ,'BU' as organization_Type ,to_number(org_tree.ancestor_pk1_value) as organization_Id ,to_number(org_tree2.ancestor_pk1_value) as all_organization_Id from per_persons per_person ,per_all_assignments_f per_asg ,per_org_tree_node_rf org_tree ,per_org_tree_node_rf org_tree2 where per_asg.person_id=per_person.person_id and TRUNC(sysdate) between per_asg.effective_start_date AND per_asg.effective_end_date and to_char(per_asg.business_unit_id)=org_tree.pk1_value and org_tree.tree_structure_code=org_tree2.tree_structure_code and org_tree.tree_code=org_tree2.tree_code and to_char(per_asg.business_unit_id)=org_tree2.pk1_value and org_tree2.tree_structure_code='PER_ORG_TREE_STRUCTURE' and org_tree2.tree_code='VISION_GLOBAL_REPORTING' and org_tree2.distance=1 UNION ALL select per_person.user_guid as user_Guid ,to_char(null) as manager_Guid , to_char(null) as all_manager_guid ,'LE' as organization_Type ,to_number(org_tree.ancestor_pk1_value) as organization_Id ,to_number(org_tree2.ancestor_pk1_value) as all_organization_Id from per_persons per_person ,per_all_assignments_f per_asg ,per_org_tree_node_rf org_tree ,per_org_tree_node_rf org_tree2 where per_asg.person_id=per_person.person_id and TRUNC(sysdate) between per_asg.effective_start_date AND per_asg.effective_end_date and to_char(per_asg.legal_entity_id)=org_tree.pk1_value and org_tree.tree_structure_code=org_tree2.tree_structure_code and org_tree.tree_code=org_tree2.tree_code and to_char(per_asg.legal_entity_id)=org_tree2.pk1_value and org_tree2.tree_structure_code='PER_ORG_TREE_STRUCTURE' and org_tree2.tree_code='VISION_GLOBAL_REPORTING' and org_tree2.distance=1 UNION ALL select per_person.user_guid as user_Guid ,to_char(null) as manager_Guid , to_char(null) as all_manager_guid ,'Dept' as organization_Type ,to_number(org_tree.ancestor_pk1_value) as organization_Id ,to_number(org_tree2.ancestor_pk1_value) as all_organization_Id from per_persons per_person ,per_all_assignments_f per_asg ,per_org_tree_node_rf org_tree ,per_org_tree_node_rf org_tree2 where per_asg.person_id=per_person.person_id and TRUNC(sysdate) between per_asg.effective_start_date AND per_asg.effective_end_date and to_char(per_asg.organization_id)=org_tree.pk1_value and org_tree.tree_structure_code=org_tree2.tree_structure_code and org_tree.tree_code=org_tree2.tree_code and to_char(per_asg.organization_id)=org_tree2.pk1_value and org_tree2.tree_structure_code='PER_ORG_TREE_STRUCTURE' and org_tree2.tree_code='VISION_GLOBAL_REPORTING' and org_tree2.distance=1
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
