# HRT_PROFILE_ITEM_HISTORY

This table stores history of the HRT_PROFILE_ITEMS table

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofileitemhistory-14135.html#hrtprofileitemhistory-14135](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofileitemhistory-14135.html#hrtprofileitemhistory-14135)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILE_ITEM_HISTORY_PK | PROFILE_ITEM_HISTORY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROFILE_ITEM_HISTORY_ID | NUMBER |  | 18 | Yes | System generated primary key |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PROFILE_ITEM_ID | NUMBER |  | 18 | Yes | Foreign Key to HRT_PROFILE_ITEMS table |
| CONTENT_ITEM_ID | NUMBER |  | 18 |  | Foreign Key to HRT_CONTENT_ITEMS_B |
| LAST_VERIFIED_ON | DATE |  |  |  | Date on which the data was verified |
| LAST_VERIFIED_BY | VARCHAR2 | 240 |  |  | Stores details of who verified the data |
| PROFILE_ITEM_DETAILS | CLOB |  |  |  | Stores Details of the Profile Items in XML or JSON format |
| SECTION_ID | NUMBER |  | 18 |  | Foreign Key to HRT_PROFILE_TYP_SECTIONS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PROFILE_ITEM_HISTORY_N1 | Non Unique | Default | PROFILE_ITEM_ID |
| HRT_PROFILE_ITEM_HISTORY_PK | Unique | Default | PROFILE_ITEM_HISTORY_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
