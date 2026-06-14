# HRQ_QSTNR_PART_GSVY_V

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrpartgsvyv-5107.html#hrqqstnrpartgsvyv-5107](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqqstnrpartgsvyv-5107.html#hrqqstnrpartgsvyv-5107)

## Columns

- QSTNR_PARTICIPANT_ID
- BUSINESS_GROUP_ID
- QUESTIONNAIRE_ID
- PARTICIPANT_TYPE
- PARTICIPANT_ID
- SUBSCRIBER_ID
- SUBJECT_CODE
- SUBJECT_ID
- STATUS
- SUBMITTED_DATE_TIME
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_LOGIN
- LAST_UPDATE_DATE

## Query

```sql
SELECT qstnr_participant_id, business_group_id, questionnaire_id, participant_type, participant_id, subscriber_id, subject_code, subject_id, status, submitted_date_time, object_version_number, created_by, creation_date, last_updated_by, last_update_login, last_update_date FROM HRQ_QSTNR_PARTICIPANTS
```

---

[← Back to Index](../20_Profile_Management_Views_Index.md)
