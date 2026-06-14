# PER_CAL_EVENT_COVERAGE

This table holds values used to determine the coverage of the calendar events to people on the system

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/percaleventcoverage-26801.html#percaleventcoverage-26801](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/percaleventcoverage-26801.html#percaleventcoverage-26801)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CAL_EVENT_COVERAGE_PK | CAL_EVENT_COVERAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| CAL_EVENT_COVERAGE_ID | NUMBER |  | 18 | Yes | Unique Calendar Event Coverage Id | Active |
| CALENDAR_EVENT_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_CALENDAR_EVENTS table. | Active |
| TREE_NODE_ID | VARCHAR2 | 32 |  | Yes | Unique identifier for tree node. | Active |
| COVERAGE_FLAG | VARCHAR2 | 30 |  | Yes | Coverage Flag like Include, Exclude or Override | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| OVERRIDE_NAME | VARCHAR2 | 80 |  |  | Override Name of Calendar Event | Active |
| OVERRIDE_CATEGORY | VARCHAR2 | 30 |  |  | Override Category of Calendar Event | Active |
| PARENT_CAL_EVENT_COVERAGE_ID | NUMBER |  | 18 |  | Parent Calendar Event Coverage Id | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CAL_EVENT_COVERAGE_N1 | Non Unique | FUSION_TS_TX_IDX | CALENDAR_EVENT_ID |
| PER_CAL_EVENT_COVERAGE_N2 | Non Unique | FUSION_TS_TX_IDX | PARENT_CAL_EVENT_COVERAGE_ID |
| PER_CAL_EVENT_COVERAGE_N3 | Non Unique | Default | COVERAGE_FLAG |
| PER_CAL_EVENT_COVERAGE_PK | Unique | FUSION_TS_TX_IDX | CAL_EVENT_COVERAGE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
