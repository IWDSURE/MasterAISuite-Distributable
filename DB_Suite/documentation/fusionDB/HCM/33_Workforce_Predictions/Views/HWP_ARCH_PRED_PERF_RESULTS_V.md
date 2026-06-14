# HWP_ARCH_PRED_PERF_RESULTS_V

## Details

**Schema:** FUSION

**Object owner:** HWP

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwparchpredperfresultsv-7314.html#hwparchpredperfresultsv-7314](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwparchpredperfresultsv-7314.html#hwparchpredperfresultsv-7314)

## Columns

- PERSON_ID
- ASSIGNMENT_ID
- WORKER_PRED_PERF

## Query

```sql
SELECT hdmr.person_id, hdmr.assignment_id, hdmr.pred_value worker_pred_perf FROM hwp_data_mining_process hdmp, hwp_arch_data_mining_results hdmr, hwp_models_b hmb WHERE hdmp.model_code = 'HWP_PERF_MODEL' AND hdmr.process_id = hdmp.process_id AND hdmp.model_code = hmb.model_code
```

---

[← Back to Index](../33_Workforce_Predictions_Views_Index.md)
