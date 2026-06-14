# CMP_PRE_SALARY_ADDITIONAL_V

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmppresalaryadditionalv-5996.html#cmppresalaryadditionalv-5996](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmppresalaryadditionalv-5996.html#cmppresalaryadditionalv-5996)

## Columns

- SALARY_ID
- DATE_FROM
- ASSIGNMENT_ID
- PREV_AMT_CUR_FREQ

## Query

```sql
SELECT SALARY_ID, DATE_FROM, ASSIGNMENT_ID, cmp_ff_dbi_pkg.get_prev_sal_in_curr_freq(sal.SALARY_ID,sal.DATE_FROM) PREV_AMT_CUR_FREQ FROM CMP_SALARY sal
```

---

[← Back to Index](../7_Compensation_Views_Index.md)
