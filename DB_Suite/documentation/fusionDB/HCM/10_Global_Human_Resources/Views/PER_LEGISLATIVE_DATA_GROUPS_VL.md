# PER_LEGISLATIVE_DATA_GROUPS_VL

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perlegislativedatagroupsvl-4167.html#perlegislativedatagroupsvl-4167](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perlegislativedatagroupsvl-4167.html#perlegislativedatagroupsvl-4167)

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

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
