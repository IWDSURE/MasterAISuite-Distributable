# PAY_ACTION_CLASSIFICATIONS

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactionclassifications-3836.html#payactionclassifications-3836](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payactionclassifications-3836.html#payactionclassifications-3836)

## Columns

- ACTION_TYPE
- CLASSIFICATION_NAME

## Query

```sql
SELECT PAY_ACTION_CLASSES.ACTION_TYPE ACTION_TYPE, PAY_ACTION_CLASSES.CLASSIFICATION_NAME CLASSIFICATION_NAME FROM PAY_ACTION_CLASSES WITH CHECK OPTION
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
