# HWR_WLNS_NEWS_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsnewsvl-6586.html#hwrwlnsnewsvl-6586](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsnewsvl-6586.html#hwrwlnsnewsvl-6586)

## Columns

- NEWS_ID
- NEWS_TITLE
- NEWS_DESC
- START_DATE
- END_DATE
- NEWS_LINK
- NEWS_IMAGE
- ORDER_RANK
- IS_DELETED
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.NEWS_ID, T.NEWS_TITLE, T.NEWS_DESC, B.START_DATE, B.END_DATE, B.NEWS_LINK, B.NEWS_IMAGE, B.ORDER_RANK, B.IS_DELETED, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM HWR_WLNS_NEWS_B B, HWR_WLNS_NEWS_TL T WHERE B.NEWS_ID = T.NEWS_ID AND T.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
