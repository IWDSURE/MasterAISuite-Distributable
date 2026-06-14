# HR_COST_CENTER_VS_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcostcentervsv-6518.html#hrcostcentervsv-6518](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcostcentervsv-6518.html#hrcostcentervsv-6518)

## Columns

- FLEX_VALUE_SET_NAME
- DESCRIPTION
- FLEX_VALUE_SET_ID

## Query

```sql
SELECT distinct vs.flex_value_set_name, vs.description, vs.flex_value_set_id FROM fnd_flex_value_sets vs, fnd_segment_attribute_values v, fnd_id_flex_segments s WHERE s.application_id = 101 AND s.id_flex_code = 'GL#' AND s.enabled_flag = 'Y' AND v.application_id = s.application_id AND V.id_flex_code = s.id_flex_code AND v.id_flex_num = s.id_flex_num AND v.application_column_name = s.application_column_name AND v.segment_attribute_type = 'FA_COST_CTR' AND v.attribute_value = 'Y' AND s.flex_value_set_id = vs.flex_value_set_id
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
