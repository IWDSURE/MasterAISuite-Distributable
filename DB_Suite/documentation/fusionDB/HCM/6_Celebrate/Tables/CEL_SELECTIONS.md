# CEL_SELECTIONS

Table to hold selections for awards or recognitions resulting from activities like nominations

## Details

**Schema:** FUSION

**Object owner:** CEL

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celselections-31361.html#celselections-31361](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celselections-31361.html#celselections-31361)

## Primary Key

| Name | Columns |
|------|----------|
| CEL_SELECTIONS_PK | SELECTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SELECTION_ID | NUMBER |  | 18 | Yes | Unique identifier for a selection |
| PERSON_ID | NUMBER |  | 18 |  | Identifier of person who is selected as the winner. |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Identifier of the assignment of the person who is selected as the winner. |
| PROGRAM_ID | NUMBER |  | 18 | Yes | Unique identifier for a program |
| RECOGNITION_ID | NUMBER |  | 18 |  | Unique identifier for a recognition |
| SELECTOR_PERSON_ID | NUMBER |  | 18 | Yes | Identifier of person who selected the winner. |
| SELECTOR_ASSIGNMENT_ID | NUMBER |  | 18 |  | Identifier of the assignment of the person who selected the winner. |
| SELECTION_DATE | TIMESTAMP |  |  |  | Date of selection |
| STATUS_CODE | VARCHAR2 | 30 |  |  | Status of the selection |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CEL_SELECTIONS_N1 | Non Unique | Default | PROGRAM_ID |
| CEL_SELECTIONS_PK | Unique | Default | SELECTION_ID |

---

[← Back to Index](../6_Celebrate_Tables_Index.md)
