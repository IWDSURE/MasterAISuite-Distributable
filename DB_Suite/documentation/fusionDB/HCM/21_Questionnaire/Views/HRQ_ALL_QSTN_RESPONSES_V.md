# HRQ_ALL_QSTN_RESPONSES_V

## Details

**Schema:** FUSION

**Object owner:** HRQ

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqallqstnresponsesv-8755.html#hrqallqstnresponsesv-8755](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqallqstnresponsesv-8755.html#hrqallqstnresponsesv-8755)

## Columns

- QSTNR_RESPONSE_ID
- QSTNR_QUESTION_ID
- BUSINESS_GROUP_ID
- QSTN_RESPONSE_ID
- ANSWER_TYPE
- ANSWER_TEXT
- ANSWER_CLOB
- ANSWER_ID

## Query

```sql
SELECT t.QSTNR_RESPONSE_ID , t.QSTNR_QUESTION_ID , t.BUSINESS_GROUP_ID , t.QSTN_RESPONSE_ID , nvl2( a.ANSWER_ID || t.ANSWER_TEXT , nvl2( a.ANSWER_ID, 'RATING', 'ANSWER' ) , NULL ) AS ANSWER_TYPE , t.ANSWER_TEXT , t.ANSWER_CLOB , a.ANSWER_ID FROM HRQ_QSTN_RESPONSES t ,lateral( SELECT/*+ no_decorrelate */ TRIM(regexp_substr( t.answer_list, '[^,;]+', 1, level )) ANSWER_ID, level FROM (SELECT 1 FROM HRQ_QSTN_RESPONSES WHERE ROWNUM = 1) CONNECT BY regexp_substr( t.answer_list, '[^,;]+', 1, level ) IS NOT NULL )(+) a
```

---

[← Back to Index](../21_Questionnaire_Views_Index.md)
