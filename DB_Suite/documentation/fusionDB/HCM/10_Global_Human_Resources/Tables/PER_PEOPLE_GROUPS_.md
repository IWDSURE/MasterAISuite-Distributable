# PER_PEOPLE_GROUPS_

This table contains the people group flexfield segment values for individual employee assignments.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpeoplegroups-7464.html#perpeoplegroups-7464](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpeoplegroups-7464.html#perpeoplegroups-7464)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PEOPLE_GROUPS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, PEOPLE_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PEOPLE_GROUP_ID | NUMBER |  | 18 | Yes | System generated primary key. |
| GROUP_NAME | VARCHAR2 | 240 |  |  | Name to identify People Group Key flexfield |
| ID_FLEX_NUM | NUMBER |  | 18 |  | Key flexfield structure foreign key. |
| SUMMARY_FLAG | VARCHAR2 | 1 |  |  | Key Flexfield summary flag |
| ENABLED_FLAG | VARCHAR2 | 1 |  |  | Key Flexfield enabled flag |
| START_DATE_ACTIVE | DATE |  |  |  | Date from which the People Group is Active. |
| END_DATE_ACTIVE | DATE |  |  |  | Date till when the People Group is active. |
| SEGMENT1 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT2 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT3 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT4 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT5 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT6 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT7 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT8 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT9 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT10 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT11 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT12 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT13 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT14 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT15 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT16 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT17 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT18 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT19 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT20 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT21 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT22 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT23 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT24 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT25 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT26 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT27 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT28 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT29 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| SEGMENT30 | VARCHAR2 | 60 |  |  | Key Flexfield: segment of the key flexfield. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Who column: indicates the impersonator who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_PEOPLE_GROUPSN1_ | Non Unique | Default | PEOPLE_GROUP_ID |
| PER_PEOPLE_GROUPS_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, PEOPLE_GROUP_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
