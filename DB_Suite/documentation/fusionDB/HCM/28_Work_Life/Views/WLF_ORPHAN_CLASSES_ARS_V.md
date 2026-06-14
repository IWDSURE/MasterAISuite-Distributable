# WLF_ORPHAN_CLASSES_ARS_V

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlforphanclassesarsv-6871.html#wlforphanclassesarsv-6871](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlforphanclassesarsv-6871.html#wlforphanclassesarsv-6871)

## Columns

- COURSE_LEARNING_ITEM_ID
- CLASS_LEARNING_ITEM_ID
- LEARNER_ID
- EVENT_TYPE
- EVENT_ASSIGNMENT_ID
- CLASS_ASSIGNMENT_RECORD_ID
- CLASS_ASSIGN_STATUS
- CLASS_ASSIGNED_ON_DATE
- CALCULATED_DUE_DATE
- ENTERPRISE_ID
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- CREATED_BY
- LAST_UPDATE_LOGIN
- COURSE_ASSIGNMENT_RECORD_ID
- COURSE_ASSIGNMENTS_STATUS
- COURSE_EVENT_TYPE
- AR_ONLY

## Query

```sql
WITH orphan_active_class_arec AS ( SELECT li_class.course_learning_item_id course_learning_item_id, class_arec.event_type class_event_type, class_arec.learner_id class_learner_id, class_arec.event_assignment_id class_ea_id, class_arec.learning_item_id class_lid, class_arec.assignment_record_id class_assignment_record_id, class_arec.status class_assign_status, class_arec.enterprise_id, class_arec.effective_start_date, class_arec.effective_end_date, class_arec.assigned_on_date class_assigned_on_date, class_arec.calculated_due_date, class_arec.created_by, class_arec.last_update_login FROM wlf_assignment_records_f class_arec INNER JOIN wlf_li_classes_f li_class ON li_class.learning_item_id = class_arec.learning_item_id AND trunc(SYSDATE) BETWEEN li_class.effective_start_date AND li_class.effective_end_date LEFT OUTER JOIN wlf_ar_relations_f ar ON ar.assignment_record_id = class_arec.assignment_record_id AND trunc(SYSDATE) BETWEEN ar.effective_start_date AND ar.effective_end_date AND relation_type = 'ORA_OFFERING_COURSE' AND related_object_type = 'ORA_COURSE' WHERE ar.relation_id IS NULL AND trunc(SYSDATE) BETWEEN class_arec.effective_start_date AND class_arec.effective_end_date AND class_arec.event_type IN ( 'ORA_JOIN_ASSIGNMENT', 'ORA_REQUIRE_ASSIGNMENT' ) AND class_arec.status = 'ORA_ASSN_REC_ACTIVE' AND class_arec.learner_id IS NOT NULL ),orphan_active_course_arec AS ( SELECT course_arec.assignment_record_id course_arec_id, course_arec.learning_item_id course_lid, course_arec.learner_id course_learner_id, course_arec.status course_arec_status, course_arec.event_type course_event_type, course_arec.event_assignment_id course_ea_id, ar.relation_id, ar.assignment_record_id related_class_arec_id, ROW_NUMBER() OVER( PARTITION BY course_arec.learning_item_id,course_arec.learner_id ORDER BY course_arec.learning_item_id,course_arec.learner_id,course_arec.assigned_on_date ASC ) rnum, ( CASE WHEN orphan_class_arec.class_event_type = 'ORA_REQUIRE_ASSIGNMENT' AND course_arec.event_type = 'ORA_JOIN_ASSIGNMENT' THEN 'N' WHEN orphan_class_arec.class_event_type = 'ORA_JOIN_ASSIGNMENT' AND course_arec.event_type = 'ORA_REQUIRE_ASSIGNMENT' AND trunc(course_arec.assigned_on_date) <= trunc(orphan_class_arec.class_assigned_on_date) THEN 'Y' WHEN orphan_class_arec.class_event_type = course_arec.event_type AND trunc(course_arec.assigned_on_date) <= trunc(orphan_class_arec.class_assigned_on_date) THEN 'Y' ELSE 'N' END ) course_arec_matchable FROM orphan_active_class_arec orphan_class_arec INNER JOIN wlf_assignment_records_f course_arec ON course_arec.learning_item_id = orphan_class_arec.course_learning_item_id AND course_arec.learner_id = orphan_class_arec.class_learner_id LEFT OUTER JOIN wlf_ar_relations_f ar ON ar.related_object_id = course_arec.assignment_record_id AND trunc(SYSDATE) BETWEEN ar.effective_start_date AND ar.effective_end_date AND ar.relation_type = 'ORA_OFFERING_COURSE' AND ar.related_object_type = 'ORA_COURSE' WHERE ar.relation_id IS NULL AND trunc(SYSDATE) BETWEEN course_arec.effective_start_date AND course_arec.effective_end_date AND course_arec.event_type IN ( 'ORA_JOIN_ASSIGNMENT', 'ORA_REQUIRE_ASSIGNMENT' ) AND course_arec.status = 'ORA_ASSN_REC_ACTIVE' AND course_arec.learner_id IS NOT NULL ),target_orphans AS ( SELECT orphan_class_arec.*, orphan_course_arec.course_lid, orphan_course_arec.course_arec_id, orphan_course_arec.course_arec_status, orphan_course_arec.course_event_type, DECODE(orphan_course_arec.course_lid, NULL, 'N', 'Y') ar_only, rnum FROM orphan_active_class_arec orphan_class_arec LEFT OUTER JOIN orphan_active_course_arec orphan_course_arec ON orphan_course_arec.course_lid = orphan_class_arec.course_learning_item_id AND orphan_course_arec.course_learner_id = orphan_class_arec.class_learner_id AND orphan_course_arec.course_arec_matchable = 'Y' AND (rnum IS NULL OR rnum = 1) ) SELECT course_learning_item_id, class_lid class_learning_item_id, class_learner_id learner_id, class_event_type event_type, class_ea_id event_assignment_id, class_assignment_record_id, class_assign_status, class_assigned_on_date, calculated_due_date, enterprise_id, effective_start_date, effective_end_date, created_by, last_update_login, course_arec_id course_assignment_record_id, course_arec_status course_assignments_status, course_event_type, ar_only FROM target_orphans ORDER BY course_learning_item_id, class_event_type, class_learner_id, class_lid
```

---

[← Back to Index](../28_Work_Life_Views_Index.md)
