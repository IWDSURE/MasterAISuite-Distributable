# IRC_CX_USER_TRK_DATA

This table is used to store the userTracking information realted to candidate experience.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxusertrkdata-4020.html#irccxusertrkdata-4020](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccxusertrkdata-4020.html#irccxusertrkdata-4020)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CX_USER_TRK_DATA_PK | USER_TRACKING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| USER_TRACKING_ID | NUMBER |  | 18 | Yes | The primary key for this table. System generated. |
| USER_ID | VARCHAR2 | 64 |  | Yes | Stores a system generated GUID that uniquely identifies every user of career site, across devices. |
| CANDIDATE_NUMBER | VARCHAR2 | 30 |  |  | Foreign Key to IRC_CANDIDATES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CX_USER_TRK_DATA_FK1 | Non Unique | Default | CANDIDATE_NUMBER |
| IRC_CX_USER_TRK_DATA_PK | Unique | Default | USER_TRACKING_ID |
| IRC_CX_USER_TRK_DATA_UK1 | Unique | Default | USER_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
