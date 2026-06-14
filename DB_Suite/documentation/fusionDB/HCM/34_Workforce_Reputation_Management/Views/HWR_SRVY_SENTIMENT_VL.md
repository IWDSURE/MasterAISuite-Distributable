# HWR_SRVY_SENTIMENT_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvysentimentvl-3885.html#hwrsrvysentimentvl-3885](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvysentimentvl-3885.html#hwrsrvysentimentvl-3885)

## Columns

- SENTIMENT_ID
- SENTIMENT_URI
- SENTIMENT_NAME
- SENTIMENT_ATTR_1
- SENTIMENT_ATTR_2
- SENTIMENT_ATTR_3
- SENTIMENT_ATTR_4
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.SENTIMENT_ID, B.SENTIMENT_URI, T.SENTIMENT_NAME, B.SENTIMENT_ATTR_1, B.SENTIMENT_ATTR_2, B.SENTIMENT_ATTR_3, B.SENTIMENT_ATTR_4, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM HWR_SRVY_SENTIMENT_B B, HWR_SRVY_SENTIMENT_TL T WHERE B.SENTIMENT_ID = T.SENTIMENT_ID AND T.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
