# WLF_ASSIGNMENT_DESTINATIONS_F

Table to store Assignment Destinations.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfassignmentdestinationsf-24487.html#wlfassignmentdestinationsf-24487](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfassignmentdestinationsf-24487.html#wlfassignmentdestinationsf-24487)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_ASSIGNMENT_DEST_F_PK | ASSIGNMENT_DESTINATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASSIGNMENT_DESTINATION_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| EVENT_ASSIGNMENT_ID | NUMBER |  | 18 |  | EVENT_ASSIGNMENT_ID |
| ASSIGNED_TO_ID | NUMBER |  | 18 | Yes | Indicates the person identifier of destination entry. |
| ASSIGNED_TO_TYPE | VARCHAR2 | 30 |  |  | ASSIGNED_TO_TYPE |
| OPERATION | VARCHAR2 | 30 |  | Yes | Destination entry operation  { INCLUDE, EXCLUDE }. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| STATUS | VARCHAR2 | 30 |  |  | Assignment Destination status: ACTIVE, INACTIVE, REQUESTED, REJECTED |
| DESTINATION_LOCK_TYPE | VARCHAR2 | 30 |  |  | Destination lock date type : CREATION , LATEST |
| DESTINATION_LOCK_DATE | DATE |  |  |  | The lock date of the destination |
| LAST_7_ELAPSED_DURATION | VARCHAR2 | 4000 |  |  | Comma separated last seven elapsed duration |
| PREVIOUS_ELAPSED_DURATION | NUMBER |  | 18 |  | Previous elapsed duration to process destination |
| LAST_7_ELAPSED_DURATION_TWO_SD | NUMBER |  | 18 |  | Two standard deviations timing of last seven successful runs |
| PROCESSED_DATE | TIMESTAMP |  |  |  | Destination processed date |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_ASSIGNMENT_DEST_F_N1 | Non Unique | Default | EVENT_ASSIGNMENT_ID |
| WLF_ASSIGNMENT_DEST_F_N2 | Non Unique | Default | OPERATION |
| WLF_ASSIGNMENT_DEST_F_N3 | Non Unique | Default | ASSIGNED_TO_ID |
| WLF_ASSIGNMENT_DEST_F_N4 | Non Unique | Default | PREVIOUS_ELAPSED_DURATION |
| WLF_ASSIGNMENT_DEST_F_N5 | Non Unique | Default | PROCESSED_DATE |
| WLF_ASSIGNMENT_DEST_F_U1 | Unique | Default | ASSIGNMENT_DESTINATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
