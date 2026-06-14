# PAY_CIR_RET_PLAN_CD_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycirretplancdvl-3874.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycirretplancdvl-3874.html)

## Columns

- COSTING_DISTRIBUTION_ID
- COSTED_ASSIGNMENT_ID
- COSTED_ASSIGNMENT
- PERCENTAGE
- RETIREMENT_PLAN_INSTANCE_ID
- COSTED_DISTRIBUTION_START_DATE
- COSTED_DISTRIBUTION_END_DATE

## Query

```sql
SELECT dist.ENTRY_PCT_DIST_ID COSTING_DISTRIBUTION_ID, asg.assignment_id COSTED_ASSIGNMENT_ID, asg.assignment_number COSTED_ASSIGNMENT, dist.percentage PERCENTAGE, pdcc.DIR_CARD_COMP_ID RETIREMENT_PLAN_INSTANCE_ID, pdcc.EFFECTIVE_START_DATE COSTED_DISTRIBUTION_START_DATE, pdcc.EFFECTIVE_END_DATE COSTED_DISTRIBUTION_END_DATE FROM pay_entry_pct_dist dist, pay_rel_groups_dn asg, pay_element_entries_f ee, PAY_DIR_CARD_COMPONENTS_F pdcc where asg.RELATIONSHIP_GROUP_ID=dist.payroll_assignment_id and asg.group_type='A' and ee.element_entry_id = dist.element_entry_id and ee.creator_id=pdcc.DIR_CARD_COMP_ID
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
