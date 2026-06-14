# CEL_RECOGNITIONS

Table to hold individual recognitions.

## Details

**Schema:** FUSION

**Object owner:** CEL

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celrecognitions-13256.html#celrecognitions-13256](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celrecognitions-13256.html#celrecognitions-13256)

## Primary Key

| Name | Columns |
|------|----------|
| CEL_RECOGNITIONS_PK | RECOGNITION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RECOGNITION_ID | NUMBER |  | 18 | Yes | Unique identifier for a recognition |
| PROGRAM_ID | NUMBER |  | 18 | Yes | Program Identifier |
| TYPE_CODE | VARCHAR2 | 30 |  |  | Lookup code that indicates type of program |
| SUB_TYPE_CODE | VARCHAR2 | 30 |  |  | Lookup code that indicates subtype of program |
| PERSON_ID | NUMBER |  | 18 | Yes | Person Identifier |
| FROM_PERSON_ID | NUMBER |  | 18 | Yes | Identifier of the person who sent recognition |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Assignment Identifier |
| FROM_ASSIGNMENT_ID | NUMBER |  | 18 |  | Identifier of the assignment of the person who sent recognition |
| RECOGNITION_DATE | TIMESTAMP |  |  | Yes | Recognition date |
| POINTS | NUMBER |  |  |  | Recognition reward points |
| HEADLINE | VARCHAR2 | 80 |  |  | Headline of the recognition card |
| MESSAGE | VARCHAR2 | 2000 |  |  | Message of the recognition card |
| ILLUSTRATION_ID | NUMBER |  | 18 |  | Identifier of illustration used in recognition |
| VALUE1_ID | NUMBER |  | 18 |  | First value identifier |
| VALUE2_ID | NUMBER |  | 18 |  | Second value identifier |
| VALUE3_ID | NUMBER |  | 18 |  | Third value identifier |
| VALUE4_ID | NUMBER |  | 18 |  | Fourth value identifier |
| VALUE5_ID | NUMBER |  | 18 |  | Fifth value identifier |
| PUBLISHED_FLAG | VARCHAR2 | 1 |  |  | Flag that indicated recognition is published |
| NOTIFIED_FLAG | VARCHAR2 | 1 |  |  | Flag that indicates notification is already sent to employee for the Recognition or Award |
| VISIBILITY_CODE | VARCHAR2 | 30 |  |  | Code that indicates visibility of the awards and recognitions |
| RECORD_CREATOR | VARCHAR2 | 30 |  |  | Creator process of this record. For example, HDL, UI, and ESS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CEL_RECOGNITIONS_N1 | Non Unique | Default | PERSON_ID |
| CEL_RECOGNITIONS_N2 | Non Unique | Default | FROM_PERSON_ID |
| CEL_RECOGNITIONS_N3 | Non Unique | Default | RECOGNITION_DATE |
| CEL_RECOGNITIONS_PK | Unique | Default | RECOGNITION_ID |

---

[← Back to Index](../6_Celebrate_Tables_Index.md)
