# IRC_CMT_LAUNCH_RESULTS

Table used for  fetching persisted job results upon subsequent launch processing

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccmtlaunchresults-11537.html#irccmtlaunchresults-11537](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccmtlaunchresults-11537.html#irccmtlaunchresults-11537)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CMT_LAUNCH_RESULTS_PK | RESULT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RESULT_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| LAUNCH_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_CMT_LAUNCHES table |
| RESULT_TYPE | VARCHAR2 | 32 |  | Yes | Stores the result type for the launch |
| RESULT_VALUE | CLOB |  |  |  | Stores job search result for the launch |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CMT_LAUNCH_RESULTS_PK | Unique | Default | RESULT_ID |
| IRC_CMT_LAUNCH_RESULTS_U1 | Unique | Default | LAUNCH_ID, RESULT_TYPE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
