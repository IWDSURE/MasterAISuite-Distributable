# HWR_WLNS_COACHING_TOPICS_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnscoachingtopicsvl-7946.html#hwrwlnscoachingtopicsvl-7946](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnscoachingtopicsvl-7946.html#hwrwlnscoachingtopicsvl-7946)

## Columns

- COACHING_TOPIC_ID
- IS_ACTIVE
- COACHING_TOPICS_ATTR_1
- COACHING_TOPICS_ATTR_2
- COACHING_TOPICS_ATTR_3
- COACHING_TOPIC_NAME
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.COACHING_TOPIC_ID, B.IS_ACTIVE, B.COACHING_TOPICS_ATTR_1, B.COACHING_TOPICS_ATTR_2, B.COACHING_TOPICS_ATTR_3, T.COACHING_TOPIC_NAME, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM HWR_WLNS_COACHING_TOPICS_B B, HWR_WLNS_COACHING_TOPICS_TL T WHERE B.COACHING_TOPIC_ID = T.COACHING_TOPIC_ID AND T.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
