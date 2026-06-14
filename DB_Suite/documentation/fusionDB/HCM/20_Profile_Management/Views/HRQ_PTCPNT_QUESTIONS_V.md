# HRQ_PTCPNT_QUESTIONS_V

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqptcpntquestionsv-6401.html#hrqptcpntquestionsv-6401](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqptcpntquestionsv-6401.html#hrqptcpntquestionsv-6401)

## Columns

- BUSINESS_GROUP_ID
- QUESTION_ID
- QSTN_VERSION_NUM
- QUESTION_CODE
- QUESTION_TYPE
- QUESTION_TEXT
- QSTNR_SECTION_ID
- QSTNR_QUESTION_ID
- ADHOC_QSTN
- QSTN_SEQ_NUM
- SECTION_SEQ_NUM
- PARTICIPANT_ID
- PARTICIPANT_TYPE
- SUBJECT_ID
- SUBJECT_CODE
- SUBSCRIBER_ID
- SCORED_FLAG
- ENABLE_COMMENTS

## Query

```sql
Select q.business_group_id , q.question_id , q.qstn_version_num , q.question_code , q.question_type , q.question_text , qq.qstnr_section_id , qq.qstnr_question_id , qq.adhoc_qstn , qq.seq_num qstn_seq_num , s.section_seq_num , p.participant_id , p.participant_type , p.subject_id , p.subject_code , p.subscriber_id , q.scored_flag , q.enable_comments From HRQ_QUESTIONS_VL q, HRQ_QSTNR_QUESTIONS qq, HRQ_QSTN_PARTICIPANTS p, HRQ_QSTNR_SECTIONS_B s Where s.qstnr_section_id = qq.qstnr_section_id and q.question_id = qq.question_id and q.qstn_version_num = qq.qstn_version_num and p.qstnr_question_id(+) = QQ.qstnr_question_id and (qq.adhoc_qstn = 'N' or p.participant_id is not null) and q.business_group_id = qq.business_group_id and q.business_group_id = p.business_group_id(+) and q.business_group_id = s.business_group_id
```

---

[← Back to Index](../20_Profile_Management_Views_Index.md)
