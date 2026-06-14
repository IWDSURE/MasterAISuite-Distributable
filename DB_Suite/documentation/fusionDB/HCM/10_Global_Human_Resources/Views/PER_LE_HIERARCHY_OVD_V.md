# PER_LE_HIERARCHY_OVD_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perlehierarchyovdv-5398.html#perlehierarchyovdv-5398](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perlehierarchyovdv-5398.html#perlehierarchyovdv-5398)

## Columns

- ORGANIZATION_ID
- PARENT_ORGANIZATION_ID
- ALL_ORGANIZATION_ID
- NAME
- LANG_CODE

## Query

```sql
select org_tree2.pk1_value as organization_Id ,org_tree2.ancestor_pk1_value as parent_organization_Id ,org_tree.ancestor_pk1_value as all_organization_Id ,per_org.name ,lower(fnd_lang.iso_language)||'-'|| lower(fnd_lang.iso_territory) as lang_code from per_org_tree_node_rf org_tree ,per_org_tree_node_rf org_tree2 ,hr_organization_units_f_tl per_org ,fnd_languages fnd_lang where org_tree2.tree_structure_code='PER_ORG_TREE_STRUCTURE' and org_tree2.tree_code='VISION_GLOBAL_REPORTING' and org_tree2.tree_structure_code=org_tree.tree_structure_code and org_tree2.tree_code=org_tree.tree_code and org_tree2.pk1_value=org_tree.pk1_value and org_tree2.distance=1 and per_org.language= fnd_lang.language_code and TRUNC(sysdate) between per_org.effective_start_date and per_org.effective_end_date and per_org.organization_id=to_number(org_tree.pk1_value) UNION ALL select org_tree2.pk1_value as organization_Id ,org_tree2.ancestor_pk1_value as parent_organization_Id ,org_tree.ancestor_pk1_value as all_organization_Id ,per_org.name ,to_char(null) as lang_code from per_org_tree_node_rf org_tree ,per_org_tree_node_rf org_tree2 ,hr_organization_units_f_tl per_org ,fnd_languages fnd_lang where org_tree2.tree_structure_code='PER_ORG_TREE_STRUCTURE' and org_tree2.tree_code='VISION_GLOBAL_REPORTING' and org_tree2.tree_structure_code=org_tree.tree_structure_code and org_tree2.tree_code=org_tree.tree_code and org_tree2.pk1_value=org_tree.pk1_value and org_tree2.distance=1 and per_org.language= fnd_lang.language_code and TRUNC(sysdate) between per_org.effective_start_date and per_org.effective_end_date and per_org.organization_id=to_number(org_tree.pk1_value) and fnd_lang.installed_flag='B'
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
