# HWP_PRED_RESULT_REASONS_V

## Details

**Schema:** FUSION

**Object owner:** HWP

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwppredresultreasonsv-5163.html#hwppredresultreasonsv-5163](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwppredresultreasonsv-5163.html#hwppredresultreasonsv-5163)

## Columns

- PERSON_ID
- ASSIGNMENT_ID
- MODEL_CODE
- PRED_VALUE
- ATTR_CODE
- ATTR_NAME
- ATTRIBUTE_VALUE
- WEIGHT
- WEIGHT_PCT
- PRECEDENCE_ORDER
- REASON_TYPE

## Query

```sql
SELECT hdmr.person_id, hdmr.assignment_id, hdmp.model_code, least(hdm.pred_value, 1) pred_value, hdmr.attr_code attr_code, hav.attr_name, hdmr.attr_value attribute_value, hdmr.pred_weight weight, hdmr.pred_weight_pct * SIGN(hdmr.pred_weight) weight_pct, dense_rank() over(partition BY hdmp.model_code,hdmr.assignment_id,SIGN(hdmr.pred_weight) order by ABS(hdmr.pred_weight) DESC,hdmp.model_code,hdmr.attr_code ) precedence_order, DECODE(hdmp.model_code, 'HWP_ATTR_MODEL', DECODE(SIGN(pred_weight),1,'LEAVING','STAYING'), DECODE(SIGN(pred_weight),1,'HIGH','LOW')) reason_type FROM hwp_data_mining_process hdmp, hwp_data_mining_results hdm, hwp_data_mining_reasons hdmr, hwp_attributes_vl hav WHERE hdm.process_id = hdmp.process_id AND hdmr.process_id = hdm.process_id AND hdmr.person_id = hdm.person_id AND hdmr.attr_code = hav.attr_code AND hdmr.assignment_id = hdm.assignment_id
```

---

[← Back to Index](../33_Workforce_Predictions_Views_Index.md)
