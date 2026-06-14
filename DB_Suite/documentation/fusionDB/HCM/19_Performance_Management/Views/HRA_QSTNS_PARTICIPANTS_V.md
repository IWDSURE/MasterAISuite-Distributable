# HRA_QSTNS_PARTICIPANTS_V

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraqstnsparticipantsv-8346.html#hraqstnsparticipantsv-8346](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraqstnsparticipantsv-8346.html#hraqstnsparticipantsv-8346)

## Columns

- QUESTION_ID
- QSTNR_VERSION_NUM
- QSTNR_QUESTION_ID
- ADHOC_QSTN
- PERSON_ID
- EVALUATION_ID
- ROLE_TYPE_CODE

## Query

```sql
Select QQ.QUESTION_ID, QQ.QSTNR_VERSION_NUM, QQ.QSTNR_QUESTION_ID, QQ.ADHOC_QSTN, PT.PERSON_ID, PT.EVALUATION_ID, PT.ROLE_TYPE_CODE From HRA_EVAL_PARTICIPANTS PT , HRQ_QSTNR_ALL_QSTNS_V QQ , HRQ_QSTNR_LATEST_RESPS_V R Where R.PARTICIPANT_ID (+) = PT.PERSON_ID and R.SUBJECT_ID (+) = PT.EVALUATION_ID and R.SUBJECT_CODE (+) is null and R.SUBSCRIBER_CODE (+) = 'HRA' and R.QUESTIONNAIRE_ID (+) = PT.QUESTIONNAIRE_ID and QQ.QUESTIONNAIRE_ID = PT.QUESTIONNAIRE_ID and (QQ.QSTNR_VERSION_NUM = R.QSTNR_VERSION_NUM or (R.QSTNR_VERSION_NUM is null and QQ.LATEST_VERSION = 'Y')) and (QQ.ADHOC_QSTN = 'N' or exists (Select 1 From HRQ_QSTN_PARTICIPANTS QP Where QP.QSTNR_QUESTION_ID = QQ.QSTNR_QUESTION_ID and QP.PARTICIPANT_ID = PT.PERSON_ID and QP.PARTICIPANT_TYPE is null))
```

---

[← Back to Index](../19_Performance_Management_Views_Index.md)
