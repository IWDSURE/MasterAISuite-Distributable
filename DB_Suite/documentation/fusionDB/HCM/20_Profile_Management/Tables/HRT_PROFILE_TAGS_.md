# HRT_PROFILE_TAGS_

This table is used to store tags created by an employee

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofiletags-31319.html#hrtprofiletags-31319](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofiletags-31319.html#hrtprofiletags-31319)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILE_TAGS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, TAG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TAG_ID | NUMBER |  | 18 | Yes | Profile Tag Id |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | BUSINESS_GROUP_ID |
| PROFILE_ID | NUMBER |  | 18 |  | Profile Id |
| TAG | VARCHAR2 | 80 |  |  | Tag |
| CONTENT_TYPE_ID | NUMBER |  | 18 |  | Foreign Key to HRT_CONTENT_TYPES_B |
| CONTENT_ITEM_ID | NUMBER |  | 18 |  | Foreign Key to HRT_CONTENT_ITEMS_B |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PROFILE_TAGSN1_ | Non Unique | Default | TAG_ID, LAST_UPDATE_DATE |
| HRT_PROFILE_TAGS_U1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, TAG_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
