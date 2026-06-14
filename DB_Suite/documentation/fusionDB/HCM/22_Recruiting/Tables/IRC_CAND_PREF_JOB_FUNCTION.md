# IRC_CAND_PREF_JOB_FUNCTION

Stores candidate preferred job functions in Recruiting.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandprefjobfunction-20858.html#irccandprefjobfunction-20858](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandprefjobfunction-20858.html#irccandprefjobfunction-20858)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_PREF_JOB_FUNCTION_PK | PREF_JOB_FUNCTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PREF_JOB_FUNCTION_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| CAND_PREF_ID | NUMBER |  | 18 | Yes | Foreign Key to IRC_CAND_PREFERENCES table. |
| JOB_FUNCTION_CODE | VARCHAR2 | 30 |  |  | Stores the job function code from talent community signup from. The corresponding
lookup type is JOB_FUNCTION_CODE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_PREF_JOB_FUNCTION_FK1 | Non Unique | Default | CAND_PREF_ID |
| IRC_CAND_PREF_JOB_FUNCTION_PK | Unique | Default | PREF_JOB_FUNCTION_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
