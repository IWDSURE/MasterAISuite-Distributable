# WLF_LEARNING_ORGANIZATIONS_F

Table to store Learning Organizations.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflearningorganizationsf-30553.html#wlflearningorganizationsf-30553](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflearningorganizationsf-30553.html#wlflearningorganizationsf-30553)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LEARN_ORG_PK | LEARNING_ORG_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LEARNING_ORG_ID | NUMBER |  | 18 | Yes | System generated unique identifier |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| LEARNING_ITEM_ID | NUMBER |  | 18 | Yes | Learning Item Id of the learning organization |
| VISIBILITY_ADMIN | VARCHAR2 | 30 |  | Yes | Visibility of the leraning organization |
| VISIBILITY_ESS | VARCHAR2 | 30 |  | Yes | Learning Organization enable for self service users to select |
| ENABLE_FOR_ACCESS | VARCHAR2 | 1 |  |  | Learning Organization enable for access |
| ENABLE_FOR_ASSIGNMENT | VARCHAR2 | 1 |  |  | Learning Organization enable for assignment |
| ENABLE_FOR_MANAGE | VARCHAR2 | 1 |  |  | Learning Organization enable for Manage |
| RECONCILE_TYPE | VARCHAR2 | 30 |  | Yes | Learning Organization reconcile type {MANUAL,AUTOMATIC} |
| RECONCILE_PRIORITY | VARCHAR2 | 30 |  |  | Priority of the learning organization with in the list of learning organiations |
| RECONCILE_START_DATE | TIMESTAMP |  |  |  | Learning Organization Reconcilation Job Start Date |
| RECONCILE_END_DATE | TIMESTAMP |  |  |  | Learning Organization Reconcilation Job End Date |
| RECONCILE_PROCESS_ID | NUMBER |  |  |  | Learning Organization Reconcile Job last run process id |
| RECONCILE_PROCESS_DATE | TIMESTAMP |  |  |  | Learning Organization Reconcilation Job last run process date |
| PROCESSING_STATUS | VARCHAR2 | 30 |  |  | Learning Organization reconcile job processing status. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS |
| IS_SYSTEM_DEFAULT | VARCHAR2 | 1 |  | Yes | Indicates seeded organization or not. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LEARN_ORG_U2 | Unique | Default | LEARNING_ORG_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
