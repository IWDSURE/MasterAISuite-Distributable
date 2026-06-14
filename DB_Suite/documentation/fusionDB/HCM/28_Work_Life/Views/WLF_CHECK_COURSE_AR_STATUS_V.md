# WLF_CHECK_COURSE_AR_STATUS_V

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcheckcoursearstatusv-3104.html#wlfcheckcoursearstatusv-3104](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcheckcoursearstatusv-3104.html#wlfcheckcoursearstatusv-3104)

## Columns

- COURSE_ASSIGNMENT_REC_ID
- COURSE_LEARNING_ITEM_ID
- COURSE_STATUS
- COURSE_SUB_STATUS
- COURSE_EFFECTIVE_START_DATE
- COURSE_EFFECTIVE_END_DATE
- CLASS_ASSIGNMENT_REC_ID
- NEW_STATUS
- NEW_SUB_STATUS
- DOUPDATE
- LOC

## Query

```sql
WITH primary_flag_class AS ( SELECT ar.assignment_record_id class_assignment_rec_id, ar.related_object_id course_assignment_rec_id FROM wlf_ar_relations_f ar WHERE ar.primary_flag = 'Y' AND relation_type = 'ORA_OFFERING_COURSE' AND related_object_type = 'ORA_COURSE' AND trunc(SYSDATE) BETWEEN ar.effective_start_date AND ar.effective_end_date ),no_primary_flag AS ( SELECT ar.related_object_id course_assignment_rec_id FROM wlf_ar_relations_f ar WHERE trunc(SYSDATE) BETWEEN ar.effective_start_date AND ar.effective_end_date AND relation_type = 'ORA_OFFERING_COURSE' AND related_object_type = 'ORA_COURSE' GROUP BY related_object_id HAVING MAX(nvl(ar.primary_flag,'N') ) = 'N' ) SELECT course_assignment.assignment_record_id course_assignment_rec_id, course_assignment.learning_item_id course_learning_item_id, course_assignment.status course_status, course_assignment.sub_status course_sub_status, course_assignment.effective_start_date course_effective_start_date, course_assignment.effective_end_date course_effective_end_date, class_assignment.assignment_record_id class_assignment_rec_id, class_assignment.status new_status, class_assignment.sub_status new_sub_status, DECODE(course_assignment.effective_start_date,trunc(SYSDATE),'Y','N') doupdate, '1' LOC FROM primary_flag_class primary_class INNER JOIN wlf_assignment_records_f class_assignment ON class_assignment.assignment_record_id = primary_class.class_assignment_rec_id AND trunc(SYSDATE) BETWEEN class_assignment.effective_start_date AND class_assignment.effective_end_date INNER JOIN wlf_assignment_records_f course_assignment ON course_assignment.assignment_record_id = primary_class.course_assignment_rec_id AND class_assignment.status != course_assignment.status AND class_assignment.sub_status != course_assignment.sub_status AND trunc(SYSDATE) BETWEEN course_assignment.effective_start_date AND course_assignment.effective_end_date AND class_assignment.learner_id = course_assignment.learner_id AND course_assignment.status NOT IN ( 'ORA_ASSN_REC_REQ_REJECTED', 'ORA_ASSN_REC_REJECTED', 'ORA_ASSN_REC_COMPLETE', 'ORA_ASSN_REC_PLANNING' ) AND class_assignment.event_type IN ( 'ORA_JOIN_ASSIGNMENT', 'ORA_REQUIRE_ASSIGNMENT' ) AND course_assignment.event_type IN ( 'ORA_JOIN_ASSIGNMENT', 'ORA_REQUIRE_ASSIGNMENT' ) UNION SELECT course_assignment.assignment_record_id course_assignment_rec_id, course_assignment.learning_item_id course_learning_item_id, course_assignment.status course_status, course_assignment.sub_status course_sub_status, course_assignment.effective_start_date course_effective_start_date, course_assignment.effective_end_date course_effective_end_date, NULL class_assignment_rec_id, 'ORA_ASSN_REC_ACTIVE' new_status, 'ORA_ASSN_REC_NO_OFFR' new_sub_status, DECODE(course_assignment.effective_start_date,trunc(SYSDATE),'Y','N') doupdate, '2' LOC FROM wlf_assignment_records_f course_assignment INNER JOIN wlf_li_courses_f courses ON course_assignment.learning_item_id = courses.learning_item_id AND trunc(nvl(course_assignment.li_effective_date,SYSDATE) ) BETWEEN courses.effective_start_date AND courses.effective_end_date LEFT OUTER JOIN wlf_ar_relations_f ar ON ar.related_object_id = course_assignment.assignment_record_id AND trunc(SYSDATE) BETWEEN ar.effective_start_date AND ar.effective_end_date WHERE ar.relation_id IS NULL AND trunc(SYSDATE) BETWEEN course_assignment.effective_start_date AND course_assignment.effective_end_date AND course_assignment.event_type IN ( 'ORA_JOIN_ASSIGNMENT', 'ORA_REQUIRE_ASSIGNMENT' ) AND course_assignment.status IN ( 'ORA_ASSN_REC_ACTIVE' ) AND course_assignment.sub_status != 'ORA_ASSN_REC_NO_OFFR' UNION SELECT course_assignment.assignment_record_id course_assignment_rec_id, course_assignment.learning_item_id course_learning_item_id, course_assignment.status course_status, course_assignment.sub_status course_sub_status, course_assignment.effective_start_date course_effective_start_date, course_assignment.effective_end_date course_effective_end_date, NULL class_assignment_rec_id, DECODE(course_assignment.is_course_subordinate,'Y','ORA_ASSN_REC_PENDING_ACTIVE',course_assignment.status) new_status, DECODE(course_assignment.is_course_subordinate,'Y','ORA_ASSN_REC_PENDING_ACTIVE',course_assignment.sub_status) new_sub_status, DECODE(course_assignment.effective_start_date,trunc(SYSDATE),'Y','N') doupdate, '3' LOC FROM no_primary_flag INNER JOIN wlf_assignment_records_f course_assignment ON course_assignment.assignment_record_id = no_primary_flag.course_assignment_rec_id AND trunc(SYSDATE) BETWEEN course_assignment.effective_start_date AND course_assignment.effective_end_date AND course_assignment.status NOT IN ( 'ORA_ASSN_REC_PENDING_ACTIVE', 'ORA_ASSN_REC_WITHDRAWN', 'ORA_ASSN_REC_WITHDRAW_PENDING', 'ORA_ASSN_REC_DELETED', 'ORA_ASSN_REC_REQ_REJECTED', 'ORA_ASSN_REC_REJECTED', 'ORA_ASSN_REC_COMPLETE', 'ORA_ASSN_REC_PLANNING' ) WHERE course_assignment.status != DECODE(course_assignment.is_course_subordinate,'Y','ORA_ASSN_REC_PENDING_ACTIVE',course_assignment.status) AND course_assignment.sub_status != DECODE(course_assignment.is_course_subordinate,'Y','ORA_ASSN_REC_PENDING_ACTIVE',course_assignment.sub_status) AND course_assignment.event_type IN ( 'ORA_JOIN_ASSIGNMENT', 'ORA_REQUIRE_ASSIGNMENT' )
```

---

[← Back to Index](../28_Work_Life_Views_Index.md)
