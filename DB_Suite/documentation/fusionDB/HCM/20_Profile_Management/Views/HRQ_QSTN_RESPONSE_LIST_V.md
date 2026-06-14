# HRQ_QSTN_RESPONSE_LIST_V

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnresponselistv-7945.html#hrqqstnresponselistv-7945](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnresponselistv-7945.html#hrqqstnresponselistv-7945)

## Columns

- QSTNR_QUESTION_ID
- QUESTION_ID
- QSTN_VERSION_NUM
- RATING_MODEL_ID
- ANSWER_ID
- SHORT_DESCR
- DESCRIPTION
- SEQ_NUM
- ANSWER_CODE

## Query

```sql
select QQ.qstnr_question_id , Q.question_id , Q.qstn_version_num , Q.rating_model_id , A.qstn_answer_id as ANSWER_ID , A.short_text as SHORT_DESCR , A.long_text as DESCRIPTION , A.seq_num as SEQ_NUM , A.answer_code as ANSWER_CODE from HRQ_QSTNR_QUESTIONS QQ, HRQ_QUESTIONS_B Q, HRQ_QSTN_ANSWERS_VL A Where QQ.QUESTION_ID = Q.QUESTION_ID and QQ.QSTN_VERSION_NUM = Q.QSTN_VERSION_NUM and A.QUESTION_ID(+) = Q.QUESTION_ID and A.QSTN_VERSION_NUM(+) = Q.QSTN_VERSION_NUM and A.BUSINESS_GROUP_ID(+) = Q.BUSINESS_GROUP_ID and Q.QUESTION_TYPE in ('1CHOICE', 'MULTCHOICE')
```

---

[← Back to Index](../20_Profile_Management_Views_Index.md)
