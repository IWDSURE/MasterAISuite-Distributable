# CEL_PROGRAM_ELIGIBILITY

Stores eligibility profiles linked to recognition and award programs

## Details

**Schema:** FUSION

**Object owner:** CEL

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celprogrameligibility-21657.html#celprogrameligibility-21657](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celprogrameligibility-21657.html#celprogrameligibility-21657)

## Primary Key

| Name | Columns |
|------|----------|
| CEL_PROGRAM_ELIGIBILITY_PK | PROGRAM_ELIGIBILITY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROGRAM_ELIGIBILITY_ID | NUMBER |  | 18 | Yes | Unique identifier for an eligibility profile linked to a program |
| PROGRAM_ID | NUMBER |  | 18 | Yes | Program identifier |
| ELIGIBILITY_PROFILE_ID | NUMBER |  | 18 | Yes | Eligibility profile identifier |
| REQUIRED_FLAG | VARCHAR2 | 1 |  |  | Required flag |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CEL_PROGRAM_ELIGIBILITY_N1 | Non Unique | Default | PROGRAM_ID |
| CEL_PROGRAM_ELIGIBILITY_PK | Unique | Default | PROGRAM_ELIGIBILITY_ID |

---

[← Back to Index](../6_Celebrate_Tables_Index.md)
