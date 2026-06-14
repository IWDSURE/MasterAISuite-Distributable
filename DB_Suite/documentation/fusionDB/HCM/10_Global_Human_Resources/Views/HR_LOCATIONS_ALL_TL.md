# HR_LOCATIONS_ALL_TL

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrlocationsalltl-8655.html#hrlocationsalltl-8655](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrlocationsalltl-8655.html#hrlocationsalltl-8655)

## Columns

- LOCATION_DETAILS_ID
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- LANGUAGE
- OBJECT_VERSION_NUMBER
- LOCATION_CODE
- LOCATION_NAME
- DESCRIPTION
- SOURCE_LANG
- AC_LOCATION_CODE
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
( SELECT "LOCATION_DETAILS_ID","EFFECTIVE_START_DATE","EFFECTIVE_END_DATE","LANGUAGE","OBJECT_VERSION_NUMBER","LOCATION_CODE","LOCATION_NAME","DESCRIPTION","SOURCE_LANG","AC_LOCATION_CODE","CREATED_BY","CREATION_DATE","LAST_UPDATED_BY","LAST_UPDATE_DATE","LAST_UPDATE_LOGIN" FROM per_location_details_f_tl WHERE trunc(sysdate) BETWEEN effective_start_date and effective_end_date )
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
