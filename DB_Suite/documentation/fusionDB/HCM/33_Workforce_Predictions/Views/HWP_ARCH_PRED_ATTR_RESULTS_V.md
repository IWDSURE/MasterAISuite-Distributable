# HWP_ARCH_PRED_ATTR_RESULTS_V

## Details

**Schema:** FUSION

**Object owner:** HWP

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwparchpredattrresultsv-6046.html#hwparchpredattrresultsv-6046](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwparchpredattrresultsv-6046.html#hwparchpredattrresultsv-6046)

## Columns

- PERSON_ID
- ASSIGNMENT_ID
- IS_EMP_PROB

## Query

```sql
SELECT hdmr.person_id, hdmr.assignment_id, hdmr.pred_value is_emp_prob FROM hwp_data_mining_process hdmp, hwp_arch_data_mining_results hdmr, hwp_models_b hmb WHERE hdmp.model_code = 'HWP_ATTR_MODEL' AND hdmr.process_id = hdmp.process_id AND hdmp.model_code = hmb.model_code
```

---

[← Back to Index](../33_Workforce_Predictions_Views_Index.md)
