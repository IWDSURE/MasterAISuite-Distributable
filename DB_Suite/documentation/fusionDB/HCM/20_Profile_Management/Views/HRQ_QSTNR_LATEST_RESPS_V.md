# HRQ_QSTNR_LATEST_RESPS_V

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrlatestrespsv-6217.html#hrqqstnrlatestrespsv-6217](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrlatestrespsv-6217.html#hrqqstnrlatestrespsv-6217)

## Columns

- QSTNR_RESPONSE_ID
- QSTNR_PARTICIPANT_ID
- QUESTIONNAIRE_ID
- QSTNR_VERSION_NUM
- PARTICIPANT_ID
- PARTICIPANT_TYPE
- SUBJECT_CODE
- SUBJECT_ID
- SUBSCRIBER_CODE

## Query

```sql
Select R.qstnr_response_id, P.qstnr_participant_id, P.questionnaire_id, R.qstnr_version_num, P.participant_id, p.participant_type, P.subject_code, P.subject_id, S.subscriber_code From HRQ_QSTNR_PARTICIPANTS P, HRQ_QSTNR_RESPONSES R, HRQ_SUBSCRIBERS_B S Where R.qstnr_participant_id = P.qstnr_participant_id and R.attempt_num = (Select max(R1.attempt_num) From HRQ_QSTNR_RESPONSES R1 where R1.qstnr_participant_id = P.qstnr_participant_id and R1.status = 'S') and S.subscriber_id = P.subscriber_id and S.business_group_id = P.business_group_id
```

---

[← Back to Index](../20_Profile_Management_Views_Index.md)
