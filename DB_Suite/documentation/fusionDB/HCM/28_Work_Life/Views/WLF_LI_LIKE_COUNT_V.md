# WLF_LI_LIKE_COUNT_V

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflilikecountv-7229.html#wlflilikecountv-7229](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflilikecountv-7229.html#wlflilikecountv-7229)

## Columns

- LEARNING_ITEM_ID
- LEARNING_ITEM_TYPE
- STATUS
- LIKES_COUNT

## Query

```sql
SELECT Events.LEARNING_ITEM_ID AS LEARNING_ITEM_ID, Learning_Items.LEARNING_ITEM_TYPE, Event_Social.STATUS, COUNT(Events.LEARNING_ITEM_ID) AS LIKES_COUNT FROM WLF_LEARNING_ITEMS_F Learning_Items, WLF_EVENTS Events, WLF_EVENT_SOCIAL Event_Social WHERE TRUNC(SYSDATE) BETWEEN Learning_Items.EFFECTIVE_START_DATE AND Learning_Items.EFFECTIVE_END_DATE AND Learning_Items.LEARNING_ITEM_ID = Events.LEARNING_ITEM_ID AND Events.EVENT_ID = Event_Social.EVENT_ID AND EVENT_TYPE = 'ORA_LI_SOCIAL' AND Events.EVENT_SUB_TYPE = 'ORA_EVT_SUBT_LIKE' GROUP BY Events.LEARNING_ITEM_ID, Learning_Items.LEARNING_ITEM_TYPE, Event_Social.STATUS
```

---

[← Back to Index](../28_Work_Life_Views_Index.md)
