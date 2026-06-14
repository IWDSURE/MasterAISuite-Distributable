# HWR_WLNS_TASKS_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnstasksvl-4487.html#hwrwlnstasksvl-4487](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnstasksvl-4487.html#hwrwlnstasksvl-4487)

## Columns

- TASK_ID
- TITLE
- START_DATE
- END_DATE
- AWARD_TYPE
- AWARD
- DESCRIPTION
- STATUS
- IS_ACTIVE
- IS_IMAGE
- ORDER_RANK
- ARCHIVE_DATE
- IMAGE
- PUBLISH_START_DATE
- PUBLISH_END_DATE
- TASK_ATTR_1
- TASK_ATTR_2
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.TASK_ID, T.TITLE, B.START_DATE, B.END_DATE, B.AWARD_TYPE, B.AWARD, T.DESCRIPTION, B.STATUS, B.IS_ACTIVE, B.IS_IMAGE, B.ORDER_RANK, B.ARCHIVE_DATE, B.IMAGE, B.PUBLISH_START_DATE, B.PUBLISH_END_DATE, B.TASK_ATTR_1, B.TASK_ATTR_2, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM HWR_WLNS_TASKS_B B, HWR_WLNS_TASKS_TL T WHERE B.TASK_ID = T.TASK_ID AND T.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
