# HWP_DATA_MINING_REASONS_V

## Details

**Schema:** FUSION

**Object owner:** HWP

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpdataminingreasonsv-4036.html#hwpdataminingreasonsv-4036](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpdataminingreasonsv-4036.html#hwpdataminingreasonsv-4036)

## Columns

- ENTERPRISE_ID
- PERSON_ID
- ASSIGNMENT_ID
- ATTR_CODE
- ATTR_VALUE
- ATTR_PRED_WEIGHT_PCT
- PERF_PRED_WEIGHT_PCT

## Query

```sql
SELECT hdmr.enterprise_id, hdmr.person_id, hdmr.assignment_id, hdmr.attr_code, hdmr.attr_value, SUM(DECODE(hdmp.model_code, 'HWP_ATTR_MODEL', SIGN(pred_weight) * pred_weight_pct,0)) attr_pred_weight_pct, SUM(DECODE(hdmp.model_code, 'HWP_PERF_MODEL', SIGN(pred_weight) * pred_weight_pct,0)) perf_pred_weight_pct FROM hwp_data_mining_process hdmp, hwp_data_mining_reasons hdmr WHERE hdmp.process_id = hdmr.process_id GROUP BY hdmr.enterprise_id, hdmr.person_id, hdmr.assignment_id, hdmr.attr_code, hdmr.attr_value
```

---

[← Back to Index](../33_Workforce_Predictions_Views_Index.md)
