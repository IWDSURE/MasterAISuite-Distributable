# PAY_EVENT_RELATIONSHIPS

This table contains details of event notifications raised in the system and their current status.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeventrelationships-6242.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeventrelationships-6242.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_EVENT_RELATIONSHIPS_PK | EVENT_RELATIONSHIP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_RELATIONSHIP_ID | NUMBER |  | 18 | Yes | EVENT_RELATIONSHIP_ID |
| PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 |  | PAYROLL_RELATIONSHIP_ID |
| PROCESS_DATE | DATE |  |  | Yes | PROCESS_DATE |
| START_DATE | DATE |  |  | Yes | START_DATE |
| OVERRIDE_PROCESS_DATE | DATE |  |  |  | Overriding process date. |
| PROCESSING_START_DATE | DATE |  |  |  | Date an Time the Event Action starts to process. |
| PROCESSING_END_DATE | DATE |  |  |  | Date and Time Processing Ends |
| EVENT_REPORT_TYPE | VARCHAR2 | 30 |  |  | EVENT_REPORT_TYPE |
| CREATOR_ID | NUMBER |  | 18 |  | CREATOR_ID |
| CREATOR_TYPE | VARCHAR2 | 5 |  |  | CREATOR_TYPE |
| APPROVAL_STATUS | VARCHAR2 | 30 |  |  | APPROVAL_STATUS |
| PAYROLL_REL_ACTION_ID | NUMBER |  | 18 |  | PAYROLL_REL_ACTION_ID |
| OBJECT_ID | NUMBER |  | 18 |  | Object identifier for the Object Type |
| OBJECT_TYPE | VARCHAR2 | 30 |  |  | The Object Type that relates to this Event. |
| SUPERSEDING_EVENT_REL_ID | NUMBER |  | 18 |  | SUPERSEDING_EVENT_REL_ID |
| OWNER_TYPE | VARCHAR2 | 30 |  |  | OWNER_TYPE |
| ORIGINAL_OWNER_TYPE | VARCHAR2 | 30 |  |  | ORIGINAL_OWNER_TYPE |
| EVENT_ACTION_ID | NUMBER |  | 18 |  | Foreign Key to Event Actions |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_EVENT_RELATIONSHIPS_N1 | Non Unique | Default | PAYROLL_REL_ACTION_ID |
| PAY_EVENT_RELATIONSHIPS_N2 | Non Unique | Default | PAYROLL_RELATIONSHIP_ID, PAYROLL_REL_ACTION_ID |
| PAY_EVENT_RELATIONSHIPS_N3 | Non Unique | Default | SUPERSEDING_EVENT_REL_ID |
| PAY_EVENT_RELATIONSHIPS_N4 | Non Unique | Default | OBJECT_ID, OBJECT_TYPE, APPROVAL_STATUS |
| PAY_EVENT_RELATIONSHIPS_PK | Unique | Default | EVENT_RELATIONSHIP_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
