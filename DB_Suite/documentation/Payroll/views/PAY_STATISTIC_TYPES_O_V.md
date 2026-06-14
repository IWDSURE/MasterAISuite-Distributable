# PAY_STATISTIC_TYPES_O_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paystatistictypesov-7477.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paystatistictypesov-7477.html)

## Columns

- STATISTIC_TYPE_ID
- BASE_STATISTIC_TYPE_ID
- DISPLAY_FLAG
- LEGISLATION_CODE
- LEGISLATIVE_DATA_GROUP_ID
- DISPLAY_STAT_NAME
- OBJECT_VERSION_NUMBER
- CATEGORY
- SUB_CATEGORY
- UOM
- STATISTIC_TYPE_NAME
- MODULE_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- NAME

## Query

```sql
SELECT b.STATISTIC_TYPE_ID, b.BASE_STATISTIC_TYPE_ID, b.DISPLAY_FLAG, ldg.LEGISLATION_CODE, ldg.LEGISLATIVE_DATA_GROUP_ID, b.DISPLAY_STAT_NAME, b.OBJECT_VERSION_NUMBER, b.CATEGORY, b.SUB_CATEGORY, b.UOM, b.STATISTIC_TYPE_NAME, b.module_id, b.CREATED_BY, b.CREATION_DATE, b.LAST_UPDATED_BY, b.LAST_UPDATE_DATE, b.LAST_UPDATE_LOGIN, tl.name FROM PAY_STATISTIC_TYPES b, PAY_STATISTIC_TYPES_TL tl, per_legislative_data_groups ldg WHERE b.STATISTIC_TYPE_ID = tl.STATISTIC_TYPE_ID AND USERENV('LANG') =tl.language AND ( (b.legislation_code IS NOT NULL AND b.legislation_code =ldg.legislation_code) OR ( b.legislation_code IS NULL AND ( NOT EXISTS ( SELECT null FROM PAY_STATISTIC_TYPES c2 WHERE b.BASE_STATISTIC_TYPE_ID = c2.BASE_STATISTIC_TYPE_ID AND ( ( c2.legislation_code IS NOT NULL AND c2.legislation_code =ldg.legislation_code ) )) ) ))
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
