# HRT_PROFILE_VBCS_LISTS

This table relates the profiles with vbcs list table.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilevbcslists-14233.html#hrtprofilevbcslists-14233](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilevbcslists-14233.html#hrtprofilevbcslists-14233)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILE_VBCS_LISTS_PK | PROFILE_VBCS_LIST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROFILE_VBCS_LIST_ID | NUMBER |  | 18 | Yes | unique identifier of the record. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PROFILE_ID | NUMBER |  | 18 | Yes | Foreign Key to HRT_PROFILES_B |
| VBCS_LIST_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_VBCS_LIST table |
| DATE_FROM | DATE |  |  |  | Effective start date for profile list |
| DATE_TO | DATE |  |  |  | Effective end date for profile list |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PROFILE_VBCS_LISTS_PK | Unique | Default | PROFILE_VBCS_LIST_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
