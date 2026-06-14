# WLF_FIX_CLASS_ASSIGN_V

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlffixclassassignv-4994.html#wlffixclassassignv-4994](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlffixclassassignv-4994.html#wlffixclassassignv-4994)

## Columns

- COURSE_ASSIGNMENT_ID
- CLASS_LEARNING_ITEM_ID
- CLASS_LEARNER_ID
- CLASS_ASSIGNMENT_ID
- CLASS_STATUS
- CLASS_EFF_START_DATE
- CLASS_EFF_END_DATE
- CLASS_PRIMARY_FLAG
- CLASS_CREATED_BY
- CLASS_ENTERPRISE_ID
- CLASS_LAST_LOGIN_UPDATE
- AR_EFFECTIVE_START_DATE
- AR_EFFECTIVE_END_DATE
- COMPLETE_ORDER

## Query

```sql
WITH completed_course_assignments AS ( SELECT ar.related_object_id course_assignment_id, arec.learner_id, COUNT(1) assign_count FROM wlf_ar_relations_f ar INNER JOIN wlf_assignment_records_f arec ON arec.assignment_record_id = ar.related_object_id AND arec.status = 'ORA_ASSN_REC_COMPLETE' AND trunc(SYSDATE) BETWEEN arec.effective_start_date AND arec.effective_end_date AND arec.event_type IN ( 'ORA_JOIN_ASSIGNMENT', 'ORA_REQUIRE_ASSIGNMENT' ) WHERE trunc(SYSDATE) BETWEEN ar.effective_start_date AND ar.effective_end_date AND ar.relation_type = 'ORA_OFFERING_COURSE' AND ar.related_object_type = 'ORA_COURSE' GROUP BY ar.related_object_id, arec.learner_id HAVING COUNT(ar.assignment_record_id) > 1 ),incomplete_class_assignments AS ( SELECT course_assignment_id, class_assignments.learning_item_id class_learning_item_id, class_assignments.learner_id class_learner_id, class_assignments.assignment_record_id class_assignment_id, class_assignments.status class_status, class_assignments.effective_start_date class_eff_start_date, class_assignments.effective_end_date class_eff_end_date, class_assignments.event_type class_event_type, class_assignments.completion_date class_completion_date, nvl(ar.primary_flag,'N') class_primary_flag, class_assignments.created_by class_created_by, class_assignments.enterprise_id class_enterprise_id, class_assignments.last_update_login class_last_login_update, ar.effective_start_date ar_effective_start_date, ar.effective_end_date ar_effective_end_date, 2 complete_order FROM completed_course_assignments INNER JOIN wlf_ar_relations_f ar ON ar.related_object_id = completed_course_assignments.course_assignment_id AND trunc(SYSDATE) BETWEEN ar.effective_start_date AND ar.effective_end_date AND ar.relation_type = 'ORA_OFFERING_COURSE' AND ar.related_object_type = 'ORA_COURSE' INNER JOIN wlf_assignment_records_f class_assignments ON class_assignments.assignment_record_id = ar.assignment_record_id AND class_assignments.learner_id = completed_course_assignments.learner_id AND trunc(SYSDATE) BETWEEN class_assignments.effective_start_date AND class_assignments.effective_end_date AND class_assignments.status NOT IN ( 'ORA_ASSN_REC_COMPLETE', 'ORA_ASSN_REC_WITHDRAW_PENDING', 'ORA_ASSN_REC_WITHDRAWN', 'ORA_ASSN_REC_DELETED', 'ORA_ASSN_REC_REJECTED', 'ORA_ASSN_REC_PENDING_ACTIVE' ) AND class_assignments.event_type IN ( 'ORA_JOIN_ASSIGNMENT', 'ORA_REQUIRE_ASSIGNMENT' ) ),complete_class_assignment AS ( SELECT course_assignment_id, class_assignments.learning_item_id class_learning_item_id, class_assignments.learner_id class_learner_id, class_assignments.assignment_record_id class_assignment_id, class_assignments.status class_status, class_assignments.effective_start_date class_eff_start_date, class_assignments.effective_end_date class_eff_end_date, class_assignments.event_type class_event_type, class_assignments.completion_date class_completion_date, nvl(ar.primary_flag,'N') class_primary_flag, class_assignments.created_by class_created_by, class_assignments.enterprise_id class_enterprise_id, class_assignments.last_update_login class_last_login_update, ar.effective_start_date ar_effective_start_date, ar.effective_end_date ar_effective_end_date, 1 complete_order FROM completed_course_assignments INNER JOIN wlf_ar_relations_f ar ON completed_course_assignments.course_assignment_id = ar.related_object_id AND trunc(SYSDATE) BETWEEN ar.effective_start_date AND ar.effective_end_date INNER JOIN wlf_assignment_records_f class_assignments ON ar.assignment_record_id = class_assignments.assignment_record_id AND trunc(SYSDATE) BETWEEN class_assignments.effective_start_date AND class_assignments.effective_end_date AND class_assignments.status = 'ORA_ASSN_REC_COMPLETE' AND ar.relation_type = 'ORA_OFFERING_COURSE' AND ar.related_object_type = 'ORA_COURSE' AND nvl(ar.primary_flag,'N') = 'N' AND class_assignments.event_type IN ( 'ORA_JOIN_ASSIGNMENT', 'ORA_REQUIRE_ASSIGNMENT' ) ) SELECT course_assignment_id, class_learning_item_id, class_learner_id, class_assignment_id, class_status, class_eff_start_date, class_eff_end_date, class_primary_flag, class_created_by, class_enterprise_id, class_last_login_update, ar_effective_start_date, ar_effective_end_date, complete_order FROM ( SELECT * FROM incomplete_class_assignments UNION SELECT * FROM complete_class_assignment ) WHERE course_assignment_id NOT IN ( SELECT related_object_id FROM wlf_ar_relations_f ar INNER JOIN wlf_assignment_records_f arec ON ar.assignment_record_id = arec.assignment_record_id AND trunc(SYSDATE) BETWEEN arec.effective_start_date AND arec.effective_end_date AND arec.status = 'ORA_ASSN_REC_COMPLETE' AND ar.relation_type = 'ORA_OFFERING_COURSE' AND ar.related_object_type = 'ORA_COURSE' AND nvl(ar.primary_flag,'N') = 'Y' AND arec.event_type IN ( 'ORA_JOIN_ASSIGNMENT', 'ORA_REQUIRE_ASSIGNMENT' ) WHERE trunc(SYSDATE) BETWEEN ar.effective_start_date AND ar.effective_end_date GROUP BY related_object_id ) ORDER BY course_assignment_id, class_learner_id, complete_order, class_learning_item_id, class_event_type DESC, class_completion_date DESC
```

---

[← Back to Index](../28_Work_Life_Views_Index.md)
