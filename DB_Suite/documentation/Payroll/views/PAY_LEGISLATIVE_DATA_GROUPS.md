# PAY_LEGISLATIVE_DATA_GROUPS

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paylegislativedatagroups-7324.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paylegislativedatagroups-7324.html)

## Columns

- LEGISLATIVE_DATA_GROUP_ID
- NAME
- LEGISLATION_CODE
- BUSINESS_GROUP_ID
- DEFAULT_CURRENCY_CODE
- COST_ALLOCATION_ID_FLEX_NUM
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT plg.LEGISLATIVE_DATA_GROUP_ID, plgtl.NAME, plg.LEGISLATION_CODE, plg.BUSINESS_GROUP_ID, plg.DEFAULT_CURRENCY_CODE , plg.COST_ALLOCATION_ID_FLEX_NUM, plg.OBJECT_VERSION_NUMBER, plg.CREATED_BY, plg.CREATION_DATE, plg.LAST_UPDATED_BY, plg.LAST_UPDATE_DATE, plg.LAST_UPDATE_LOGIN FROM PER_LEGISLATIVE_DATA_GROUPS plg, PER_LEGISLATIVE_DATA_GROUPS_TL plgtl WHERE plg.LEGISLATIVE_DATA_GROUP_ID = plgtl.LEGISLATIVE_DATA_GROUP_ID AND plgtl.LANGUAGE = USERENV('lang')
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
