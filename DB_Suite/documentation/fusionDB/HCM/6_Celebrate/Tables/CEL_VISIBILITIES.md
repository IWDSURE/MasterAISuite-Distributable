# CEL_VISIBILITIES

Table stores visibility override settings for programs

## Details

**Schema:** FUSION

**Object owner:** CEL

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celvisibilities-24346.html#celvisibilities-24346](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celvisibilities-24346.html#celvisibilities-24346)

## Primary Key

| Name | Columns |
|------|----------|
| CEL_VISIBILITIES_PK | VISIBILITY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VISIBILITY_ID | NUMBER |  | 18 | Yes | Surrogate key |
| PERSON_ID | NUMBER |  | 18 | Yes | Unique identifier for a person |
| PROGRAM_ID | NUMBER |  | 18 | Yes | Unique identifier for a celebrate program |
| VISIBILITY_CODE | VARCHAR2 | 30 |  |  | Code that indicates visibility of the awards and recognitions through the program |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CEL_VISIBILITIES_N1 | Non Unique | Default | PERSON_ID |
| CEL_VISIBILITIES_PK | Unique | Default | VISIBILITY_ID |

---

[← Back to Index](../6_Celebrate_Tables_Index.md)
