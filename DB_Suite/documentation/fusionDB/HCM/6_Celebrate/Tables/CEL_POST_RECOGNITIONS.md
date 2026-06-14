# CEL_POST_RECOGNITIONS

Stores details of a recognition being posted in a transfer process run.

## Details

**Schema:** FUSION

**Object owner:** CEL

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celpostrecognitions-14631.html#celpostrecognitions-14631](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celpostrecognitions-14631.html#celpostrecognitions-14631)

## Primary Key

| Name | Columns |
|------|----------|
| CEL_POST_RECOGNITIONS_PK | RECOGNITION_RUN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RECOGNITION_RUN_ID | NUMBER |  | 18 | Yes | Unique identifier for a recognition run |
| RUN_ID | NUMBER |  | 18 | Yes | Unique identifier for a transfer process run |
| PROGRAM_ID | NUMBER |  | 18 | Yes | Program identifier |
| RECOGNITION_ID | NUMBER |  | 18 | Yes | Recognition identifier |
| PERSON_ID | NUMBER |  | 18 | Yes | Person identifier |
| FROM_PERSON_ID | NUMBER |  | 18 | Yes | Identifier of the person who sent recognition |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Assignment identifier |
| FROM_ASSIGNMENT_ID | NUMBER |  | 18 |  | Identifier of the assignment of the person who sent recognition |
| RECOGNITION_DATE | TIMESTAMP |  |  |  | Recognition Date |
| ACTION_ID | NUMBER |  | 18 |  | Action identifier |
| TYPE_CODE | VARCHAR2 | 30 |  |  | Lookup code that indicates type of program |
| STATUS_CODE | VARCHAR2 | 30 |  |  | Status code |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CEL_POST_RECOGNITIONS_N1 | Non Unique | Default | RUN_ID |
| CEL_POST_RECOGNITIONS_PK | Unique | Default | RECOGNITION_RUN_ID |
| CEL_POST_RECOGNITIONS_U1 | Unique | Default | RECOGNITION_ID, RUN_ID |

---

[← Back to Index](../6_Celebrate_Tables_Index.md)
