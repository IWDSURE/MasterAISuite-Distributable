# IRC_BC_CAND_SCREENINGS

Stores candidate background check screenings outcome for submissions in recruiting

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircbccandscreenings-13184.html#ircbccandscreenings-13184](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircbccandscreenings-13184.html#ircbccandscreenings-13184)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_BC_CAND_SCREENINGS_PK | SCREENING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCREENING_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| OBJECT_STATUS | VARCHAR2 | 30 |  |  | Stores the status of the object. |
| RESULT_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_BC_CAND_RESULTS |
| PHASE_ID | NUMBER |  | 18 |  | Foreign key to IRC_PHASES_B |
| STATE_ID | NUMBER |  | 18 |  | Foreign key to IRC_STATES_B |
| ENTERING_PHASE_FLAG | VARCHAR2 | 1 |  |  | stores the flag whether to trigger a package when entering a corresponding phase |
| LEAVING_PHASE_FLAG | VARCHAR2 | 1 |  |  | stores the flag whether to trigger a package when leaving a corresponding phase |
| EVENT_CODE | VARCHAR2 | 60 |  |  | Stores the event code as a lookup code. The corresponding lookup type is ORA_IRC_PROC_ACTION_EVENT. |
| SCR_PKG_CODE | VARCHAR2 | 30 |  |  | Stores the code identifying the screening package |
| SCR_PKG_NAME | VARCHAR2 | 500 |  | Yes | Stores the name of the screening package |
| SCR_STATUS_CODE | VARCHAR2 | 30 |  | Yes | Stores the status of the screening package.  The corresponding lookup type is ORA_IRC_BC_SCREENING_STATUS |
| SCR_ERROR_DESC | CLOB |  |  |  | Stores the error description for the screening package |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_BC_CAND_SCREENINGS_FK1 | Non Unique | Default | RESULT_ID |
| IRC_BC_CAND_SCREENINGS_FK2 | Non Unique | Default | PHASE_ID |
| IRC_BC_CAND_SCREENINGS_FK3 | Non Unique | Default | STATE_ID |
| IRC_BC_CAND_SCREENINGS_PK | Unique | Default | SCREENING_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
