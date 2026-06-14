# PER_POS_FUNDING_POSITIONS_F_

This table stores relationships between positions and their funding positions

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perposfundingpositionsf-29912.html#perposfundingpositionsf-29912](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perposfundingpositionsf-29912.html#perposfundingpositionsf-29912)

## Primary Key

| Name | Columns |
|------|----------|
| PER_POS_FUNDING_POS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, FUNDING_RELATIONSHIP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FUNDING_RELATIONSHIP_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| POSITION_ID | NUMBER |  | 18 |  | Position Id |
| FUNDING_POSITION_ID | NUMBER |  | 18 |  | Funding Position Id |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Indicates Business group |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | Foreign Key to PER_ACTION_OCCURRENCES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_POS_FUNDING_POSITIONN1_ | Non Unique | Default | FUNDING_RELATIONSHIP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, LAST_UPDATE_DATE |
| PER_POS_FUNDING_POS_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, FUNDING_RELATIONSHIP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
