# HRA_MS_EVT_PD_MGR_TASK_V

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hramsevtpdmgrtaskv-6450.html#hramsevtpdmgrtaskv-6450](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hramsevtpdmgrtaskv-6450.html#hramsevtpdmgrtaskv-6450)

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
SELECT worker_id person_id, assignment_id assignment_id, to_char(hra_eval_steps.due_date, 'YYYY') event_year, hra_eval_steps.due_date event_date, 0 event_days, hra_pf_task_roles_vl.mgr_task_name event_title, hra_tmpl_periods_vl.customary_name event_details, '?evaluationId=' || hra_evaluations.evaluation_id || '&loggedInPersonRole=MANAGER&calledFrom=PERSON_SPOTLIGHT&workerAssignmentId=' || hra_evaluations.assignment_id || '&workerPersonId=' || hra_evaluations.worker_id link_text FROM hra_evaluations, hra_eval_steps, hra_eval_participants, hra_tmpl_defns_b, hra_pf_task_roles_vl, hra_tmpl_periods_vl WHERE hra_evaluations.manager_id = nvl(hrc_session_util.get_user_personid, - 1) AND hra_evaluations.status_code NOT IN ( 'COMP', 'CANCELLED' ) AND hra_evaluations.evaluation_id = hra_eval_steps.evaluation_id AND hra_evaluations.evaluation_id = hra_eval_participants.evaluation_id AND hra_eval_participants.role_type_code = 'MANAGER' AND hra_eval_steps.eval_participant_id = hra_eval_participants.eval_participant_id AND hra_eval_steps.step_code NOT IN ( 'WSEVAL', 'MNG_PCPN_FEEDBACK' ) AND hra_eval_steps.parent_step_id IS NOT NULL AND hra_eval_steps.step_status IN ( 'NOTSTR', 'READY', 'INPROG' ) AND hra_eval_steps.due_date IS NOT NULL AND hra_evaluations.tmpl_period_id = hra_tmpl_periods_vl.tmpl_period_id AND hra_evaluations.template_defn_id = hra_tmpl_defns_b.template_defn_id AND hra_tmpl_defns_b.process_flow_id = hra_pf_task_roles_vl.process_flow_id AND hra_pf_task_roles_vl.task_code = hra_eval_steps.step_code AND hra_evaluations.business_group_id = hra_eval_steps.business_group_id AND hra_evaluations.business_group_id = hra_tmpl_defns_b.business_group_id AND hra_evaluations.business_group_id = hra_pf_task_roles_vl.business_group_id AND hra_evaluations.business_group_id = hra_tmpl_periods_vl.business_group_id
```

---

[← Back to Index](../19_Performance_Management_Views_Index.md)
