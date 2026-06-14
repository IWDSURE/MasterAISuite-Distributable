# PAY_PERSON_ARCH_ANA_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypersonarchanavl-6696.html#paypersonarchanavl-6696](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypersonarchanavl-6696.html#paypersonarchanavl-6696)

## Columns

- OBJECT_ACTION_ID
- ZERO_BALANCE_INDICATOR

## Query

```sql
SELECT PRA.PAYROLL_REL_ACTION_ID OBJECT_ACTION_ID, 'N' ZERO_BALANCE_INDICATOR FROM PAY_PAYROLL_REL_ACTIONS PRA, PAY_PAYROLL_ACTIONS PPA WHERE PRA.PAYROLL_ACTION_ID=PPA.PAYROLL_ACTION_ID AND PPA.ACTION_TYPE='PS' AND exists(select 1 from pay_action_information act_info_pymt where act_info_pymt.action_context_id = PRA.payroll_rel_action_id and act_info_pymt.action_context_type = 'PRA' and act_info_pymt.action_information_category like 'GLB_PAY_ARCH_CBID_INFORMATION_FC' and nvl(act_info_pymt.action_information50, 'No') = 'No')
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
