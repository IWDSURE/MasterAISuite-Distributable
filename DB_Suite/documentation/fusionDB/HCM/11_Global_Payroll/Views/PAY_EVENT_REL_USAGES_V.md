# PAY_EVENT_REL_USAGES_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeventrelusagesv-4928.html#payeventrelusagesv-4928](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeventrelusagesv-4928.html#payeventrelusagesv-4928)

## Columns

- EVENT_USAGE_ID
- PROCESS_EVENT_ID
- USAGE_ID
- USAGE_TYPE
- ENTERPRISE_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATE_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_LOGIN
- PAYROLL_RELATIONSHIP_ID
- PROCESS_DATE
- START_DATE
- OVERRIDE_PROCESS_DATE
- PROCESSING_START_DATE
- PROCESSING_END_DATE
- EVENT_REPORT_TYPE
- CREATOR_ID
- CREATOR_TYPE
- APPROVAL_STATUS
- PAYROLL_REL_ACTION_ID
- OBJECT_ID
- OBJECT_TYPE
- SUPERSEDING_EVENT_REL_ID
- OWNER_TYPE
- ORIGINAL_OWNER_TYPE
- EVENT_ACTION_ID

## Query

```sql
SELECT pevtusg.event_usage_id, pevtusg.process_event_id, pevtusg.usage_id, pevtusg.usage_type, pevtusg.enterprise_id, pevtusg.created_by, pevtusg.creation_date, pevtusg.last_update_date, pevtusg.last_updated_by, pevtusg.last_update_login, pevtrel.payroll_relationship_id, pevtrel.process_date, pevtrel.start_date, pevtrel.override_process_date, pevtrel.processing_start_date, pevtrel.processing_end_date, pevtrel.event_report_type, pevtrel.creator_id, pevtrel.creator_type, pevtrel.approval_status, pevtrel.payroll_rel_action_id, pevtrel.object_id, pevtrel.object_type, pevtrel.superseding_event_rel_id, pevtrel.owner_type, pevtrel.original_owner_type, pevtrel.event_action_id FROM pay_event_usages pevtusg, pay_event_relationships pevtrel WHERE pevtusg.usage_id = pevtrel.event_relationship_id AND pevtusg.usage_type = 'PAY_EVENT_RELATIONSHIPS'
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
