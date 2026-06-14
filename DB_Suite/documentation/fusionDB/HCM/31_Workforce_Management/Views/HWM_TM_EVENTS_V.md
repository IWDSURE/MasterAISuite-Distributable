# HWM_TM_EVENTS_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmeventsv-6888.html#hwmtmeventsv-6888](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmeventsv-6888.html#hwmtmeventsv-6888)

## Columns

- TM_EVENT_ID
- EVENT_TIME_REAL
- TIMEZONE_OFFSET
- REF_TIMEZONE_ID
- EVENT_TIME_STRING
- REPORTER_ID_TYPE
- REPORTER_ID
- EVENT_TYPE
- PERSON_ID
- RESOURCE_ID
- DEVICE_ID
- TM_EVENT_REQ_ID
- STATUS
- EVENT_STATUS
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- TM_EVENT_CORRECTION_ID
- CORR_BADGE_ID
- CORR_PERSON_ID
- CORR_ASSIGNMENT_ID
- CORR_CREATED_BY
- CORR_CREATION_DATE
- CORR_LAST_UPDATED_BY
- CORR_LAST_UPDATE_DATE
- CORR_LAST_UPDATE_LOGIN

## Query

```sql
SELECT EventPEO.tm_event_id, EventPEO.event_time_real, EventPEO.timezone_offset, NVL(EventPEO.REF_TIMEZONE_ID,SUBSTR(event_time_string,31,(INSTR(event_time_string,']') - INSTR(event_time_string,'['))-1)) as REF_TIMEZONE_ID, EventPEO.event_time_string, EventPEO.reporter_id_type, EventPEO.reporter_id, EventPEO.event_type, EventPEO.person_id, NVL(CorrEventPEO.person_id, EventPEO.person_id) resource_id, EventPEO.device_id, EventPEO.tm_event_req_id, EventPEO.status, EventPEO.event_Status, EventPEO.created_by, EventPEO.creation_date, EventPEO.last_updated_by, EventPEO.last_update_date, EventPEO.last_update_login, CorrEventPEO.tm_event_correction_id, CorrEventPEO.badge_id corr_badge_id, CorrEventPEO.person_id corr_person_id, CorrEventPEO.assignment_id corr_assignment_id, CorrEventPEO.created_by corr_created_by, CorrEventPEO.creation_date corr_creation_date, CorrEventPEO.last_updated_by corr_last_updated_by, CorrEventPEO.last_update_date corr_last_update_date, CorrEventPEO.last_update_login corr_last_update_login FROM fusion.HWM_TM_EVENTS EventPEO, fusion.HWM_TM_EVENT_CORRECTIONS CorrEventPEO WHERE EventPEO.tm_event_id = CorrEventPEO.tm_event_id (+) AND SYSDATE BETWEEN CorrEventPEO.DATE_FROM (+) and CorrEventPEO.DATE_TO (+)
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
