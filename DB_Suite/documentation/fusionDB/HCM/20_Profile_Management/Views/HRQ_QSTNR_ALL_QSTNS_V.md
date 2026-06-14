# HRQ_QSTNR_ALL_QSTNS_V

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrallqstnsv-4320.html#hrqqstnrallqstnsv-4320](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrallqstnsv-4320.html#hrqqstnrallqstnsv-4320)

## Columns

- QSTNR_QUESTION_ID
- QUESTION_ID
- QSTN_VERSION_NUM
- ADHOC_QSTN
- QUESTIONNAIRE_ID
- QSTNR_VERSION_NUM
- LATEST_VERSION

## Query

```sql
SELECT QQ.qstnr_question_id, QQ.question_id, QQ.qstn_version_num, QQ.adhoc_qstn, Q.questionnaire_id, Q.qstnr_version_num, Q.latest_version FROM HRQ_QUESTIONNAIRES_VL Q, HRQ_QSTNR_SECTIONS_B S, HRQ_QSTNR_QUESTIONS QQ Where S.questionnaire_id = Q.questionnaire_id and S.qstnr_version_num = Q.qstnr_version_num and S.business_group_id = Q.business_group_id and QQ.qstnr_section_id = S.qstnr_section_id and QQ.business_group_id = S.business_group_id
```

---

[← Back to Index](../20_Profile_Management_Views_Index.md)
