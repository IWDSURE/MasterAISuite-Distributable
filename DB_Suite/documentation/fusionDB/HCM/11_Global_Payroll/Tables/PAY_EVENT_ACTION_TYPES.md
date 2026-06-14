# PAY_EVENT_ACTION_TYPES

This is a seeded table of the Event Action Types that can be used by clients.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeventactiontypes-29075.html#payeventactiontypes-29075](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeventactiontypes-29075.html#payeventactiontypes-29075)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_EVENT_ACTION_TYPE_PK | EVENT_ACTION_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_ACTION_TYPE_ID | NUMBER |  | 18 | Yes | Primary Key |
| BASE_NAME | VARCHAR2 | 80 |  | Yes | BASE_NAME |
| REPORT_TYPE_REQUIRED | VARCHAR2 | 5 |  | Yes | Y/N. This denotes whether a Report Type is required for this action. |
| OVERRIDE_ACT_SUBMISSION_FLAG | VARCHAR2 | 5 |  | Yes | Y/N. Indicates whether Action Submission can be overriden. |
| APPLICATION_ID | NUMBER |  | 18 | Yes | Foreign key to the Applications table, |
| ACTION_SUBMISSION | VARCHAR2 | 30 |  | Yes | This denotes how the action will be processed by default. |
| JAVA_CLASS | VARCHAR2 | 2000 |  | Yes | This identifies the Java Class to process this action. |
| DELETE_EVENTS_FLAG | VARCHAR2 | 5 |  | Yes | Y/N. Can the events be deleted after processing. |
| PROCESSING_LEVEL | VARCHAR2 | 30 |  | Yes | The Level that the Action needs to be processed. Person/Assignment/Payroll Relationship. |
| SEGMENT_NAME | VARCHAR2 | 30 |  |  | Name of the Flexfield definition to be used for the Action. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | LEGISLATION_CODE |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ALLOW_MANUAL_NOTIFICATION_FLAG | VARCHAR2 | 1 |  | Yes | Y/N. Flag to Indicate whether Manual Notifications Allowed. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_EVENT_ACTION_TYPES_N20 | Non Unique | Default | SGUID |
| PAY_EVENT_ACTION_TYPE_PK1 | Unique | Default | EVENT_ACTION_TYPE_ID, ORA_SEED_SET1 |
| PAY_EVENT_ACTION_TYPE_PK11 | Unique | Default | EVENT_ACTION_TYPE_ID, ORA_SEED_SET2 |
| PAY_EVENT_ACTION_TYPE_U1 | Unique | Default | BASE_NAME, ENTERPRISE_ID, ORA_SEED_SET1 |
| PAY_EVENT_ACTION_TYPE_U11 | Unique | Default | BASE_NAME, ENTERPRISE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
