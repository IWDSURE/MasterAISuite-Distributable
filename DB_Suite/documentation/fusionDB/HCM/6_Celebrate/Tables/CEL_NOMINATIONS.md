# CEL_NOMINATIONS

Table to hold individual nominations.

## Details

**Schema:** FUSION

**Object owner:** CEL

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celnominations-9785.html#celnominations-9785](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celnominations-9785.html#celnominations-9785)

## Primary Key

| Name | Columns |
|------|----------|
| CEL_NOMINATIONS_PK | NOMINATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| NOMINATION_ID | NUMBER |  | 18 | Yes | Unique identifier for a nomination |
| PROGRAM_ID | NUMBER |  | 18 | Yes | Program identifier |
| PERSON_ID | NUMBER |  | 18 |  | Person identifier |
| FROM_PERSON_ID | NUMBER |  | 18 |  | Identifier of the person who sent the nomination |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Assignment Identifier |
| FROM_ASSIGNMENT_ID | NUMBER |  | 18 |  | Identifier of the assignment of the person who sent the nomination |
| NOMINATION_DATE | TIMESTAMP |  |  |  | Date of the nomination |
| STATUS_CODE | VARCHAR2 | 30 |  |  | Status of the nomination |
| NOMINEE_COUNT | NUMBER |  | 3 |  | Number of nominees included in the nomination |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| QUESTIONNAIRE_ID | NUMBER |  | 18 |  | Unique identifier for a questionnaire |
| QSTNR_VERSION_NUM | NUMBER |  | 18 |  | Version number of the questionnaire |
| QSTNR_PARTICIPANT_ID | NUMBER |  | 18 |  | Unique identifier for a questionnaire participant |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CEL_NOMINATIONS_N1 | Non Unique | Default | FROM_PERSON_ID |
| CEL_NOMINATIONS_N2 | Non Unique | Default | PROGRAM_ID |
| CEL_NOMINATIONS_PK | Unique | Default | NOMINATION_ID |

---

[← Back to Index](../6_Celebrate_Tables_Index.md)
