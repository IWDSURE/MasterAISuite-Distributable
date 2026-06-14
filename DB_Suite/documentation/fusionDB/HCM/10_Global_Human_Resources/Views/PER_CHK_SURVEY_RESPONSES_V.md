# PER_CHK_SURVEY_RESPONSES_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchksurveyresponsesv-8616.html#perchksurveyresponsesv-8616](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchksurveyresponsesv-8616.html#perchksurveyresponsesv-8616)

## Columns

- SURVEY_RESPONSE_ID
- SURVEY_CATEGORY
- CHECKLIST_ID
- TASK_IN_CHECKLIST_ID
- PERSON_ID
- ASSIGNMENT_ID
- PERIOD_START_DATE
- PERIOD_END_DATE
- RESPONSE_STATUS
- SUBMIT_DATE
- SCORE
- QUESTIONNAIRE_ID
- QSTNR_PARTICIPANT_ID
- FREQUENCY
- THRESHOLD_SCORE
- ANALYSIS_PERIOD
- ANALYSIS_PERIOD_UOM
- SUBJECT_TYPE
- SUBJECT_KEY
- NAME

## Query

```sql
SELECT rsp.survey_response_id, rsp.survey_category, rsp.checklist_id, rsp.task_in_checklist_id, rsp.person_id, rsp.assignment_id, rsp.period_start_date, rsp.period_end_date, rsp.response_status, rsp.submit_date, rsp.score, rsp.questionnaire_id, rsp.qstnr_participant_id, rsp.frequency, sch.threshold_score, sch.analysis_period, sch.analysis_period_uom, rsp.subject_type, rsp.subject_key, chk.name FROM per_chk_survey_responses rsp, per_checklists_vl chk, per_checklist_schedules sch WHERE survey_type = 'ORA_SURVEY' AND chk.checklist_id = sch.schedule_owner_id AND sch.schedule_owner = 'CHECKLIST'
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
