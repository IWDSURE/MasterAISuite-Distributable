# PER_LOC_ADDRESS_USAGES_X

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perlocaddressusagesx-6791.html#perlocaddressusagesx-6791](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perlocaddressusagesx-6791.html#perlocaddressusagesx-6791)

## Columns

- LOC_ADDRESS_USAGE_ID
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- OBJECT_VERSION_NUMBER
- BUSINESS_GROUP_ID
- ADDRESS_USAGE_TYPE
- LOCATION_ID
- ADDRESS_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
( SELECT "LOC_ADDRESS_USAGE_ID","EFFECTIVE_START_DATE","EFFECTIVE_END_DATE","OBJECT_VERSION_NUMBER","BUSINESS_GROUP_ID","ADDRESS_USAGE_TYPE","LOCATION_ID","ADDRESS_ID","CREATED_BY","CREATION_DATE","LAST_UPDATED_BY","LAST_UPDATE_DATE","LAST_UPDATE_LOGIN" FROM per_loc_address_usages_f WHERE TRUNC(SYSDATE) BETWEEN effective_start_date AND effective_end_date )
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
