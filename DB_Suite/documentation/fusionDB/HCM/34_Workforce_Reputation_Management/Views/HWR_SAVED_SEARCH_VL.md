# HWR_SAVED_SEARCH_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsavedsearchvl-6174.html#hwrsavedsearchvl-6174](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsavedsearchvl-6174.html#hwrsavedsearchvl-6174)

## Columns

- SEARCH_ID
- SEARCH_OWNER
- NAME
- COMPONENT_KEY
- SEARCH_MODE
- FILTER
- SEARCH_ORDER
- IS_AUTO_RUN
- IS_DEFAULT
- IS_HIDDEN
- IS_SEEDED_DATA
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.SEARCH_ID, B.SEARCH_OWNER, T.NAME, B.COMPONENT_KEY, B.SEARCH_MODE, B.FILTER, B.SEARCH_ORDER, B.IS_AUTO_RUN, B.IS_DEFAULT, B.IS_HIDDEN, B.IS_SEEDED_DATA, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM HWR_SAVED_SEARCH_B B, HWR_SAVED_SEARCH_TL T WHERE B.SEARCH_ID = T.SEARCH_ID AND T.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
