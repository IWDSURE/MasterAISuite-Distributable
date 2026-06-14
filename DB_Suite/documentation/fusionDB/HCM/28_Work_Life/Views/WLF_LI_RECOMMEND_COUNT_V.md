# WLF_LI_RECOMMEND_COUNT_V

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflirecommendcountv-3923.html#wlflirecommendcountv-3923](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflirecommendcountv-3923.html#wlflirecommendcountv-3923)

## Columns

- LEARNING_ITEM_ID
- LEARNING_ITEM_TYPE
- STATUS
- RECOMMENDS_COUNT

## Query

```sql
SELECT Events.LEARNING_ITEM_ID, Learning_Items.LEARNING_ITEM_TYPE, Event_Assignments.STATUS as STATUS, Count(Events.LEARNING_ITEM_ID) AS RECOMMENDS_COUNT FROM WLF_LEARNING_ITEMS_F Learning_Items, WLF_EVENTS Events, WLF_EVENT_ASSIGNMENTS_F Event_Assignments WHERE TRUNC(SYSDATE) BETWEEN Learning_Items.EFFECTIVE_START_DATE AND Learning_Items.EFFECTIVE_END_DATE AND EVENT_TYPE ='ORA_RECOMMEND_ASSIGNMENT' AND Events.EVENT_ID = Event_Assignments.EVENT_ID AND TRUNC(SYSDATE) BETWEEN Event_Assignments.EFFECTIVE_START_DATE AND Event_Assignments.EFFECTIVE_END_DATE AND Events.LEARNING_ITEM_ID=Learning_Items.LEARNING_ITEM_ID GROUP BY Events.LEARNING_ITEM_ID, Event_Assignments.STATUS, Learning_Items.LEARNING_ITEM_TYPE
```

---

[← Back to Index](../28_Work_Life_Views_Index.md)
