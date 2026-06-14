# WLF_ADJUST_COURSE_DUEDATE_V

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfadjustcourseduedatev-3070.html#wlfadjustcourseduedatev-3070](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfadjustcourseduedatev-3070.html#wlfadjustcourseduedatev-3070)

## Columns

- COURSE_LEARNING_ITEM_ID
- COURSE_LEARNER_ID
- COURSE_ASSIGNMENT_REC_ID
- COURSE_DUE_DATE
- COURSE_EFFECTIVE_START_DATE
- COURSE_EFFECTIVE_END_DATE
- CLASS_ASSIGNMENT_REC_ID
- CLASS_DUE_DATE

## Query

```sql
SELECT course_assignments.learning_item_id AS course_learning_item_id, course_assignments.learner_id AS course_learner_id, course_assignments.assignment_record_id AS course_assignment_rec_id, course_assignments.calculated_due_date course_due_date, course_assignments.effective_start_date course_effective_start_date, course_assignments.effective_end_date course_effective_end_date, class_assignments.assignment_record_id AS class_assignment_rec_id, class_assignments.calculated_due_date class_due_date FROM wlf_assignment_records_f course_assignments, wlf_ar_relations_f arrelations, wlf_assignment_records_f class_assignments WHERE course_assignments.assignment_record_id = arrelations.related_object_id AND class_assignments.assignment_record_id = arrelations.assignment_record_id AND arrelations.relation_type = 'ORA_OFFERING_COURSE' AND arrelations.related_object_type = 'ORA_COURSE' AND class_assignments.status NOT IN ( 'ORA_ASSN_REC_WITHDRAWN', 'ORA_ASSN_REC_DELETED', 'ORA_ASSN_REC_REQ_REJECTED', 'ORA_ASSN_REC_REJECTED', 'ORA_ASSN_REC_COMPLETE', 'ORA_ASSN_REC_PLANNING' ) AND course_assignments.status NOT IN ( 'ORA_ASSN_REC_WITHDRAWN', 'ORA_ASSN_REC_DELETED', 'ORA_ASSN_REC_REQ_REJECTED', 'ORA_ASSN_REC_REJECTED', 'ORA_ASSN_REC_COMPLETE', 'ORA_ASSN_REC_PLANNING' ) AND trunc(SYSDATE) BETWEEN course_assignments.effective_start_date AND course_assignments.effective_end_date AND trunc(SYSDATE) BETWEEN class_assignments.effective_start_date AND class_assignments.effective_end_date AND trunc(SYSDATE) BETWEEN arrelations.effective_start_date AND arrelations.effective_end_date AND course_assignments.learner_id IS NOT NULL AND trunc(class_assignments.calculated_due_date) < trunc(course_assignments.calculated_due_date) ORDER BY course_assignments.learning_item_id, course_assignments.learner_id
```

---

[← Back to Index](../28_Work_Life_Views_Index.md)
