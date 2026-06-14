# PAY_STATISTIC_CONTEXTS_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paystatisticcontextsvl-6096.html#paystatisticcontextsvl-6096](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paystatisticcontextsvl-6096.html#paystatisticcontextsvl-6096)

## Columns

- STATISTIC_CONTEXT_ID
- BASE_STATISTIC_CONTEXT_ID
- DISPLAY_FLAG
- STATISTIC_CONTEXT_NAME
- LEGISLATION_CODE
- ENTERPRISE_ID
- MODULE_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- NAME
- SGUID

## Query

```sql
SELECT b.STATISTIC_CONTEXT_ID, b.BASE_STATISTIC_CONTEXT_ID, b.DISPLAY_FLAG, b.STATISTIC_CONTEXT_NAME, b.LEGISLATION_CODE, b.ENTERPRISE_ID, b.MODULE_ID, b.CREATED_BY, b.CREATION_DATE, b.LAST_UPDATED_BY, b.LAST_UPDATE_DATE, b.LAST_UPDATE_LOGIN, tl.NAME, b.SGUID SGUID FROM PAY_STATISTIC_CONTEXTS b, PAY_STATISTIC_CONTEXTS_TL tl WHERE b.STATISTIC_CONTEXT_ID = tl.STATISTIC_CONTEXT_ID AND USERENV('LANG') = tl.LANGUAGE
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
