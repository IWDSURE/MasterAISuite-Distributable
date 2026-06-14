# HWR_WLNS_QSTN_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsqstnvl-7521.html#hwrwlnsqstnvl-7521](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsqstnvl-7521.html#hwrwlnsqstnvl-7521)

## Columns

- QUESTION_ID
- FUS_PROFILE_ID
- SOURCE_ID
- CONVERSATION_ID
- RESPONSES
- EXPERTS
- IS_VALID
- IS_ANALYZED
- QUESTION_TEXT
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.QUESTION_ID, B.FUS_PROFILE_ID, B.SOURCE_ID, B.CONVERSATION_ID, B.RESPONSES, B.EXPERTS, B.IS_VALID, B.IS_ANALYZED, T.QUESTION_TEXT, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM HWR_WLNS_QSTN_B B, HWR_WLNS_QSTN_TL T WHERE B.QUESTION_ID = T.QUESTION_ID AND T.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
