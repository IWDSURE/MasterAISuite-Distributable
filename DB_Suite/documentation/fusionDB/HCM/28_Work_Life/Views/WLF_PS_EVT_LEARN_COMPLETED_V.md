# WLF_PS_EVT_LEARN_COMPLETED_V

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfpsevtlearncompletedv-8220.html#wlfpsevtlearncompletedv-8220](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfpsevtlearncompletedv-8220.html#wlfpsevtlearncompletedv-8220)

## Columns

- PERSON_ID
- ASSIGNMENT_ID
- EVENT_YEAR
- EVENT_DATE
- EVENT_DAYS
- EVENT_TITLE
- EVENT_DETAILS
- LINK_TEXT

## Query

```sql
SELECT rec.learner_id person_id, NULL assignment_id, to_char(completion_date, 'YYYY') event_year, completion_date event_date, 0 event_days, '{"strKey":"FdHICompletedlearning"}' event_title, name event_details, '?launchedFrom=myLearnExperience&persona=ORA_LEARNER&learnerRecordId=' || rec.assignment_record_id link_text FROM wlf_assignment_records_f rec, wlf_learning_items_f li, wlf_learning_items_f_tl li_tl WHERE li.learning_item_id = rec.learning_item_id AND li.learning_item_id = li_tl.learning_item_id AND li_tl.language = sys_context('USERENV', 'LANG') AND ( trunc(sysdate) BETWEEN rec.effective_start_date AND rec.effective_end_date ) AND ( trunc(sysdate) BETWEEN li_tl.effective_start_date AND li_tl.effective_end_date ) AND ( trunc(sysdate) BETWEEN li.effective_start_date AND li.effective_end_date ) AND event_type IN ( 'ORA_REQUIRE_ASSIGNMENT', 'ORA_JOIN_ASSIGNMENT' ) AND ( rec.status = 'ORA_ASSN_REC_COMPLETE' AND rec.sub_status IN ( 'ORA_ASSN_REC_COMPLETE', 'ORA_ASSN_REC_BYPASSCOMPLETE' ) ) AND li.learning_item_type IN ( 'ORA_COURSE', 'ORA_SPECIALIZATION', 'ORA_VIDEO', 'ORA_TUTORIAL', 'ORA_ELEARNING', 'ORA_NON_CATALOG', 'ORA_LEGACY' ) AND completion_date <= trunc(SYSDATE)
```

---

[← Back to Index](../28_Work_Life_Views_Index.md)
