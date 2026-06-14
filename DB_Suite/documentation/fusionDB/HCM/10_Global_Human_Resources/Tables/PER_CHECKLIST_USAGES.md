# PER_CHECKLIST_USAGES

Table to track usages of a given checklist template

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistusages-15373.html#perchecklistusages-15373](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistusages-15373.html#perchecklistusages-15373)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHECKLIST_USAGES_PK | USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| USAGE_ID | NUMBER |  | 18 | Yes | USAGE_ID |
| CHECKLIST_ID | NUMBER |  | 18 | Yes | Parent Key to PER_CHECKLISTS_B.CHECKLIST_ID |
| CODE | VARCHAR2 | 400 |  | Yes | Alternate Key |
| USAGE_TYPE | VARCHAR2 | 80 |  | Yes | Lookup: ORA_PER_CHK_USAGE_TYPES |
| ACTION_TYPE | VARCHAR2 | 80 |  | Yes | Lookup: ORA_PER_CHK_USAGE_ACTION_TYPES |
| OBJECT_TYPE | VARCHAR2 | 80 |  | Yes | Lookup: ORA_PER_CHK_USAGE_OBJECT_TYPES |
| OBJECT_KEY | VARCHAR2 | 400 |  | Yes | Foreign Key to the object |
| ENABLED_FLAG | VARCHAR2 | 4 |  | Yes | Lookup: YES_NO |
| START_DATE | DATE |  |  |  | Start date for this link. Defaulted to current date |
| END_DATE | DATE |  |  |  | End data for this link. If not provided the link is valid till end of time |
| CREATOR_TYPE | VARCHAR2 | 80 |  | Yes | Lookup: ORA_PER_CHK_USAGE_CREATOR_TYPES |
| CREATOR_PERSON_ID | NUMBER |  | 18 |  | Foreign key to PER_ALL_PEOPLE_F.PERSON_ID

The person who created this link |
| CREATOR_USER | VARCHAR2 | 64 |  |  | CREATOR_USER |
| WRITE_OUTCOME | VARCHAR2 | 4 |  |  | WRITE_OUTCOME |
| CONTENT_DETAILS1 | VARCHAR2 | 2000 |  |  | CONTENT_DETAILS1 |
| CONTENT_DETAILS2 | VARCHAR2 | 2000 |  |  | CONTENT_DETAILS2 |
| CONTENT_DETAILS3 | VARCHAR2 | 2000 |  |  | CONTENT_DETAILS3 |
| CONTENT_DETAILS4 | VARCHAR2 | 2000 |  |  | CONTENT_DETAILS4 |
| CONTENT_DETAILS5 | VARCHAR2 | 2000 |  |  | CONTENT_DETAILS5 |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CHECKLIST_USAGES_N1 | Non Unique | Default | ACTION_TYPE, USAGE_TYPE, OBJECT_TYPE, OBJECT_KEY |
| PER_CHECKLIST_USAGES_PK | Unique | Default | USAGE_ID |
| PER_CHECKLIST_USAGES_U1 | Unique | Default | CHECKLIST_ID, CODE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
