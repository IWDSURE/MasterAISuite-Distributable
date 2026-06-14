# HWP_PRED_PERF_REASONS_V

## Details

**Schema:** FUSION

**Object owner:** HWP

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwppredperfreasonsv-7583.html#hwppredperfreasonsv-7583](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwppredperfreasonsv-7583.html#hwppredperfreasonsv-7583)

## Columns

- ENTERPRISE_ID
- PROCESS_ID
- PERSON_ID
- ASSIGNMENT_ID
- ATTR_CODE
- ATTRIBUTE_NAME
- ATTRIBUTE_VALUE
- ATTRIBUTE_UNIT
- DATA_TYPE
- WEIGHT
- WEIGHT_PCT
- PRECEDENCE_ORDER
- REASON_TYPE

## Query

```sql
SELECT hdmr.enterprise_id, hdmr.process_id, hdmr.person_id, hdmr.assignment_id, hab.attr_code attr_code, hab.attr_name attribute_name, hdmr.attr_value attribute_value, decode(hl_units.lookup_code,'PCT','%',hl_units.meaning) attribute_unit, hab.data_type, hdmr.pred_weight weight, hdmr.pred_weight_pct * SIGN(hdmr.pred_weight) weight_pct, dense_rank() over(partition BY assignment_id,SIGN(pred_weight) order by ABS(pred_weight) DESC,hab.attr_code ) precedence_order, DECODE(SIGN(pred_weight),1,'HIGH','LOW') reason_type FROM hwp_data_mining_process hdmp, hwp_data_mining_reasons hdmr, hwp_attributes_vl hab, hr_lookups hl_units WHERE hdmp.model_code = 'HWP_PERF_MODEL' AND hdmr.process_id = hdmp.process_id AND hab.attr_code = hdmr.attr_code AND hab.attr_unit = hl_units.lookup_code(+) AND hl_units.lookup_type(+) = 'HWP_ATTR_UNITS'
```

---

[← Back to Index](../33_Workforce_Predictions_Views_Index.md)
