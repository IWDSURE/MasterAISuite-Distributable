# HRQ_PTCPNT_RESPONSES_V

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqptcpntresponsesv-6251.html#hrqptcpntresponsesv-6251](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqptcpntresponsesv-6251.html#hrqptcpntresponsesv-6251)

## Columns

- PARTICIPANT_ID
- PARTICIPANT_TYPE
- SUBJECT_ID
- SUBJECT_CODE
- SUBSCRIBER_ID
- QUESTIONNAIRE_ID
- QSTNR_QUESTION_ID
- ANSWER_TEXT
- ANSWER_LIST
- QSTN_ANSWER_ID
- ANSWER_CLOB

## Query

```sql
Select P.PARTICIPANT_ID , P.PARTICIPANT_TYPE , P.SUBJECT_ID , P.SUBJECT_CODE , P.SUBSCRIBER_ID , P.QUESTIONNAIRE_ID , R.QSTNR_QUESTION_ID , R.ANSWER_TEXT , R.ANSWER_LIST , R.QSTN_ANSWER_ID , R.ANSWER_CLOB From HRQ_QSTNR_PARTICIPANTS P, HRQ_QSTN_RESPONSES R, HRQ_QSTNR_RESPONSES Q Where Q.qstnr_participant_id = P.qstnr_participant_id and Q.attempt_num = (Select max(Q1.attempt_num) from HRQ_QSTNR_RESPONSES Q1 where Q1.qstnr_participant_id = Q.qstnr_participant_id and Q1.status = 'S') and R.qstnr_response_id = Q.qstnr_response_id
```

---

[← Back to Index](../20_Profile_Management_Views_Index.md)
