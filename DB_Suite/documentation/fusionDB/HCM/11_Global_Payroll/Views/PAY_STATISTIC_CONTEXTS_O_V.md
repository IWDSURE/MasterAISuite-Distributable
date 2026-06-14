# PAY_STATISTIC_CONTEXTS_O_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paystatisticcontextsov-3393.html#paystatisticcontextsov-3393](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paystatisticcontextsov-3393.html#paystatisticcontextsov-3393)

## Columns

- STATISTIC_CONTEXT_ID
- BASE_STATISTIC_CONTEXT_ID
- DISPLAY_FLAG
- STATISTIC_CONTEXT_NAME
- LEGISLATION_CODE
- LEGISLATIVE_DATA_GROUP_ID
- MODULE_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- NAME

## Query

```sql
SELECT b.STATISTIC_CONTEXT_ID, b.BASE_STATISTIC_CONTEXT_ID, b.DISPLAY_FLAG, b.STATISTIC_CONTEXT_NAME, ldg.LEGISLATION_CODE, ldg.LEGISLATIVE_DATA_GROUP_ID, b.MODULE_ID, b.CREATED_BY, b.CREATION_DATE, b.LAST_UPDATED_BY, b.LAST_UPDATE_DATE, b.LAST_UPDATE_LOGIN, tl.name FROM PAY_STATISTIC_CONTEXTS b, PAY_STATISTIC_CONTEXTS_TL tl, per_legislative_data_groups ldg WHERE b.STATISTIC_CONTEXT_ID = tl.STATISTIC_CONTEXT_ID AND USERENV('LANG') =tl.language AND ( (b.legislation_code IS NOT NULL AND b.legislation_code =ldg.legislation_code) OR ( b.legislation_code IS NULL AND ( NOT EXISTS ( SELECT null FROM PAY_STATISTIC_CONTEXTS c2 WHERE b.BASE_STATISTIC_CONTEXT_ID = c2.BASE_STATISTIC_CONTEXT_ID AND ( ( c2.legislation_code IS NOT NULL AND c2.legislation_code =ldg.legislation_code ) )) ) ))
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
