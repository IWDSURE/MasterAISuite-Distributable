# PER_REPRESENTATIVE_BODIES

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perrepresentativebodies-4772.html#perrepresentativebodies-4772](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perrepresentativebodies-4772.html#perrepresentativebodies-4772)

## Columns

- ORGANIZATION_ID
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- BUSINESS_GROUP_ID
- SET_ID
- NAME
- STATUS
- TYPE
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT hao.organization_id ,hao.effective_start_date ,hao.effective_end_date ,hao.business_group_id ,hac.set_id ,haotl.name ,hac.status ,hao.type ,hac.object_version_number ,hac.created_by ,hac.creation_date ,hac.last_updated_by ,hac.last_update_date ,hac.last_update_login FROM hr_org_unit_classifications_f hac, hr_all_organization_units_f hao, hr_organization_units_f_tl haotl WHERE hao.organization_id = hac.organization_id AND hao.organization_id = haotl.organization_id AND (hao.effective_start_date between hac.effective_start_date AND hac.effective_end_date) AND haotl.LANGUAGE = USERENV('LANG') AND haotl.effective_start_date = hao.effective_start_date AND haotl.effective_end_date = hao.effective_end_date AND hac.classification_code = 'REPBODY'
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
