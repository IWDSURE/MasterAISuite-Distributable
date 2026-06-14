# HRQ_ALL_QSTN_ANSWERS_V

## Details

**Schema:** FUSION

**Object owner:** HRQ

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqallqstnanswersv-4420.html#hrqallqstnanswersv-4420](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqallqstnanswersv-4420.html#hrqallqstnanswersv-4420)

## Columns

- QA_QSTN_ANSWER_ID
- QA_BUSINESS_GROUP_ID
- QUESTION_ID
- RATING_LEVEL_ID
- SEQ_NUM
- QAT_QSTN_ANSWER_ID
- QAT_BUSINESS_GROUP_ID
- LANGUAGE
- SHORT_TEXT
- LONG_TEXT

## Query

```sql
select QA.QSTN_ANSWER_ID AS QA_QSTN_ANSWER_ID, QA.BUSINESS_GROUP_ID AS QA_BUSINESS_GROUP_ID, QA.QUESTION_ID, QA.RATING_LEVEL_ID, QA.SEQ_NUM, QAT.QSTN_ANSWER_ID AS QAT_QSTN_ANSWER_ID, QAT.BUSINESS_GROUP_ID AS QAT_BUSINESS_GROUP_ID, QAT.LANGUAGE, QAT.SHORT_TEXT, QAT.LONG_TEXT from HRQ_QSTN_ANSWERS_B QA, HRQ_QSTN_ANSWERS_TL QAT WHERE QA.QSTN_ANSWER_ID = QAT.QSTN_ANSWER_ID AND QA.BUSINESS_GROUP_ID = QAT.BUSINESS_GROUP_ID
```

---

[← Back to Index](../21_Questionnaire_Views_Index.md)
