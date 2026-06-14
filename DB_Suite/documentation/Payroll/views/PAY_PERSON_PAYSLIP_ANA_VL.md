# PAY_PERSON_PAYSLIP_ANA_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypersonpayslipanavl-7114.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypersonpayslipanavl-7114.html)

## Columns

- OBJECT_ACTION_ID
- DELIEVERY_OPTION_NAME
- ACTION_STATUS

## Query

```sql
SELECT pra.PAYROLL_REL_ACTION_ID OBJECT_ACTION_ID, (dl.DELIVERY_OPTION_NAME) ||' - '||lk.meaning delievery_option_name, pay_obj_act.ACTION_STATUS FROM pay_temp_object_actions pay_obj_act,pay_payroll_actions payrollactioneo, pay_payroll_actions bip,pay_payroll_actions xwr, pay_payroll_rel_actions pra, per_ext_delivery_options_vl dl,hcm_lookups lk where payrollactioneo.action_type='XRD' and pay_obj_act.payroll_action_id= payrollactioneo.payroll_action_id AND bip.payroll_action_id=payrollactioneo.target_payroll_action_id AND xwr.payroll_action_id=bip.target_payroll_action_id and pra.payroll_action_id= xwr.payroll_action_id and to_char(pra.PAYROLL_REL_ACTION_ID)=pay_obj_act.PARENT_OBJECT_ID and lookup_type = 'PER_EXT_DELIVERY_TYPES' and lookup_code = dl.delivery_type and dl.EXT_DELIVERY_OPTION_ID=pay_core_utils.get_parameter('delivery_option_id' ,bip.LEGISLATIVE_PARAMETERS)
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
